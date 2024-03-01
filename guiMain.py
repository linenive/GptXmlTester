import tkinter as tk
from threading import Thread
import gui.guiStatus as guiStatus
import game.gameMain as gameMain

def press_start_game():    
    game_thread = Thread(target=gameMain.start_game)
    game_thread.start()

    guiStatus.create_new_window(gameMain.current_status)

# 메인 윈도우 생성
root = tk.Tk()
root.title("회사원 로그라이크")

# 레이블 위젯 추가
label = tk.Label(root, text="당신은 방금 막 입사했습니다... 최종 목표는 대표의 자리입니다. 힘내보세요.")
label.pack()

# 버튼 위젯 추가
button = tk.Button(root, text="시작", command=press_start_game)
button.pack()

# 메인 이벤트 루프 실행
root.mainloop()