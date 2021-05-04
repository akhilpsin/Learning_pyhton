def school_dis(x):
    discount=x-(x*15)/100
    return discount

def reg_dis(y):
    r=school_dis(y)
    discount=r-(r*5)/100
    return discount

item={'1.carrot':10,'2.salt':18,'3.pencil box':70,'4.tomato':45,'5.rice':300}
print("Product List:-")
for i in item.keys():
    print(i)

prod=input('please provide your product: ')

product=[i for i in item.keys() if prod in i]
str1=str(product[0])
prod_price=item[str1]

dicount=int(input('please provide your dicount detail: \n 1.Student Discount \n 2.Regular Discount \n '))

if dicount==1:
    print('final amount after student discount: ',school_dis(prod_price))
elif dicount==2:
    print('final amount after regular discount: ',reg_dis(prod_price))
else:
    print('provide valid option')

'''
OutPut:

C:\Users\akhil\Desktop\Inmakes_Learning\venv\Scripts\python.exe C:/Users/akhil/Desktop/Inmakes_Learning/venv/code8.py
Product List:-
1.carrot
2.salt
3.pencil box
4.tomato
5.rice
please provide your product: 3
please provide your dicount detail: 
 1.Student Discount 
 2.Regular Discount 
 2
final amount after regular discount:  56.525

Process finished with exit code 0
'''