import unittest
from BeautifulReport import BeautifulReport
import main


class TestFunction(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("开始测试")

    @classmethod
    def tearDown(self):
        print("测试结束")

    def text_orig(self):
        print("正在读取orig.txt")
        file1 = main.readfile(r'sim_0.8\orig.txt')
        file2 = main.readfile(r'sim_0.8\orig.txt')
        list1 = main.wordcut(file1)
        list2 = main.wordcut(file2)
        degree = main.sim((main.dic(list1,main.unii(list1,list2))), main.dic(list2,main.unii(list1,list2)))
        print('相似度为%.2f' % degree)

    def text_add(self):
        print("正在读取orig_0.8_add.txt")
        file1 = main.readfile(r'sim_0.8\orig.txt')
        file2 = main.readfile(r'sim_0.8\orig_0.8_add.txt')
        list1 = main.wordcut(file1)
        list2 = main.wordcut(file2)
        degree = main.sim((main.dic(list1,main.unii(list1,list2))), main.dic(list2,main.unii(list1,list2)))
        print('相似度为%.2f' % degree)

    def text_del(self):
        print("正在读取orig_0.8_del.txt")
        file1 = main.readfile(r'sim_0.8\orig.txt')
        file2 = main.readfile(r'sim_0.8\orig_0.8_del.txt')
        list1 = main.wordcut(file1)
        list2 = main.wordcut(file2)
        degree = main.sim((main.dic(list1,main.unii(list1,list2))), main.dic(list2,main.unii(list1,list2)))
        print('相似度为%.2f' % degree)

    def text_dis_1(self):
        print("正在读取orig_0.8_dis_1.txt")
        file1 = main.readfile(r'sim_0.8\orig.txt')
        file2 = main.readfile(r'sim_0.8\orig_0.8_dis_1.txt')
        list1 = main.wordcut(file1)
        list2 = main.wordcut(file2)
        degree = main.sim((main.dic(list1,main.unii(list1,list2))), main.dic(list2,main.unii(list1,list2)))
        print('相似度为%.2f' % degree)

    def text_dis_3(self):
        print("正在读取orig_0.8_dis_3.txt")
        file1 = main.readfile(r'sim_0.8\orig.txt')
        file2 = main.readfile(r'sim_0.8\orig_0.8_dis_3.txt')
        list1 = main.wordcut(file1)
        list2 = main.wordcut(file2)
        degree = main.sim((main.dic(list1,main.unii(list1,list2))), main.dic(list2,main.unii(list1,list2)))
        print('相似度为%.2f' % degree)

    def text_dis_7(self):
        print("正在读取orig_0.8_dis_7.txt")
        file1 = main.readfile(r'sim_0.8\orig.txt')
        file2 = main.readfile(r'sim_0.8\orig_0.8_dis_7.txt')
        list1 = main.wordcut(file1)
        list2 = main.wordcut(file2)
        degree = main.sim((main.dic(list1,main.unii(list1,list2))), main.dic(list2,main.unii(list1,list2)))
        print('相似度为%.2f' % degree)

    def text_dis_10(self):
        print("正在读取orig_0.8_dis_10.txt")
        file1 = main.readfile(r'sim_0.8\orig.txt')
        file2 = main.readfile(r'sim_0.8\orig_0.8_dis_10.txt')
        list1 = main.wordcut(file1)
        list2 = main.wordcut(file2)
        degree = main.sim((main.dic(list1,main.unii(list1,list2))), main.dic(list2,main.unii(list1,list2)))
        print('相似度为%.2f' % degree)

    def text_dis_15(self):
        print("正在读取orig_0.8_dis_15.txt")
        file1 = main.readfile(r'sim_0.8\orig.txt')
        file2 = main.readfile(r'sim_0.8\orig_0.8_dis_15.txt')
        list1 = main.wordcut(file1)
        list2 = main.wordcut(file2)
        degree = main.sim((main.dic(list1,main.unii(list1,list2))), main.dic(list2,main.unii(list1,list2)))
        print('相似度为%.2f' % degree)

    def text_mix(self):
        print("正在读取orig_0.8_mix.txt")
        file1 = main.readfile(r'sim_0.8\orig.txt')
        file2 = main.readfile(r'sim_0.8\orig_0.8_mix.txt')
        list1 = main.wordcut(file1)
        list2 = main.wordcut(file2)
        degree = main.sim((main.dic(list1,main.unii(list1,list2))), main.dic(list2,main.unii(list1,list2)))
        print('相似度为%.2f' % degree)

    def text_rep(self):
        print("正在读取orig_0.8_rep.txt")
        file1 = main.readfile(r'sim_0.8\orig.txt')
        file2 = main.readfile(r'sim_0.8\orig_0.8_rep.txt')
        list1 = main.wordcut(file1)
        list2 = main.wordcut(file2)
        degree = main.sim((main.dic(list1,main.unii(list1,list2))), main.dic(list2,main.unii(list1,list2)))
        print('相似度为%.2f' % degree)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [
        TestFunction('text_orig'),
        TestFunction('text_add'),
        TestFunction('text_del'),
        TestFunction('text_dis_1'),
        TestFunction('text_dis_3'),
        TestFunction('text_dis_7'),
        TestFunction('text_dis_10'),
        TestFunction('text_dis_15'),
        TestFunction('text_mix'),
        TestFunction('text_rep')
    ]
    suite.addTests(tests)
    BeautifulReport(suite).report(filename='测试报告.html',
                                  description='论文查重报告',
                                  log_path='.')
