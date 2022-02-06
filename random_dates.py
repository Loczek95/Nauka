import random
import datetime

def generate_random_date():
    year = random.randint(1900, 2021)
    month = random.randint(1,12)
    day = random.randint(1,31)
    x = datetime.date(year,month,day)
    return print(x)

generate_random_date()