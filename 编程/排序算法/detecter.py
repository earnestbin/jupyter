#搞一个对数器来判断写的排序算法对不对
import random ,operator

 
def swap(arr,a,b):
    #交换函数
    arr[a],arr[b] = arr[b],arr[a]
 
# 对数器
 
def generateRandomArr(size,value):
    #产生一个随机数列长度为size，数字范围为-value~value
    arr = []
    for i in range(size):
        arr.append(int((value+1)*random.random())-int(value*random.random()))
    return arr
 
def rigth_mothod(arr):
    #一个绝对正确的方法
    arr.sort()
    return arr
 
def isRight(times,size,value,func):
    succeed = True
    for i in range(times):
        arr1 = generateRandomArr(size,value)
        arr2 = arr1.copy()
        arr3 = arr1.copy()
        arr1=func(arr1)
        rigth_mothod(arr2)
        if not operator.eq(arr1,arr2):
            succeed = False
            print(arr3)
            break
    print('NICE'if succeed==True else 'WRONG')
