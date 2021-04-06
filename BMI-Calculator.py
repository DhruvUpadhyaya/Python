#BMI calculator
#It helps user to calculate their BMI

weight = float(input("Enter your weight in Kg\n"))
height = float(input("Enter your height in m\n"))

bmi = weight/height ** 2
bmi = round(bmi)
print(f"---> BMI = {bmi}")

if bmi <= 18.5:
    print("You are under weight")
elif bmi <= 25:
    print("You have normal weight")
elif bmi <= 30:
    print("You are Overweight")
elif bmi <= 35:
    print("You are Obese")
else:
    print("Clinically Obese") 