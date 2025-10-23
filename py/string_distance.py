"""
字符串距离
编辑距离(莱文斯坦距离)
https://yinode.tech/post/201909/编辑距离算法计算两个单词之间的相似度/
https://en.wikipedia.org/wiki/Levenshtein_distance
https://blog.csdn.net/sinat_26811377/article/details/102652547
"""


def Levenshtein_Distance(str1, str2):
    if not str1:
        return len(str2 or '') or 0

    if not str2:
        return len(str1 or '') or 0

    matrix = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost)

    return matrix[len(str1)][len(str2)]


if __name__ == '__main__':
    print(Levenshtein_Distance("abc", "bd"))
    print(Levenshtein_Distance("abc", "abc"))
    print(Levenshtein_Distance("aaa", "abc"))
    print(Levenshtein_Distance("hello", "HELLO"))
