import tkinter as tk
from threading import Thread
import gui.guiStatus as guiStatus
import gui.guiExplore as guiExplore
import game.gameMain as gameMain

def press_start_game():    
    game_thread = Thread(target=gameMain.start_game)
    game_thread.start()

    open_status_window()

    game_start_button.pack_forget()

    status_button.pack()
    work_button.pack()
    explore_button.pack()

    game_info_label.config(text="운명의 주사위는 던져졌다..........")

def on_work_button_click():
    gameMain.on_work()
    statusWindow.update_var(gameMain.current_status)

def open_explore_window():
    exploreWindow.create_new_window(gameMain.current_explore)

def open_status_window():
    statusWindow.create_new_window(gameMain.current_status)

# 메인 윈도우 생성
root = tk.Tk()
root.title("회사원 로그라이크")

# 레이블 위젯 추가
game_info_label = tk.Label(root, text="당신은 방금 막 입사했습니다... 최종 목표는 대표의 자리입니다. 힘내보세요.")
game_info_label.pack()

# 버튼 위젯 추가
game_start_button = tk.Button(root, text="시작", command=press_start_game)
game_start_button.pack()

# 메인 윈도우에 스텟 창 버튼 추가
status_button = tk.Button(
        root,
        text="스테이터스",
        command=open_status_window)

work_button = tk.Button(
        root,
        text="일하기",
        command=on_work_button_click)

explore_button = tk.Button(
        root,
        text="탐험하기",
        command=open_explore_window)

statusWindow = guiStatus.StatusWindow()
exploreWindow = guiExplore.ExploreWindow()

# 메인 이벤트 루프 실행
root.mainloop()