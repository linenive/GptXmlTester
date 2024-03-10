from game.data.dataType import StatusType
from game.idGenerator import IDGenerator

id_generator = IDGenerator()

class Employee:
    def __init__(self, name, salary, rank, job_group):
        self.id = id_generator.get_next_id()
        self.name = name
        self.salary = salary
        self.max_hp = 100
        self.hp = self.max_hp
        self.max_san = 100
        self.san = self.max_san
        self.state = "정상"
        self.rank = rank
        self.job_group = job_group

    def __str__(self):
        return f"이름: {self.name}, 연봉: {self.salary}만, 체력: {self.hp}/{self.max_hp}, 정신력: {self.san}/{self.max_san}"

    def reduce_san_by_work(self):
        self.san -= 10

        if self.san <= 0:
            self.san = 0
            self.state = "사망"
            print(f"{self.name}이(가) 일을 하다 사망했습니다.")
    
    def change_by_event(self, status_type, amount):
        if status_type == StatusType.HP:
            self.hp += amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            elif self.hp <= 0:
                self.hp = 0
                self.state = "사망"
                print(f"{self.name}이(가) 사망했습니다.")
        elif status_type == StatusType.SAN:
            self.san += amount
            if self.san > self.max_san:
                self.san = self.max_san
            elif self.san <= 0:
                self.san = 0
                self.state = "사망"
                print(f"{self.name}이(가) 사망했습니다.")
