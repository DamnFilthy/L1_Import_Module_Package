from L1_Import_Module_Package.application.salary import *
from L1_Import_Module_Package.application.db.people import *

if __name__ == '__main__':
    people_num = get_employees()
    salary = calculate_salary(people_num)

    print(f'Зарплата каждого сотрудника составляет: {salary}, всего сотрудников: {people_num}')
