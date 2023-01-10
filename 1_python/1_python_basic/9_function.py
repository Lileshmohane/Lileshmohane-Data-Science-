# create  a function 
# function with argument 
#def myfunction(a):
 # print("enter  a number: ",a)
  # colling a function 
#  myfunction(5)# print a argument

 
# create  a function 
#def myfunction(state="m p"):
#  print("your  state is :",state)
#colling a function 

#myfunction("gujarat")
#myfunction()


# creating a function  recurtion 
#def factorial(x):
 #   if x == 1:
  #       return 1
   # else:
    # function colling
    # return (x*factorial(x-1))
#num = int(input("enter a number : "))
#print(f" the factiria  of {num} is : ",factorial(num))


# create a function 
#x = lambda a: a+10
#print(x(5))
# creat a function 
# local variable 
#def sum(x,y):
 #   sum  =x+y
 #  return sum
  # print(sum(5,10))
  # choice()
#from random import choice
#l1 = [1,3,4,5,6,7]
#print(choice(l1))
 # cerate a function 
#from random import randint 
#otp = randint (1000,9999)
#print("  yor otp is : ",otp)

# *argus and **kuargus
#def num(*args):
 #   for arg in args:
#       print(arg)
#num('hellow ','how ','are ','you')
def function1(a,b):
      print(" hellow you are in 1",a+b)
def function2(a,b):
      """ this is is a function  which will  calculate two the number """

      average = (a+b)/2
      print(average)
      return average
#v= function1(3, 7)
#print(v)
print(function2.__doc__)
def fact(n):
      if n==1:
        return 1 
      else:
            a= n-1
            b= n*fact(a)
            return b
            #return n*fact(n-1)
print(fact(5))