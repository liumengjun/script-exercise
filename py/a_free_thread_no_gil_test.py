#!/usr/bin/env python3t

"""
experimental free-threading build
python 禁用GIL 自由线程模式, 版本3.13, 版本信息中含有"experimental free-threading build"文字
当前版本 3.13.0 in 2024, 默认开启GIL, 使用禁用GIL特别发行版`python3t`(源码编译亦可)
"""

import sys
from datetime import datetime
import threading

ITER_TIMES = 10000000
SIMPLE_VERSION = ".".join(str(s) for s in sys.version_info)


def foo(times: int = ITER_TIMES):
    start_at = datetime.now()
    s = 0
    for i in range(times):
        s = s + 1

    end_at = datetime.now()

    print("    python-{} 线程 {}   执行 foo() 执行耗时 = {} s = {} ".format(
        SIMPLE_VERSION, threading.current_thread().name, end_at - start_at, s
    ))


def main():
    print("程序开始执行")
    # 开 10 个线程
    threads = [threading.Thread(target=foo) for _ in range(10)]

    start_at = datetime.now()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_at = datetime.now()

    print("python-{} 版下 main 函数执行耗时 = {}s ".format(
        SIMPLE_VERSION, end_at - start_at
    ))


if __name__ == "__main__":
    "experimental free-threading build"
    print(sys.version)
    print("支持禁用GIL" if "free-threading" in sys.version else "不支持禁用GIL")
    main()
