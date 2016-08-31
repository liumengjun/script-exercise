#!/usr/bin/python
# -*- coding:utf-8 -*-
# coding=utf-8
# calculate string distance

def calculateStringDistance(strA, pABegin, pAEnd, strB, pBBegin, pBEnd):
    if pABegin > pAEnd:
        if pBBegin > pBEnd:
            return 0;
        else:
            return pBEnd - pBBegin + 1;
    if pBBegin > pBEnd:
        if pABegin > pAEnd:
            return 0;
        else:
            return pAEnd - pABegin + 1;
    if strA[pABegin] == strB[pBBegin]:
        return calculateStringDistance(strA, pABegin + 1, pAEnd, strB, pBBegin + 1, pBEnd)
    else:
        t1 = calculateStringDistance(strA, pABegin, pAEnd, strB, pBBegin + 1, pBEnd)
        t2 = calculateStringDistance(strA, pABegin + 1, pAEnd, strB, pBBegin, pBEnd)
        t3 = calculateStringDistance(strA, pABegin + 1, pAEnd, strB, pBBegin + 1, pBEnd)
        return min(t1,t2,t3) + 1

if __name__ == "__main__":
    import sys
    # print(sys.argv)
    if len(sys.argv) != 3:
        print('need two string')
        quit(0)
    strA = sys.argv[1]
    strB = sys.argv[2]
    print(calculateStringDistance(strA, 0, len(strA)-1, strB, 0, len(strB)-1))
