#insert height, weight, and amount of kg to lose per month
#print dailycaloriesforweightloss
from input_utils import input_int, input_choice

weight = input_int("Your weight(kg): ")
height = input_int("Your height(cm): ")
age = input_int("Your age:" )
gender = input_choice("Your gender(M/F):" , ["M", "F"])
kgpermonth = input_int("How many kilograms you wish to lose per month?: ")

def findTDEE(weight_kg, height_cm, age, gender):
    if gender == "M":
        BMR = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5 
    else:
        BMR = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    TDEE = BMR*1.2
    return TDEE

def find_daily_cal_intake(TDEE, kgpermonth):
    monthly_cal_deficit = kgpermonth * 7700
    suggested_daily_cal_intake = TDEE - (monthly_cal_deficit / 30)
    return suggested_daily_cal_intake

computed_TDEE = findTDEE(weight, height, age, gender)

print(find_daily_cal_intake(computed_TDEE, kgpermonth))




