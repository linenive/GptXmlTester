from enum import Enum
import game.idGenerator as idGenerator

idGenerator = idGenerator.IDGenerator()

class Place:
    def __init__(self, name, place_type, floor, is_my_desk = False):
        self.id = idGenerator.get_next_id()
        self.name = name
        self.place_type = place_type
        self.floor = floor
        self.is_my_desk = is_my_desk
        self.is_revealed_neighbor_place = False

    def get_place_data(self):
        return place_data_table[self.place_type]

class PlaceData:
    def __init__(
        self, 
        place_type,
        place_name, 
        description, 
        num_neighbor_mean, 
        num_neighbor_std_dev):
        self.place_type = place_type
        self.name = place_name
        self.description = description
        self.num_neighbor_mean = num_neighbor_mean
        self.num_neighbor_std_dev = num_neighbor_std_dev

# 장소 Enum 데이터
class PlaceType(Enum):
    WORKSPACE = 1
    CANTEEN = 2
    RESTROOM = 3
    MEETING_ROOM = 4

place_data_table = {
    PlaceType.WORKSPACE: PlaceData(
        PlaceType.WORKSPACE,
        "업무 공간", 
        "평범한 업무 공간이다. 여러 사람들이 열심히 업무를 하고 있다.",
        num_neighbor_mean=4,
        num_neighbor_std_dev=1),
    PlaceType.CANTEEN: PlaceData(
        PlaceType.CANTEEN,
        "탕비실", 
        "물을 마시거나 냉장고를 이용할 수 있는 공간. 가끔 맛있는 음식이 스폰되곤 한다.",
        num_neighbor_mean=3,
        num_neighbor_std_dev=1),
    PlaceType.RESTROOM: PlaceData(
        PlaceType.RESTROOM,
        "화장실", 
        "화장실이다. 냄새가 나는 것 같다.",
        num_neighbor_mean=2,
        num_neighbor_std_dev=1),
    PlaceType.MEETING_ROOM: PlaceData(
        PlaceType.MEETING_ROOM,
        "회의실", 
        "회의를 할 수 있는 공간이다. 안이 잘 들여다보이기 때문에 몰래 무언가를 하기는 힘들 것 같다.",
        num_neighbor_mean=3,
        num_neighbor_std_dev=1),
}

neighbor_type_table_efficient = {
    PlaceType.WORKSPACE: {
        'samples': [PlaceType.WORKSPACE, PlaceType.CANTEEN, PlaceType.RESTROOM, PlaceType.MEETING_ROOM],
        'probabilities': [0.6, 0.1, 0.1, 0.2]
    },
    PlaceType.CANTEEN: {
        'samples': [PlaceType.WORKSPACE, PlaceType.RESTROOM, PlaceType.MEETING_ROOM],
        'probabilities': [0.4, 0.2, 0.4]
    },
    PlaceType.RESTROOM: {
        'samples': [PlaceType.WORKSPACE, PlaceType.CANTEEN, PlaceType.MEETING_ROOM],
        'probabilities': [0.6, 0.1, 0.3]
    },
    PlaceType.MEETING_ROOM: {
        'samples': [PlaceType.WORKSPACE, PlaceType.CANTEEN, PlaceType.RESTROOM],
        'probabilities': [0.3, 0.3, 0.4]
    },
}
