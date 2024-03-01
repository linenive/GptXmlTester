import tkinter as tk
from tkinter import scrolledtext
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def draw_graph_on_canvas(graph, root):
    # 새로운 matplotlib 그림(Figure) 객체 생성
    fig, ax = plt.subplots(figsize=(5, 4))
    
    # NetworkX 그래프를 그림에 그리기
    nx.draw(graph, ax=ax, with_labels=True, node_color='skyblue', edge_color='gray')
    
    # FigureCanvasTkAgg 객체 생성
    canvas = FigureCanvasTkAgg(fig, master=root)  # root는 Tkinter의 메인 윈도우
    
    # Tkinter 캔버스 위젯으로 변환 및 패킹
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # 캔버스에 그래프 그리기
    canvas.draw()

class ExploreWindow():
    def create_new_window(self, current_place, places):
        new_window = tk.Toplevel()
        new_window.title("탐험")
        new_window.geometry("600x300")

        place_name = tk.Label(
            new_window, text=f'{current_place.floor}층, {current_place.name}')
        place_name.pack()

        self.log_area = scrolledtext.ScrolledText(
            new_window, width=160, height=10, state='disabled')
        self.log_area.pack(padx=10, pady=10)

        self.add_log('당신은 의자를 박차고 일어났다... 주위를 둘러보았다.')
        self.add_log(current_place.description)
        self.add_log('이제 무엇을 할까?')

        local_map_header = tk.Label(new_window, text='지역 지도')
        local_map_header.pack()
        
        draw_graph_on_canvas(places, new_window)

    def add_log(self, log):
        self.log_area.configure(state='normal')
        self.log_area.insert(tk.END, log + '\n')
        self.log_area.see(tk.END)
        self.log_area.configure(state='disabled')
