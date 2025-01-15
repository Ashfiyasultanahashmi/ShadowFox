#1. Write a program to determine the BMI Category based on user input. Ask the user to: Enter height in meters, Enter weight in kilograms Calculate BMI using the formula: BMI = weight / (height)**2
def bmi_category():
    height=float(input("Enter the height in meters:")) #Input the height from user
    weight=float(input("Enter the weight in kilograms:")) #Input the weight from user
    bmi=weight/(height**2)
    if bmi >= 30:
        category = "Obesity"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    else:
        category = "Underweight"

    print(f"BMI Category: {category}")
    
bmi_category()
