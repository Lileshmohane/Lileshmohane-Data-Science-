# 
count = 0
while (count<3):
    count+=1
    print("lilesh")
#for iterator_var in sequence:
 #  statements(s)
 #list  
n= 4
for i in range(0,n):
    print(i)
    #listr
print("list  iterator ")
l= ["hellow","lilesh","mohane"]
print(type(l))
for i in l:
    print(i)
    
#tuple 
r=(1,2,3,4)
print(type(r))
for i in r:
    print(i)
#string 
s="lilesh"
print(type(s))# it is a string 
for i in s: 
    print(i)
# dictinary
d=dict()
d['abc']=123
d['xyz']=456
for i in d:
    print("%s %d" %(i,d[i]))

#set 
s1={1,2,3}
print(type(s1))
for i in s1:
    print(i)

#iterate by index sequence 
list = ["lilesh","mohane","hellow"]
for index in range(len(list)):
    print (list[index])
