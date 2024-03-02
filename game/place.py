from enum import Enum

class Place:
    def __init__(self, name, description, floor, is_my_desk = False):
        self.name = name
        self.description = description
        self.floor = floor
        self.is_my_desk = is_my_desk
        self.is_revealed_neighbor_place = False

# 장소 Enum 데이터
class PlaceType(Enum):
    WORKSPACE = 1
    CANTEEN = 2
    RESTROOM = 3
    MEETING_ROOM = 4

place_data = {
    PlaceType.WORKSPACE: Place(
        "사무실 업무 공간", 
        "평범한 업무 공간이다. 여러 사람들이 열심히 업무를 하고 있다.",
        floor=2),
    PlaceType.CANTEEN: Place(
        "사무실 1층 탕비실", 
        "물을 마시거나 냉장고를 이용할 수 있는 공간. 가끔 맛있는 음식이 스폰되곤 한다.",
        floor=2),
    PlaceType.RESTROOM: Place(
        "사무실 1층 화장실", 
        "화장실이다. 냄새가 나는 것 같다.",
        floor=2),
    PlaceType.MEETING_ROOM: Place(
        "사무실 2층 회의실", 
        "회의를 할 수 있는 공간이다. 안이 잘 들여다보이기 때문에 몰래 무언가를 하기는 힘들 것 같다.",
        floor=2),
}

neighbor_type_table = {
    PlaceType.WORKSPACE: [
        {PlaceType.WORKSPACE: 0.6},
        {PlaceType.CANTEEN: 0.1},
        {PlaceType.RESTROOM: 0.1},
        {PlaceType.MEETING_ROOM: 0.2},
    ],
    PlaceType.CANTEEN: [
        {PlaceType.WORKSPACE: 0.4},
        {PlaceType.RESTROOM: 0.2},
        {PlaceType.MEETING_ROOM: 0.4},
    ],
    PlaceType.RESTROOM: [
        {PlaceType.WORKSPACE: 0.6},
        {PlaceType.CANTEEN: 0.1},
        {PlaceType.MEETING_ROOM: 0.3},
    ],
    PlaceType.MEETING_ROOM: [
        {PlaceType.WORKSPACE: 0.3},
        {PlaceType.CANTEEN: 0.3},
        {PlaceType.RESTROOM: 0.4},
    ],
}
