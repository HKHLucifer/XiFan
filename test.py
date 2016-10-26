#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#print('100 + 200 =', 100 + 200)
##print('你好！', )
#b = a
#a = 'XYZ'
#print(b)
#s1=72
#s2=85
#r=(s2-s1)/s1*100
#print('小明成绩提高了%.2s%%' % r)

"""
#判读年龄代码块-开始
a = input('请输入年龄') #输入语句基本写法
age = int(a)
print('多少岁',age)             #输出语句基本写法
if age > 18:                    #第一次判断年龄
    print('你是成年人')        #输出第一次判断结果
elif age > 14:                  #第二次判断年龄
    print('你是少年人')        #输出第二次判断结果
else:                          #第三次比对年龄
    print('你是小朋友')        #输出第三次结果
#判读年龄代码块-结束
"""

#评估体重BMI代码块
height = input ('请输入您的身高（M）:')                     #输入数据
weight = input ('请输入您的体重（KG）:')                    #输入数据
height = float(height)            #数据转换为浮点型
weight = float(weight)            #数据转换为浮点型
bmi = weight/(height*height)      #数据计算公式

if bmi > 32:
    print ("您的BMI指数为：", '%.2f' %bmi, '严重肥胖')    #%.2f为输出结果保留小数点2位精度
elif 28 < bmi <= 32:
    print ("您的BMI指数为：", '%.2f' %bmi, '肥胖')
elif 25 < bmi <= 28:
    print ("您的BMI指数为：", '%.2f' %bmi, "过重")
elif 18.5 < bmi <= 25:
    print ("您的BMI指数为：", '%.2f' %bmi, "正常")
else:
    print ("您的BMI指数为：", '%.2f' %bmi, "过轻")