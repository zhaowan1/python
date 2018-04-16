'''
Created on 2018年4月9日

@author: Administrator
'''
# coding:utf-8
i = 10 #对称数至少有两位数
a = []
b = []
c = []
for h in range(10,100001):
    c.append(h)
while(i <= 100000):
    j = str(i)
    k = len(j) // 2
    m = 0
    while(m < k):
        if(j[m]!=j[-m-1]):
            a.append(i)
            break
        m = m + 1
    i = i + 1             
for w in a:
    c.remove(w)
    b = c
for n in b:
    print(n)
