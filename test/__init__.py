# coding=utf-8
# 90-100优秀；70-90良好；60-70及格；40-60不及格；40以下差等；输入其他数字，输出：输入错误
score = float(input('分数为：'))
if 90<= score <=100:
    print ('优秀')
elif 70<= score < 90:
    print('良好')
elif 60<= score < 70:
    print('及格')
elif 40<= score < 60:
    print('不及格')
elif 0<=score < 40:
    print('差等')
else:
    print('输入错误啦')