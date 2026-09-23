import os
import logging
import sys
import time
from functools import wraps


def _detect_work_dir():
    # print(os.getcwd())
    # print(os.path.expanduser('~'))
    file_dir = os.path.dirname(os.path.realpath(__file__))
    # print(file_dir)
    while len(file_dir) > 1:
        _logs_dir = os.path.join(file_dir, 'logs')
        if os.path.exists(_logs_dir):
            return file_dir
        file_dir = os.path.dirname(file_dir)
        # print(file_dir)
    return os.getcwd()


def log_config(your_file: str, with_console=True, log_level=logging.INFO):
    work_dir = _detect_work_dir()
    if your_file:
        your_file = os.path.basename(your_file)
        if your_file.endswith('.log'):
            log_filename = your_file
        else:
            your_file = your_file.replace('.py', '')
            log_filename = your_file+'.log'
    else:
        log_filename = 'log.log'
    log_filepath = os.path.join(work_dir, 'logs', log_filename)
    print('log_file: %s' % log_filepath)

    _fmt = '%(asctime)s %(filename)s [%(levelname)s] %(message)s'
    logging.basicConfig(level=log_level, filename=log_filepath, format=_fmt)
    # above only file, below add console
    if with_console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.formatter = logging.Formatter(_fmt)
        logging.root.addHandler(console_handler)


def timing(pattern=None):
    # 外层函数：接收参数(如果不包含参数，可直接从中层写起)
    """
    计时: 函数运行计时器
          pattern %%格式字符串, 包含'方法名'和'耗时';
                  为空时默认"Function '{方法名}' executed in {耗时:.3f} seconds"。
    """
    def decorator(func):
        # 中层函数：接收被装饰函数
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()  # 记录开始时间
            result = func(*args, **kwargs)  # 执行被装饰的函数
            end_time = time.time()  # 记录结束时间
            elapsed_time = end_time - start_time  # 计算耗时
            if pattern:
                print(pattern % (func.__name__, elapsed_time))
            else:
                print(
                    f"Function '{func.__name__}' executed in {elapsed_time:.3f} seconds")
            return result  # 返回被装饰函数的执行结果
        return wrapper
    return decorator


if __name__ == '__main__':
    # only test
    # log_config(None)
    # log_config(__file__)
    # log_config('web.log')
    pass
