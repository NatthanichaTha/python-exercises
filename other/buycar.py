


DIESEL_PRICE_PER_KM = 0.12
BENZINE_PRICE_PER_KM = 0.13
GPL_PRICE_PER_KM = 0.07
EXPECTED_KM_PER_YEAR = 10000
MAX_CAR_AGE = 30
MAX_CAR_KM = 300000

def compute_car_yearly_cost(instant_cost, expected_future_maintanance_cost, installment_years, installment_cost, curr_car_age, curr_car_km, car_fuel_type):
    car_life_span = min(int((MAX_CAR_KM - curr_car_km)/EXPECTED_KM_PER_YEAR), int(MAX_CAR_AGE - curr_car_age))
    total_cost = instant_cost + expected_future_maintanance_cost + (installment_years * installment_cost)
    if car_fuel_type == "diesel":
        total_cost += DIESEL_PRICE_PER_KM * EXPECTED_KM_PER_YEAR * car_life_span
    elif car_fuel_type == "benzine":
        total_cost += BENZINE_PRICE_PER_KM * EXPECTED_KM_PER_YEAR * car_life_span
    elif car_fuel_type == "gpl":
        total_cost += GPL_PRICE_PER_KM * EXPECTED_KM_PER_YEAR * car_life_span

    return total_cost/car_life_span


file = open("./cars.txt", "r")
car_list = file.readlines()
best_choice = None
min_cost = None
for item in car_list:
    info = item.split(",")
    carname = info[0]
    instant_cost = int(info[1])
    expected_future_maintanance_cost = int(info[2])
    installment_years = int(info[3])
    installment_cost = int(info[4])
    curr_car_age = int(info[5])
    curr_car_km = int(info[6])
    car_fuel_type = info[7]

    yearly_cost = compute_car_yearly_cost(instant_cost, expected_future_maintanance_cost, installment_years, installment_cost, curr_car_age, curr_car_km, car_fuel_type)
    print(carname, compute_car_yearly_cost(instant_cost, expected_future_maintanance_cost, installment_years, installment_cost, curr_car_age, curr_car_km, car_fuel_type))
    if min_cost == None:
        best_choice = carname
        min_cost = yearly_cost
    elif yearly_cost < min_cost:
        best_choice = carname
        min_cost = yearly_cost

print("best choice is", best_choice)