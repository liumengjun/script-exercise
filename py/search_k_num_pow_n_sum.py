"""
欧拉猜想
莱昂哈德·欧拉于1769年提出的数论猜想，
断言n>2时，n-1个正整数的n次幂之和不可能等于另一个正整数的n次幂，
但该猜想已被反例推翻。


27^5 + 84^5 + 110^5 + 133^5 = 144^5    (1966年，美国数学家L. J. Lander和T. R. Parkin)

2682440^4 + 15365639^4 + 18796760^4 = 20615673^4    (1988年，哈佛大学的Noam Elkies, n=4时方程存在无穷多个整数解)

95800^4 + 217519^4 + 414560^4 = 422481^4    (Roger Frye找到该方程的最小整数解)


尝试寻找最小k值，使得
    A1^n + A2^n + A3^n + ... + Ak^n = B^n

--------------------------------------
程序设计
通用的方法`searchKNumPowNSum()`, 不如专门设计的方法速度快(`search4p5to1p5`, `search3p4to1p4`)。
但是执行复杂度在`N`的`k`次方, `N`在`1000`上时就很慢, `10000`以上就几乎不动。
多线程版本`searchKNumPowNSum_mp()`, 对比专门设计的方法竟然性能几乎没有提升, 对比`searchKNumPowNSum`提升也不明显, 也许更多CPU(>4)的机器上会有不一样的表现。
    多线程调度需要`数组 copy 传值`, 也许单纯`math.pow(S,1/n)`计算很快, 比内存传输一组数都快;
    而且, 甚至线程子任务内调用`log.debug`(尽管只是判断没有输出)都影响速度。
还属提前计算好`Ai**n`的方法`calc_range_power_n`带来的性能提升明显, 这样循环内只作`sum`和`sum^(1/n)`就可以了。
"""


import math
import logging
import os
import time
from concurrent.futures import ThreadPoolExecutor
from config import timing, log_config
from commons import ThreadSafeCounter

log_config(__file__, log_level=logging.INFO)


@timing(pattern="方法%s运行耗时%.2f秒")
def search4p5to1p5(N=200, start=1):
    """
    寻找 a^5 + b^5 + c^5 + d^5 = e^5
    """
    found = False
    Apn = calc_range_power_n(start, N, 5)
    for a in range(start, N):
        logging.info("progress %d of %d~%d: %.2f%%" %
                     (a, start, N, (a-start)*100/(N-start+1),))
        if found:
            break
        for b in range(a, N):
            if found:
                break
            for c in range(b, N):
                if found:
                    break
                for d in range(c, N):
                    sumM = Apn[a-start]+Apn[b-start]+Apn[c-start]+Apn[d-start]
                    tmpE = math.pow(sumM, 1/5)
                    if int(tmpE)**5 == sumM:
                        logging.info("%d^5 + %d^5 + %d^5 + %d^5 = %d^5" %
                                     (a, b, c, d, tmpE))
                        found = True
                        break


def calc_range_power_n(fo, to, n):
    cnt = to-fo+1
    logging.info('calc [%d, %d] power values to array, count: %d.',
                 fo, to, cnt)
    Apn = [0]*cnt  # 提前计算好Ai**n
    for ai in range(fo, to+1):
        Apn[ai-fo] = ai**n
    logging.debug(Apn)
    return Apn


@timing(pattern="方法%s运行耗时%.2f秒")
def search3p4to1p4(N=200, start=1):
    """
    寻找 a^4 + b^4 + c^4 = d^4
    """
    found = False
    Apn = calc_range_power_n(start, N, 4)
    for a in range(start, N):
        logging.info("progress %d of %d~%d: %.2f%%" %
                     (a, start, N, (a-start)*100/(N-start+1),))
        if found:
            break
        for b in range(a, N):
            if found:
                break
            for c in range(b, N):
                sumM = Apn[a-start]+Apn[b-start]+Apn[c-start]
                tmpD = math.pow(sumM, 1/4)
                if int(tmpD)**4 == sumM:
                    logging.info("%d^4 + %d^4 + %d^4 = %d^4" %
                                 (a, b, c, tmpD))
                    found = True
                    break


