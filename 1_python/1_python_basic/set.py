my= {1,2,3}
print(my)
set1=set()
print("initialise blank set ")
print(set1)
set1=set("lilesh")
print(set1)
# in set cantain only  uniqe element 
set1=set(["lilesh","hello","lilesh"])
print(set1)
# add element in set
set1={1,2,3}
set1.add(4)
set1.add(5) 
set1.add(6)
print(set1)
# using update method
set1=set([1,2,3,4])
set1.update([10,15])
print(set1)
#accessing a set 
set1 = set(["hello","hii","hello"])
print(set1)
# acess a element using for loop  
for i in set1:
    print(i,end=" ")
 #check  the element using in keyword
print("hello" in set1)
# removing a element using
set1=set([1,2,3,4,5])
print(set1)
set1.remove(1)
set1.remove(2)
# using diskard  method
set1.discard(3) 
print(set1)