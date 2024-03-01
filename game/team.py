import game.employee

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):
        return f'Team {self.team_name} has {len(self.employees)} employees'

    def __len__(self):
        return len(self.employees)

    def __call__(self):
        print(f'The team {self.team_name} has the following employees:')
        for employee in self.employees:
            print(employee)