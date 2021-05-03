def bmi_cal(ht,wt):
    return wt/(ht**2)

ht=float(input("please provide height in meters: "))
wt=float(input("please provide weight in Kg: "))

print('BMI: ',bmi_cal(ht,wt))

