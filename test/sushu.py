'''
Created on 2018年4月9日

@author: Administrator
'''
# coding:utf-8
# 输入1到100中的素数（使用for循环）
from math import sqrt
result = []
for num in range(2,100): 
    f = True
    for snu in range(2,int(sqrt(num)+1)):
        if num %snu ==0:
            f = False
            break
    if f:
        result.append(num)
#数组列表表示
print(result)

#换行表示结果
'''
for a in result:
    print(a)
'''