my_list=[]
for i in range(5):
    my_list.append(int(input('Enter the number ')))
oddcount=0
evencount=0
print('odd numbers:')
for i in range(5):
    if my_list[i]%2!=0:
        oddcount+=1
        print(my_list[i])
print('Number of odd numbers:',oddcount)
print('Even numbers:')
for i in range(5):
    if my_list[i]%2==0:
        evencount+=1
        print(my_list[i])
print('Number of even numbers:',evencount)
    
    
    
        
