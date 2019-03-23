#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    # __xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

print(Student('Michael'))
