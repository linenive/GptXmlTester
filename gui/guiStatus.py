import tkinter as tk

def create_new_window(status):
    new_window = tk.Toplevel()
    new_window.title("스테이터스")
    new_window.geometry("300x200")  # 창 크기 설정
    me_header = tk.Label(new_window, text="< 내 상태 >", font=("Arial", 16))
    me_header.pack()
    
    my_status = tk.Label(new_window, text=status.me.__str__())
    my_status.pack()

    team_header = tk.Label(
        new_window, text="< 내 팀 >", font=("Arial", 16))
    team_header.pack(pady=10)

    team_name = tk.Label(new_window, text=f"팀 이름: {status.my_team.team_name}")
    team_name.pack()

    team_size = tk.Label(new_window, text=f"팀 인원: {len(status.my_team)}")
    team_size.pack()

    tk.Label(new_window, text="팀원 목록").pack()
    employee_list = tk.Label(new_window, text=status.my_team.employees).pack()

    