def genNextKNum(depth: int, start: int, search_max: int, arr: list):
    """
    生成一组数(生成器方式), 保存到`arr`内, yield arr 本身:
    个数`k=len(arr)`, 每个数可选范围[start, search_max], 时间复杂度 O(N^k);
    有个特殊处理, arr 前面的数不大于后面的数, 所以具体组数是`N*(N-1)*...*(N-k+1)`组。
    """
    for a in range(start, search_max + 1):
        if depth == 1:
            logging.info("progress %d of %d~%d: %.2f%%" %
                         (a, start, search_max, (a-start)*100/(search_max-start+1),))
        arr[depth-1] = a
        if depth == len(arr):
            yield arr
            continue
        # 层次(或下标)加一, 后面的数不小于前面的数
        for ele in genNextKNum(depth+1, a, search_max, arr):
            yield ele


@timing(pattern="方法%s运行耗时%.2f秒")
def searchKNumPowNSum(k, n, search_max=200, search_min=1, found_end=True):
    """
    寻找k个整数的n次幂和恰好是另一个整数的n次幂
      A1^n + A2^n + A3^n + ... + Ak^n = B^n
    """
    logging.info('start to search `%d` numbers in [%d, %d], with `sum of those power %d` = B^%d',
                 k, search_min, search_max, n, n)
    A = [0]*k
    logging.debug(A)
    interval_size = search_max-search_min+1
    Apn = calc_range_power_n(search_min, search_max, n)

    logging.info('search times is almost O(%d^%d) = O(%d)',
                 interval_size, k, interval_size**k)

    found_count = 0
    for arr in genNextKNum(1, search_min, search_max, A):
        # logging.debug(arr)
        # calc
        sumM = 0
        for a in A:
            sumM += Apn[a-search_min]
        tmpE = math.pow(sumM, 1/n).__round__()
        # 此处用`round`, `s^(1/5)`会比实际值偏大还好, 但是`s^(1/3), s^(1/6)`会比实际值偏小
        if tmpE**n == sumM:
            found_count += 1
            _show_found(arr, k, n, tmpE)
            if found_end:
                break
    logging.info("found_count: %d" % found_count)


def _show_found(arr, k, n, tmpE):
    # 输出
    text = "found %d^%d" % (arr[0], n)
    for i in range(1, k):
        text += " + %d^%d" % (arr[i], n)
    text += " = %d^%d" % (tmpE, n)
    logging.info(text)


