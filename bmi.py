# calculate body mass in squared metres
# weight 65
# height 180
# bmi 20.06


weight = float(input("weight in kg "))
height = float(input("height in cm "))
# bmi = weight / height 
# bmi - kg / m2 

heightsquare  = (height * height) 
# to calulate heightsqaure multiply height by height
bmi = round(weight / heightsquare, 6 ) 
# bmi is weight multiplied by heightsquared
bmi2 = bmi * 10000
# bmi2 = to round up the BMI 

print("Your BMI is", bmi2 )














