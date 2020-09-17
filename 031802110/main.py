
import jieba
import math
import sys
import numpy
import cProfile

#空文本
class NoWordError(Exception):
    def __init__(self):
        print("空文本测个锤子！")

#分词，去除停用词
def wordcut(file):

    #用jieba库分词
    result = []
    words = jieba.cut(file)

    #去除停用词可提高准确度
    stopwords = open('stopword.txt', 'r', encoding='utf-8')
    swords = stopwords.read()
    stopwords.close()

    
    #去除停用词
    for word in words:
        if (word not in swords) and word != '':
            result += word

    return result

#字典保存出现词并编号
def dic(li,un):

    #创建空字典
    wordsdic=dict()

    #字典写入
    i = 0
    for word in un:
        wordsdic[word] = i
        i += 1


    #形成向量
    ve = [0]* len(wordsdic)

    for word in li:
        ve[wordsdic[word]] += 1

    return ve

#求相似度
def sim(ve1,ve2):

    len1=len(ve1)
    len2=len(ve2)
    if len1 < len2:
        len1=len2

    sum=0.0
    den1=0
    den2=0

    for i in range(len1):
        den1 += pow(ve1[i],2)
        den2 += pow(ve2[i],2)
        sum += ve1[i]*ve2[i]

    side1=math.sqrt(den1)
    side2=math.sqrt(den2)
    
    result = float(sum)/(side1*side2)

    return result

def readfile(path):
    txt = []
    with open(path,'r',encoding='utf-8') as f:
        txt = f.read()
    return txt

def unii(list1,list2):
    return set(list1).union(set(list2))
#主程序
if __name__ == '__main__':

    path1 = sys.argv[1]
    path2 = sys.argv[2]
    #命令行参数读入文件
    
    file1 = readfile(path1)
    file2 = readfile(path2)

    #空文本检测
    if file1 == '' or file2 == '':
        raise NoWordError

    #返回两篇文章的分词结果到list1,list2
    list1 = wordcut(file1)
    list2 = wordcut(file2)

    
    #uni是分词的并集
    uni = unii(list1,list2)

    #返回向量
    vector1 = dic(list1,uni)
    vector2 = dic(list2,uni)

    #返回相似度
    result = sim(vector1,vector2)

    output = open(sys.argv[3], 'w', encoding='utf-8')
    output.write(str("%.2f%%" % (result*100)))
    output.close()
    
"""    
    cProfile.run('wordcut(file1)')
    cProfile.run('wordcut(file2)')
    cProfile.run('dic(list1,uni)')
    cProfile.run('dic(list2,uni)')
    cProfile.run('sim(vector1,vector2)')
"""

