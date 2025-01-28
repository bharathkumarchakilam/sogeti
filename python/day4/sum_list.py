list1=[1,2,3,4,5]
sum=0
for i in list1:
    sum+=i
    
print(sum)

number=[int(input(f"enter number {i+1}: "))for i in range(5)]
total=sum(number)
print(total)



    