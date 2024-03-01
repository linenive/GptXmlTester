import tkinter as tk

class StatusWindow():
    def __init__(self):
        self.my_san = tk.IntVar()
        self.my_state = tk.StringVar()

    def create_new_window(self, status):
        new_window = tk.Toplevel()
        new_window.title("스테이터스")
        new_window.geometry("300x200")  # 창 크기 설정
        me_header = tk.Label(new_window, text="< 내 상태 >", font=("Arial", 16))
        me_header.pack()

        my_name = tk.StringVar()
        my_name.set(status.me.name)
        name_label = tk.Label(new_window, text=f"이름: {my_name.get()}")
        name_label.pack()

        my_salary = tk.IntVar()
        my_salary.set(status.me.salary)
        salary_label = tk.Label(new_window, text=f"연봉: {my_salary.get()}만")
        salary_label.pack()

        my_hp = tk.IntVar()
        my_hp.set(status.me.hp)
        hp_label = tk.Label(new_window, text=f"체력: {my_hp.get()}/{status.me.max_hp}")
        hp_label.pack()

        self.my_san.set(f'정신력: {status.me.san}/{status.me.max_san}')
        san_label = tk.Label(new_window, textvariable=self.my_san)
        san_label.pack()

        self.my_state.set(f'상태: {status.me.state}')
        state_label = tk.Label(new_window, textvariable=self.my_state, font=("Arial", 16), fg="red")
        state_label.pack()
        
        team_header = tk.Label(
            new_window, text="< 내 팀 >", font=("Arial", 16))
        team_header.pack(pady=10)

        team_name = tk.Label(new_window, text=f"팀 이름: {status.my_team.team_name}")
        team_name.pack()

        team_size = tk.Label(new_window, text=f"팀 인원: {len(status.my_team)}")
        team_size.pack()

        tk.Label(new_window, text="팀원 목록").pack()
        employee_list = tk.Label(new_window, text=status.my_team.str_all_members_name()).pack()

    def update_var(self, status):
        self.my_san.set(f'정신력: {status.me.san}/{status.me.max_san}')
        self.my_state.set(f'상태: {status.me.state}')
        

