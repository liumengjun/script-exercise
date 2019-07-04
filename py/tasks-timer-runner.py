"""
延时执行任务demo：
有一个任务队列，不定时向任务队列添加任务。添加任务后安排稍后执行，如果期间又添加了任务，也一并执行；不向任务队列添加任务，不安排。
"""
from collections import deque
import time
from datetime import datetime
import threading
import random
import signal


def _print2(*args, **kwargs):
    cur_thread = threading.current_thread()
    print(datetime.now(), '[' + cur_thread.name + ']', *args, **kwargs)


class TasksTimerRunner(object):
    # task_queue = [] is bad, other alternate choices are queue.Queue(), asyncio.Queue(), here just use deque
    _task_queue = deque()
    _scheduled = False
    _doing = False
    _shutdown_signals_registered = False
    _closing = False
    _tasks_handler = None
    _delay = 5.0

    def __init__(self, tasks_handler=None, delay=5.0, deal_shutdown_signals=True):
        """

        :param tasks_handler: 自定义tasks处理函数
        :param delay: threading.Timer延时，单位s
        :param deal_shutdown_signals: 是否处理shutdown信号，有的框架会处理shutdown信号，防止冲突
        """
        if tasks_handler and callable(tasks_handler):
            self._tasks_handler = tasks_handler
        if delay >= 0.0:
            self._delay = delay
        if deal_shutdown_signals:
            self._install_shutdown_signals()

    def is_closing(self):
        return self._closing

    def add_task(self, task, delay=None):
        """
        添加任务，并安排一个timer做job
        """
        if self._closing:
            raise Exception("runner is closing")
        self._task_queue.append(task)
        self._schedule_timer(delay)

    def _schedule_timer(self, delay=None):
        """
        安排一个timer做job，如果已经安排了，就不在安排
        """
        if self._scheduled:
            return
        self._scheduled = True
        # delay 秒后运行job
        if delay is None:
            delay = self._delay
        threading.Timer(delay, self._job).start()
        # threading.Timer(6, _job).start()

    def _job(self):
        if self._doing:
            return
        self._doing = True
        self.run_now()
        self._doing = False
        self._scheduled = False
        if self._task_queue:
            # 处理遗留任务
            self._schedule_timer()

    def run_now(self):
        """
        执行tasks。一般在threading.Timer中调用，否则表示立即执行任务
        这里保证每一个任务仅执行一遍。即使安排了多个timer
        """
        _print2('start job'.center(80, '-'))
        # copy() clear()两次操作不能保证原子性，可能导致task丢失。如果正在doing就不要添加task也不好控制。
        # tasks = task_queue.copy()
        # task_queue.clear()
        # 此处使用FIFO方式，deque popleft()是线程安全的，但可能抛出异常。
        tasks = []
        try:
            for _ in range(len(self._task_queue)):
                tasks.append(self._task_queue.popleft())
        except:
            pass
        if tasks:
            _print2("do task:", tasks)
            if self._tasks_handler:
                try:
                    self._tasks_handler(tasks)
                except Exception as err:
                    _print2("Failed to call tasks_handler, error: ", err)
        else:
            _print2("Nothing to do")
        _print2('end job'.center(80, '-'))

    def _shutdown_handler(self, signum, _):
        _print2('catch signal: %s, shutdown later...' % signum)
        self._closing = True
        self.run_now()

    def _install_shutdown_signals(self):
        if self._shutdown_signals_registered:
            return
        self._shutdown_signals_registered = True
        signal.signal(signal.SIGTERM, self._shutdown_handler)
        signal.signal(signal.SIGINT, self._shutdown_handler)
        # signal.signal(signal.SIGKILL, self._shutdown_handler)
        if hasattr(signal, 'SIGBREAK'):  # windows
            signal.signal(signal.SIGBREAK, self._shutdown_handler)


def main_demo(delay):
    def worker(tasks):
        if not tasks:
            print('aha, no job')
        if random.random() < 0.2:
            raise Exception('Not stable, random exception')
        print(sum(tasks))

    runner = TasksTimerRunner(tasks_handler=worker)
    for i in range(20):
        if runner.is_closing():
            return
        runner.add_task(i)
        _print2('task', i, 'was added')
        time.sleep(random.random() * delay)


if __name__ == '__main__':
    main_demo(2.5)
