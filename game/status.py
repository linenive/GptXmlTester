import game.team as team
import game.employee as employee

class Status:
    def __init__(self):
        self.my_team = team.Team('신생 팀')
        self.me = employee.Employee('나', 1000)
        self.add_team(self.me)

    def add_team(self, employee):
        self.my_team.add_employee(employee)

    def __str__(self):
        return f'Status\n{self.my_team.__str__()}'

    def __call__(self):
        print(f'The status {self.status_name} has the following teams:')
        for team in self.teams:
            print(team)
