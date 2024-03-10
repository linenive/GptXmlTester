from game.employee import Employee
from game.data.employeeJob import Rank, JobGroup

class EmployeeManager:
    def __init__(self):
        # 나는 추가하지 않는다.
        self.employees = make_preset_employees()

    def add_employee(self, employee):
        self.employees[employee.id] = employee

    def remove_employee(self, employee):
        del self.employees[employee.id]

    def get_employee(self, id):
        return self.employees[id]
    
    def get_employee_table(self):
        return self.employees
    
    def try_assign_desk_someone(self, place_id):
        for employee in self.employees.values():
            if not employee.has_desk():
                employee.set_desk(place_id)
                return employee
            
        print("회사의 모든 사람들이 이미 자리를 가지고 있습니다.")
        return None

def make_preset_employees():
    employees = {}
    weak1 = Employee("신입개발이", 1000, Rank.INTERN, JobGroup.PROGRAMMING)
    weak2 = Employee("김종밥", 1500, Rank.STAFF, JobGroup.ART)
    weak3 = Employee("김밥진", 1500, Rank.STAFF, JobGroup.DESIGN)
    weak4 = Employee("김예지", 2000, Rank.ASSISTANT_MANAGER, JobGroup.SOUND)
    weak5 = Employee("다잘라", 1200, Rank.INTERN, JobGroup.HR)
    weak6 = Employee("다판다", 1000, Rank.INTERN, JobGroup.SALES)
    weak7 = Employee("다잡아", 1000, Rank.INTERN, JobGroup.QA)
    weak8 = Employee("주식이", 1000, Rank.STAFF, JobGroup.FINANCE)
    employees[weak1.id] = weak1
    employees[weak2.id] = weak2
    employees[weak3.id] = weak3
    employees[weak4.id] = weak4
    employees[weak5.id] = weak5
    employees[weak6.id] = weak6
    employees[weak7.id] = weak7
    employees[weak8.id] = weak8

    return employees
