import tkinter as tk
from tkinter import scrolledtext
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

font_path = os.path.join('fonts', 'MALGUN.TTF') 
font_prop = fm.FontProperties(fname=font_path)

class ExploreWindow():
    def create_new_window(self, current_explore):
        self.new_window = tk.Toplevel()
        self.new_window.title("탐험")
        self.new_window.geometry("600x300")
        self.new_window.geometry("+500+0")

        place_name = tk.Label(
            self.new_window, text=f'{current_explore.current_place.floor}층, {current_explore.current_place.name}')
        place_name.pack()

        self.log_area = scrolledtext.ScrolledText(
            self.new_window, width=160, height=10, state='disabled')
        self.log_area.pack(padx=10, pady=10)

        self.add_log('당신은 의자를 박차고 일어났다... 주위를 둘러보았다.')
        self.add_log(current_explore.current_place.get_place_data().description)
        self.add_log('이제 무엇을 할까?')

        move_button = tk.Button(self.new_window, text='이동하기', command=lambda: self.create_buttons(current_explore))
        move_button.pack()

        self.prepare_move_buttons()

        local_map_header = tk.Label(self.new_window, text='지역 지도')
        local_map_header.pack()
        
        self.draw_graph_on_canvas(
            current_explore, self.new_window)

    def draw_graph_on_canvas(self, current_explore, root):
        # 새로운 matplotlib 그림(Figure) 객체 생성
        fig, self.ax = plt.subplots(figsize=(5, 4))

        # FigureCanvasTkAgg 객체 생성
        self.canvas = FigureCanvasTkAgg(fig, master=root)  # root는 Tkinter의 메인 윈도우

        # Tkinter 캔버스 위젯으로 변환 및 패킹
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.draw_graph(current_explore)

    def draw_graph(self, current_explore):
        self.ax.clear()

        # 노드 위치 결정
        pos = nx.spring_layout(current_explore.map_graph)

        node_colors = ['red' if node == current_explore.current_place.id 
                       else 'grey' if current_explore.is_visited(node) else 'skyblue' 
                       for node in current_explore.map_graph.nodes()]

        # NetworkX 그래프를 그림에 그리기
        nx.draw(
            current_explore.map_graph, 
            pos, ax=self.ax, with_labels=False, node_color=node_colors, edge_color='gray')
        nx.draw_networkx_labels(
            current_explore.map_graph,
            pos,
            current_explore.get_labels(),
            font_size=12,
            font_family=font_prop.get_name())

        self.canvas.draw()

    def prepare_move_buttons(self):
        self.move_buttons = []
        # 미리 충분한 버튼들을 생성해 둡니다.
        for i in range(8):
            # 버튼 생성
            self.move_buttons.append(tk.Button(
                self.new_window, text="Empty"))

    def add_log(self, log):
        self.log_area.configure(state='normal')
        self.log_area.insert(tk.END, log + '\n')
        self.log_area.see(tk.END)
        self.log_area.configure(state='disabled')

    def create_buttons(self, current_explore):
        neighbors = list(current_explore.get_neighbor_places())
        
        # 기존 버튼 사용
        for i in range(len(neighbors)):
            self.move_buttons[i].configure(
                text=current_explore.get_label(neighbors[i]), 
                command=lambda neighbor_id=neighbors[i]: self.on_click_move_button(
                    current_explore, neighbor_id))
            self.move_buttons[i].place(x=10 + i * 140, y=200)

    def on_click_move_button(self, current_explore, neighbor_id):
        current_explore.move_to(neighbor_id)

        for button in self.move_buttons:
            button.place_forget()
        
        self.draw_graph(current_explore)