@timing(pattern="方法%s运行耗时%.2f秒")
def searchKNumPowNSum_mp(k, n, search_max=200, search_min=1, found_end=True, batch_size=10000):
    """
    searchKNumPowNSum 的多线程版本
    寻找k个整数的n次幂和恰好是另一个整数的n次幂
      A1^n + A2^n + A3^n + ... + Ak^n = B^n
    """
    logging.info('start to search `%d` numbers in [%d, %d], with `sum of those power %d` = B^%d, in multi-threads',
                 k, search_min, search_max, n, n)
    A = [0]*k
    logging.debug(A)
    interval_size = search_max-search_min+1
    Apn = calc_range_power_n(search_min, search_max, n)

    logging.info('search times is almost O(%d^%d) = O(%d)',
                 interval_size, k, interval_size**k)

    found_counter = ThreadSafeCounter()

    def _check_power_n_sum(batch_arrays, batch_seq):
        if found_end and found_counter.count:
            return
        for arr in batch_arrays:
            # if found_end and found_counter.count:
            #     break
            # logging.debug('got array: %s', arr)
            sumM = 0
            for a in arr:
                sumM += Apn[a-search_min]
            tmpE = math.pow(sumM, 1/n).__round__()
            # logging.debug('got tmpE: %d, with %s', tmpE, arr)
            # 此处用`round`, `s^(1/5)`会比实际值偏大还好, 但是`s^(1/3), s^(1/6)`会比实际值偏小
            if tmpE**n == sumM:
                found_counter.increment()
                _show_found(arr, k, n, tmpE)
                if found_end:
                    logging.info('found to end at: [%d]', batch_seq)
                    break

    pool_size = os.process_cpu_count() or 2
    logging.info('thread pool size: %d', pool_size)
    pool = ThreadPoolExecutor(max_workers=pool_size)
    # batch_size = 10000  # 默认10000见参数生命，可能需要调整
    batch_arrays = []  # 线程内处理多组，处理单组太浪费
    batch_seq = 0

    for arr in genNextKNum(1, search_min, search_max, A):
        # logging.debug(arr)
        if found_end and found_counter.count:
            break
        batch_arrays.append(list(arr))  # arr 数组 copy 传值, 否则就是A
        if len(batch_arrays) == batch_size:
            # logging.info('to submit batch[%d]', batch_seq)
            pool.submit(_check_power_n_sum, batch_arrays, batch_seq)
            # logging.info('submit batch[%d] ok', batch_seq)
            batch_arrays = []  # 新开一个, 不和前面的冲突
            batch_seq += 1
            if batch_seq % pool_size == 0:
                time.sleep(0.01)
    logging.info('last batch[%d], arrays: %d', batch_seq, len(batch_arrays))
    if batch_arrays:
        pool.submit(_check_power_n_sum, batch_arrays, batch_seq)
    pool.shutdown(wait=True)
    # logging.info('last submit end')

    logging.info("found_count: %d" % found_counter.count)


if __name__ == '__main__':
    search4p5to1p5(150, 20)  # 27^5 + 84^5 + 110^5 + 133^5 = 144^5
    # searchKNumPowNSum(2, 2, 10, 3, False)  # 10以内勾股数, 2组
    # searchKNumPowNSum(2, 2, 100, 3, False)  # 100以内勾股数, 63组
    # searchKNumPowNSum(3, 3, 100, 1, False)  # 100以内三数立方和等立方, 98组
    # searchKNumPowNSum(4, 4, 200, 1, False)  # 200以内四数四次方和等四次方, 无解
    # searchKNumPowNSum(5, 5, 100, 1, False)  # 100以内五数五次方和等五次方, 3组
    # searchKNumPowNSum(6, 6, 100, 1, False)  # 100以内6数6次方和等6次方, 太慢了
    # searchKNumPowNSum(4, 5, 200)  # 和 search4p5to1p5() 效果相同
    searchKNumPowNSum(4, 5, 150, 20)  # 和 search4p5to1p5() 效果相同
    # searchKNumPowNSum(5, 6, 200)  # 太慢了
    # searchKNumPowNSum(3, 4, 200)  # 无解
    # searchKNumPowNSum(3, 4, 2000)  # 太慢了
    # search3p4to1p4(200)
    # search3p4to1p4(2000)
    # search3p4to1p4(10000)  # 太慢了
    # searchKNumPowNSum_mp(2, 2, 10, 3, False)
    # searchKNumPowNSum_mp(2, 2, 100, 3, False)
    # searchKNumPowNSum_mp(3, 3, 100, 1, False)
    # searchKNumPowNSum_mp(4, 4, 200, 1, False)
    # searchKNumPowNSum_mp(5, 5, 100, 1, False)
    # searchKNumPowNSum_mp(6, 6, 100, 1, False)  # 依旧特别慢
    # searchKNumPowNSum_mp(4, 5, 200, batch_size=30000)
    searchKNumPowNSum_mp(4, 5, 150, 20, True, 30000)
    # searchKNumPowNSum_mp(5, 6, 200)  # 依旧特别慢
    # searchKNumPowNSum_mp(3, 4, 200)
    # searchKNumPowNSum_mp(3, 4, 2000)  # 依旧很慢
    pass
