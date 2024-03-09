from enum import Enum
from game.data.dataType import StatusType
import game.idGenerator as idGenerator

idGenerator = idGenerator.IDGenerator()

class EventManager:
    def __init__(self):
        self.place_event_table = {}

    def add_event(self, place_id, event):
        self.place_event_table[place_id] = event

    def has_event(self, place_id):
        return place_id in self.place_event_table
    
    def get_event(self, place_id):
        return self.place_event_table[place_id]
    
    def remove_event(self, place_id):
        del self.place_event_table[place_id]
    
class Event:
    def __init__(self, event_name, root_sub_event_id, sub_events):
        self.event_id = idGenerator.get_next_id()
        self.event_name = event_name
        self.root_sub_event_id = root_sub_event_id
        self.sub_events = sub_events
    
    def get_sub_event(self, sub_event_id):
        return self.sub_events[sub_event_id]

class SubEvent:
    def __init__(self, sub_event_id):
        self.sub_event_id = sub_event_id

class Dialogue(SubEvent):
    def __init__(self, sub_event_id, dialogue, next):
        super().__init__(sub_event_id)
        self.dialogue = dialogue
        self.next_sub_event_id = next

class Choice(SubEvent):
    def __init__(self, sub_event_id, choicesMap):
        super().__init__(sub_event_id)
        self.choicesMap = choicesMap
    
class ChangeStatus(SubEvent):
    def __init__(self, sub_event_id, status_type, amount, next):
        super().__init__(sub_event_id)
        self.status_type = status_type
        self.amount = amount
        self.next_sub_event_id = next

class EndEvent(SubEvent):
    def __init__(self, sub_event_id):
        super().__init__(sub_event_id)

class PresetEventType(Enum):
    CHEESE_GATEAU = 1

preset_event_table = {
    PresetEventType.CHEESE_GATEAU: Event(
        "황치즈 갸또", 0,
        {
            0: Dialogue(0, "이런! 황치즈 갸또가 나타났다. 먹어도 될까?", next=1),
            1: Choice(1, {"먹자.": 2, "사내 메신저를 확인한다.": 7, "무시한다.": 9}),
            2: Dialogue(2, "맛있는 황치즈 갸또를 먹었다.", next=3),
            3: ChangeStatus(3, StatusType.SAN, amount=10, next=4),
            4: Dialogue(4, "피로가 싹 가셨다. 정신력이 10 회복되었다.", next=5),
            5: Dialogue(5, "이제 황치즈 갸또는 없어졌다.", next=6),
            6: EndEvent(6),
            7: Dialogue(7, "딱히 먹으라는 이야기는 없는 것 같다...", next=8),
            8: Choice(8, {"먹자.": 2, "무시한다.": 9}),
            9: Dialogue(9, "분명 주인이 있는 갸또일거야... 먹지 말자.", next=6),
        }
    )
}
