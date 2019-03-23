#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    '''
        在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，
    外部不能访问.确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
        变量名类似__xxx__的，即以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直
    接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
        变量名_xxx的，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你
    看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
        双下划线开头的实例变量其实也能被外部访问？不能直接访问__name是因为Python解释器对外把__name
    变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
    '''
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())
# 强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
print('DO NOT use bart._Student__name:', bart._Student__name)

'''
    表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量
不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart
新增了一个__name变量。不信试试：
'''
bart.__name = 'New Name' # 设置__name变量！
print('bart.get_name() =', bart.__name)
print('bart.get_name() =', bart.get_name())
