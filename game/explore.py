import networkx as nx
import game.place as place

class Explore:
    def __init__(self):
        self.current_place = place.Place(
            "내 자리",
            place.place_data_table[place.PlaceType.WORKSPACE],
            floor=2,
            is_my_desk=True)
        self.map_graph = nx.Graph()
        self.map_graph.add_edge(
            'My Desk',
            'Canteen')
        self.map_graph.add_edge(
            'My Desk',
            'Restroom')
        self.map_graph.add_edge(
            'My Desk',
            'Meeting Room')

    def reveal():
        # 주변 지역 밝히기
        if(not self.current_place.is_revealed_neighbor_place):
            self.current_place.is_revealed_neighbor_place = True


            for neighbor in place.neighbor_type_table[place.PlaceType.WORKSPACE]:
                for key in neighbor:
                    self.map_graph.add_edge(
                        self.current_place.name,
                        place.place_data[key].name)
