#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# type()
# type()函数返回的是什么类型呢？它返回对应的Class类型

print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
# 一个变量指向函数或者类，也可以用type()判断
print('type(abs) =', type(abs))

import types

# 比较两个变量的type类型是否相同
print('type(\'abc\')==str?', type('abc')==str)

