# calculate body mass in squared metres
# weight 65
# height 180
# bmi 20.06


weight = float(input("weight in kg"))
height = float(input("height in cm"))

# bmi = weight / height 
# bmi - kg / m2 

heightsquare  = (height * height) 

bmi = round(weight / heightsquare) 

# x = round('bmi';2,)


print("your bmi is", bmi,) ('Please check you have entered whole numbers\n' 'and decimals where asked.')


















