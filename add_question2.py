#Question 1
ex_list=[1,2,4,5,6,8,23,45,65,78,22,99,73,48,123,675,97,20]
new_list=[i for i in ex_list if i%5==0]
print('old list: ',ex_list)
print('new list: ',new_list)

#Question 2
print('sliced list: ',ex_list[1:7])

#Question 3
x=(1,'hello','best',3,6,9,11,34,'pyhton') #create tupple
print('tuple before insert and append:',x)
#since tuple is imutable update and insert is not possible changing to list then make update and convert back to tupple
x=list(x)
x.insert(1,2) #insert
x.append('cats') #append
x=tuple(x)
print('tuple after insert and append:',x)
sec_last_elm=x[-2]
print('2nd last index in tuple: ',x.index(sec_last_elm)) #print index num of 2nd last element