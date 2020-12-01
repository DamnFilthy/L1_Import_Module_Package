import datetime


def get_employees():
    now = datetime.datetime.now()

    people_number = int(input('Введите количество сотрудников: '))
    print(now)

    return people_number
