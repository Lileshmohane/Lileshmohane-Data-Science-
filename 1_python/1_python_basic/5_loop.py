a= int(input("enter first number :"))
b= int(input("enter first number :"))
if a>b:
    print("a is greater : ")
else:
    print("b is greater : ")

i=20
if(i==10):
    print("i equl to 10")
elif(i==15):
    print("i equal to 15")
elif(i==20):
    print("i equal to 20")
else:
    print("i  is not present")

num = int(input("enter a number :"))
for i in  range(1,11):
    #print(str(num)+"x"+str(i)+"="+str(i*num))
    # using f string 
    print(f"{num}x{i}={i*num}")
num = int(input("enter a number :"))
i=1
while(i<=11):
    print(f"{num}x{i}={i*num}")
    i+=1
    