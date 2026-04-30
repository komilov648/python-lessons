# pythonda modullar 
# import math
# print(math.sqrt(16))
# print(math.pi)
# as operator
import math_operators as m
# print(math_operators.PI)
# print(math_operators.addition(5, 7))
print(m.PI)
print(m.addition(5, 7))
# 2. modul ichidan faqat kerakli funksiyani chiqarib olish
from math_operators import addition,  subtraction,PI
print(addition(10, 20))
print(subtraction(10, 20))
print(PI)

from math_operators import *
print(addition(3, 6))

#4.python random modul
import random as r
print(r.random()) # 0.0 dan 1.0 gacha tasodifiy son
print(r.randint(1, 100)) # 1 dan 100 gacha tasodifiy son
print(r.choice(["olma", "anor", "behi", "shaftoli"])) # tasodifiy meva tanlasho;lfghj;lkjhASDFGHJ;LKGFDSAxcv,mmnbvcxz     