#get 3 inputs (amount of investment per year, % of profit per year, amount of year to invest)

from input_utils import input_int

annual_invest = input_int("How much will you invest per year: ")
annual_interest_rate = input_int("How much is the annual profit(%): ")  
simulation_years = input_int("How many years?: ")

def calculate_dca(amount, rate, years):
    total = 0
    for i in range(years):
        total += amount
        total += total*rate/100

    return total

print("You will have ", calculate_dca(annual_invest, annual_interest_rate, simulation_years))