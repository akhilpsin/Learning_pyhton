#Notes part3 additional questions 
# ------------------------------------------------------------- Question 1
def month():
        list=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']
        i=1
        n=int(input("Please provide a valid month number(01-12): "))
        n=n-1
        if n>=0 and n<13:
                print("Selected month is: ",list[n])
        else:
                print('please select a valid month number')                
# ------------------------------------------------------------- Question 2
def simple_intrest():
        def simp(p,n,r):
                si=p*n*r
                print(si)
        p=float(input('enter Principal: '))
        n=float(input('Time Period of the Loan/deposit in years: '))
        r=float(input('enter Rate of Interest: '))
        simp(p,n,r)
# ------------------------------------------------------------- Question 3
def while_fun():
        i=19
        while i<25:
                i=i+1
                if i==22:
                        continue
                print(i)
# ------------------------------------------------------------- Question 4               
def break_fun():
        for i in range(20,30):
                i=i+1
                if i==28:
                        break
                print(i)
#-- Main ----
j=1
while j==1:
        print('1.provide a number to see corresponding Month.\n2.find simple intrest.\n3.exclude 22.\n4.exclude 28.\n')
        op=int(input('please provide question number to view the output: '))
        if op==1:
                print
                month()
        elif op==2:
                simple_intrest()
        elif op==3:
                while_fun()
        elif op==4:
                break_fun()
        else :
                print('Plese provide a valid question number')
        print('\n')
        j=int(input('would you like to continue (yes=1/no=0): '))
        print('\n')

print('thank you')
