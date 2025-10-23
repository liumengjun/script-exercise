from concurrent.futures import ProcessPoolExecutor

process_pool = ProcessPoolExecutor(max_workers=4)


def _run_pool_task(name):
    with open('logs/mpaf.log', 'a') as f:
        for i in range(10000):
            f.write('name: %s, line: %d\n' % (name, i))


def main_run():
    names = ['apple', 'ball', 'cat']
    for name in names:
        process_pool.submit(_run_pool_task, name)


if __name__ == '__main__':
    main_run()
