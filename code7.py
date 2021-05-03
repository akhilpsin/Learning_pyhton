list=[]
for i in range(1,101):
    list.append(i)
#list contains 1 to 100

new_list=[i for i in list if i%2!=0]

print(new_list)