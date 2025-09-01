# ghadah alhoshan 443200505

name = input(" Enter your name: ")
weight = float(input(" Enter your weight: "))
height = float(input(" Enter your height: "))

height_convert = height / 100
bmi = weight / (height_convert ** 2)
rounded_bmi = round(bmi, 2)

print("your BMI = \n", rounded_bmi)
