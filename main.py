from application import people, salary


class Process:
    p = people.People.get_employees()
    s = salary.Salary.calculate_salary()


if __name__ == '__main__':
    Process