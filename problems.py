#Mesele1 calc
'''print("1.SUM")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
a=int(input("Select operation:"))
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if(a==1):
    print("{}+{}=".format(num1,num2), end="")
    print(num1+num2)
elif(a==2):
    print("{}-{}=".format(num1,num2), end="")
    print(num1-num2)
elif(a==3):
    print("{}*{}=".format(num1,num2), end="")
    print(num1*num2)
elif(a==4):
    print("{}/{}=".format(num1,num2), end="")
    print(num1/num2)
else:
    print("ERROR!")'''

#Mesele1 calc
'''x = input()
if x.find('+') != -1:
    a = x.split('+')
   # print("{}+{}=",end="")
    print(int(a[0].strip()) + int(a[1].strip()))
elif x.find('-') != -1:
    a = x.split('-')
    print(int(a[0].strip()) - int(a[1].strip()))
elif x.find('*') != -1:
    a = x.split('*')
    print(int(a[0].strip()) * int(a[1].strip()))
elif x.find('/') != -1:
    a = x.split('/')
    print(int(a[0].strip()) / int(a[1].strip()))
else:
    print("ERROR")'''

#Mesele2 8 13
'''while(1):
    x=str(input("Enter password:"))
    print("Wrong password!")
    if(len(x)>8 and len(x)<13):
        break '''

#Mesele3 3 cehd
'''i=0
a=input("Password:")
while(i<3):
    x=str(input("Enter password:"))
    if(a==x):
        print("Right password")
        break
    print("Wrong password!")
    i+=1
'''
