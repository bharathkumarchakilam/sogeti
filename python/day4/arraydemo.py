import array;

l1=[]
print("The empty list: ",l1)

l2=[0,1,2,3,4,5]
print("Elements in the list: ",l2)

l3=['a',['b','c']]
print("The nested list: ")

l4=list('spam')
print("list creates by string: ",l4)

l5=list(range(-4,4))
print("list using range: ",l5)

l6=[10,20,30,40,50]
print("element at index: ",l6[1])

l7=[['x'],[10,20,30],['y']]
print("Element in nested list: ",l7[1][0])

l8=[10,20,30,40,50]
print("element at index: ",l8[1:4])

l9=[1,[2,3,4,5],5]
print("the element in l9: ",l9[1])
print("the element at l9[1][3]: ",l9[1][3])
print("the element in list using slicing: ",l9[1][1:3])

print("Summary of the list")
print("list1: ",l1)
print("list2: ",l2)
print("list3: ",l3)
print("list4: ",l4)
print("list5: ",l5)
print("list6: ",l6)
print("list7: ",l7)
print("list8: ",l8)
print("list9: ",l9)
