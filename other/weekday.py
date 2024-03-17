from datetime import datetime, date
from input_utils import input_date
user_input = input_date("Please insert the date (DD/MM/YYYY): ")
print(user_input.strftime("%A"))
