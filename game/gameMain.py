import game.status as status
import game.place as place
import networkx as nx

current_status = status.Status()
current_place = place.place_data[place.PlaceType.OFFICE_2F_WORKSPACE]

def start_game():
    print('게임을 시작합니다.')
            

def on_work():
    current_status.work()
    
places = nx.Graph()
places.add_edge(
    'My Desk',
    'Canteen')
places.add_edge(
    'My Desk',
    'Restroom')
places.add_edge(
    'My Desk',
    'Meeting Room')
