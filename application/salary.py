import datetime


def calculate_salary(people_number):
    now = datetime.datetime.now()

    salary_rate = int(input('Введите ставку: '))
    print(now)
    salary = (people_number * salary_rate) / people_number

    return salary
