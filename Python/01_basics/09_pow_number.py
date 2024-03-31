from os import *
from sys import *
from collections import *
from math import *

x, pow_num = map(int, input().split())

if(x == 0 and pow_num == 0):
    print(1)
else:
    print(x**pow_num)
