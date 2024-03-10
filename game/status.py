import game.team as team
import game.employee as employee
from game.data.employeeJob import Rank, JobGroup

class Status:
    def __init__(self):
        self.my_team = team.Team('신생 팀')
        self.me = employee.Employee(
            '나', 1000, Rank.STAFF, JobGroup.PROGRAMMING)
        self.add_team(self.me)

    def add_team(self, employee):
        self.my_team.add_employee(employee)

    def work(self):
        if self.me.state == '사망':
            print('사망한 상태에서는 일할 수 없습니다.')
            return
        print(f'일했습니다.')
        self.me.reduce_san_by_work()

    def change_status_event_to_me(self, status_type, amount):
        self.me.change_by_event(status_type, amount)

    def __str__(self):
        return f'Status\n{self.my_team.__str__()}'

    def __call__(self):
        print(f'The status {self.status_name} has the following teams:')
        for team in self.teams:
            print(team)
