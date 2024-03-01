from enum import Enum

class Place:
    def __init__(self, name, description, floor):
        self.name = name
        self.description = description
        self.floor = floor

# 장소 Enum 데이터
class PlaceType(Enum):
    OFFICE_2F_WORKSPACE = 1
    OFFICE_2F_CANTEEN = 2
    OFFICE_2F_RESTROOM = 3

place_data = {
    PlaceType.OFFICE_2F_WORKSPACE: Place(
        "사무실 업무 공간", 
        "평범한 업무 공간이다. 여러 사람들이 열심히 업무를 하고 있다.",
        floor=2),
    PlaceType.OFFICE_2F_CANTEEN: Place(
        "사무실 1층 탕비실", 
        "물을 마시거나 냉장고를 이용할 수 있는 공간. 가끔 맛있는 음식이 스폰되곤 한다.",
        floor=2),
    PlaceType.OFFICE_2F_RESTROOM: Place(
        "사무실 1층 화장실", 
        "화장실이다. 냄새가 나는 것 같다.",
        floor=2)    
}

