import networkx as nx
import game.place as place
import numpy as np
import time

seed_value = int(time.time())
np.random.seed(seed_value)

class Explore:
    def __init__(self):
        self.current_place = place.Place(
            "내 자리",
            place.PlaceType.WORKSPACE,
            floor=2,
            is_my_desk=True)
        self.maps = {}
        self.maps[self.current_place.id] = self.current_place
        self.map_graph = nx.Graph()
        
        self.reveal()

    def reveal(self):
        # 주변 지역 밝히기
        if(not self.current_place.is_revealed_neighbor_place):
            self.current_place.is_revealed_neighbor_place = True
            self.reveal_neighbor()
            
    def reveal_neighbor(self):
        place_data = self.current_place.get_place_data()
        num_neighbor = np.random.normal(
            place_data.num_neighbor_mean,
            place_data.num_neighbor_std_dev)

        num_neighbor = int(num_neighbor)
        neighbor_places = sample_places(place_data, num_neighbor)

        for neighbor_place_type in neighbor_places:
            new_place_data = place.place_data_table[neighbor_place_type]
            new_place = place.Place(
                new_place_data.name,
                new_place_data.place_type,
                2,
                False
            )
            self.maps[new_place.id] = new_place
            self.map_graph.add_edge(
                self.current_place.id,
                new_place.id)  
            
    def move_to(self, neighbor_id):
        self.current_place = self.maps[neighbor_id]
        self.reveal()
    
    def get_neighbor_places(self):
        return self.map_graph.neighbors(self.current_place.id)
    
    # 일단 사용하지 않겠다.
    def get_labels_deprecated(self):
        return [self.maps[id].name for id in self.map_graph.nodes if id in self.maps]
    
    def get_labels(self):
        return {map_id: map.name for map_id, map in self.maps.items()}
    
    def get_label(self, map_id):
        return self.maps[map_id].name

# np.random.choice를 사용하여 표본 n개 뽑기
def sample_places(place_data, n):
    # 현재 장소 유형에 대한 표본과 확률을 가져옴
    samples = place.neighbor_type_table_efficient[place_data.place_type]['samples']
    probabilities = place.neighbor_type_table_efficient[place_data.place_type]['probabilities']
    
    # np.random.choice를 사용하여 n개의 표본 뽑기
    chosen_samples = np.random.choice(samples, n, p=probabilities)
    return chosen_samples
