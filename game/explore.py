import networkx as nx
import game.place as place
import numpy as np
import time

seed_value = int(time.time())
np.random.seed(seed_value)

class Explore:
    def __init__(self):
        self.current_place = place.Place(
            "My Desk",
            place.PlaceType.WORKSPACE,
            floor=2,
            is_my_desk=True)
        self.map_graph = nx.Graph()
        
        self.reveal_neighbor()

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

        for neighbor_place in neighbor_places:
            self.map_graph.add_edge(
                self.current_place.name,
                neighbor_place.name)
    
    def get_neighbor_places(self):
        return self.map_graph.neighbors(self.current_place.name)

# np.random.choice를 사용하여 표본 n개 뽑기
def sample_places(place_data, n):
    # 현재 장소 유형에 대한 표본과 확률을 가져옴
    samples = place.neighbor_type_table_efficient[place_data.place_type]['samples']
    probabilities = place.neighbor_type_table_efficient[place_data.place_type]['probabilities']
    
    # np.random.choice를 사용하여 n개의 표본 뽑기
    chosen_samples = np.random.choice(samples, n, p=probabilities)
    return chosen_samples
