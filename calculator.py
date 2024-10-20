num1=5
num2=2
op = input("add,sub,mul,div:")
result:0

if op== "add":
    result= num1+num2
elif op== "sub":
    result= num1-num2
elif op== "mul":
    result= num1*num2
elif op== "div":
    result= num1/num2
else:
    result=0
print(result)
