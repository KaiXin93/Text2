# encoding=utf-8
__author__ = 'qkx'
from svmutil import *
import jieba

# 读取停词
f_stop = open('stop_words_ch_utf-8.txt')
stop_word = f_stop.read().decode('utf-8').split('\n')
f_stop.close()
stop_word.append(u'\n')
# print(stop_word)

# 去停词和换行符
# 统计词频
def word_count(text, word_docfreq):
    # 分词
    text_words = list(jieba.cut(text, cut_all=False))
    word_freq = {}
    for word in text_words:
        if word != '\r\n' and word not in stop_word:
            freq = word_freq.setdefault(word, 0)
            word_freq[word] = freq + 1

            docfreq = word_docfreq.setdefault(word, 0)
            word_docfreq[word] = docfreq + 1
    return word_freq, word_docfreq


if __name__ == '__main__':

    # N_catg = 10
    N_catg = 2
    # N_essay = 2000
    N_essay = 11
    # catg_word = []
    # 统计字典，类别-->文本-->词-->词频
    catg_text_word_freq = {}
    # 表示词在多少篇文档中出现过
    word_docfreq = {}
    # 类别i
    for i in range(1, N_catg):
        # 每类的样本文章j
        text_word_freq = {}
        # for j in range(10, 2000):
        for j in range(10, N_essay):
            print("i--->" + str(i) + ",j--->" + str(j))
            file_name = "../Reduced/C00000" + str(i) + "/" + str(j) + ".txt"
            f1 = open(file_name)
            text1 = f1.read()
            f1.close()

            word_freq_j, word_docfreq = word_count(text1, word_docfreq)  # 1.词频字典 2.频率大于一定值的词集合

            text_word_freq[j] = word_freq_j

        catg_text_word_freq[i] = text_word_freq

    fc = open("catg_text_word_freq.txt", "w")
    fc.write(str(catg_text_word_freq))
    fc.close()

    fd = open("word_docfreq.txt", "w")
    fd.write(str(word_docfreq))
    fd.close()

    for w in word_docfreq:
        print(w)
    print("维度为" + str(len(word_docfreq.keys())))
