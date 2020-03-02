# calculate body mass in squared metres
# weight 65
# height 180
# bmi 20.06


weight = float(input("weight in kg"))
height = float(input("height in cm"))

# bmi = weight / height 
# bmi - kg / m2 

heightsquare  = (height * height) 

bmi = (weight / heightsquare) 

# bmi2 = ( 'bmi * 1000') 


print("your bmi is", bmi )














