import game.status as status
from game.explore import Explore
from game.employeeManager import EmployeeManager
from game.event import EventManager

class GameMain:
    def __init__(self):
        self.current_status = status.Status()
        self.current_explore = Explore(self)
        self.employee_manager = EmployeeManager()
        self.event_manager = EventManager()

    def start_game(self):
        print('게임을 시작합니다.')
        self.current_explore.reveal()
                
    def on_work(self):
        self.current_status.work()
