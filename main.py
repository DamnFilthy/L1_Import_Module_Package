from L1_Import_Module_Package.application import salary
from L1_Import_Module_Package.application.db import people

if __name__ == '__main__':
    people_num = people.get_employees()
    salary = salary.calculate_salary(people_num)

    print(f'Зарплата каждого сотрудника составляет: {salary}, всего сотрудников: {people_num}')
