'''
Created on 2018年4月9日

@author: Administrator
'''
# coding:utf-8
L=[1,5,8,3,9,0,66,89,47,35]
#range()创建一个整数列表
for i in range(len(L)):
#    flag=False
    for j in range(len(L)-1,i,-1):
        if L[j-1]>L[j]:
            L[j-1],L[j]=L[j],L[j-1] #两个值比较互相交换
#            flag=True
#    if flag==False:
#        break
print (L) 