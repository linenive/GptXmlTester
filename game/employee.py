
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.max_hp = 100
        self.hp = self.max_hp
        self.max_san = 100
        self.san = self.max_san
        self.state = "정상"

    def __str__(self):
        return f"이름: {self.name}, 연봉: {self.salary}만, 체력: {self.hp}/{self.max_hp}, 정신력: {self.san}/{self.max_san}"

    def reduce_san_by_work(self):
        self.san -= 10

        if self.san <= 0:
            self.san = 0
            self.state = "사망"
            print(f"{self.name}이(가) 일을 하다 사망했습니다.")
    