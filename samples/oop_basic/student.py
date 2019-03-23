#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）
class Student(object):
    # 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
    # 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    #
    # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，
    # 必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    # get_grade方法可以直接在实例变量上调用
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())
