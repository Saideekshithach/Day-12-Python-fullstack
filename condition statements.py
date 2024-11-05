#conditions
#if
'''a=9
b=12
if a>b:
    print("greater")'''
'''a=9
b=12
if a<b:
    print("greater")'''
'''a=4
b=8
if a<=b:
    print("less")'''
'''a=12
b=14
if b>=a:
    print("true")'''
'''a=5
b=5
if a==b:
    print("equal")'''
'''a=8
b=9
if a!=b:
    print("not equal")'''
    
#if condition by using logical operators
'''a=3
b=6
if a<b and b>a:
    print("true")
'''
'''a=5
b=10
if a<=b and b>=a:
    print("greater")'''

'''a=6
b=12
if a!=b and a==b:
    print("false")'''

'''a=7
b=11
if a<b or a==b:
    print("equal")'''

'''a=15
b=30
if b>a or a!=b:
    print("not equal")'''
'''a=2
b=4
if a<=b or b<=a:
    print("less")'''


#if condition by using identity operators(is)
'''a=10
if type(a) is int:
    print("true")
a=4.5
if type(a) is float:
    print("float")
a="python"
if type(a) is str:
    print("True")
a=True
if type(a) is bool:
    print("True")
a=5+3j
if type(a)is complex:
    print("True")'''
#if condition by using identity operators(is not)
'''a=14
if type(a) is not int:
    print("False")
a=4.5
if type(a) is not float:
    print("True")
a="False"
if type(a) is not bool:
    print("True")'''
#if condition by using membership operators
'''a=[1,2,3,4,5,6]
if 5 in a:
    print(5)
a=[1,2,3,4,5,6]
if 5 not in a:
    print(10)
a=(1,2,3,4,5,6,7)
if 3 in a:
    print(a[2])'''
'''a=int(input("enter a value"))
if a<20:
      print("less")'''
#runtime using relational
"""a=int(input("enter a value"))
b=int(input("enter a value"))
if(a<b):
    print("lower")"""
    
'''#if condition using logical
a=int(input("enter a value"))
b=int(input("enter a value"))
if a<b and a<=b:
      print("true")'''
'''a=int(input("enter a value"))
b=int(input("enter a value"))
if a<b or a>b:
      print("True")'''
#run time using identity operators
a=int(input("enter a value"))
if type(a) is int:
      print("true")
#run time using membership operators
'''a=list(map(int,input().split()))
if 5 in a:
       print("true")'''
'''a=int(input("enter the list of data"))
b=[2,3,4,5,6,7,8]
if a in b:
    print("yes")'''

            
