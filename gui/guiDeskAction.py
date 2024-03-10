import tkinter as tk

class DeskActionWindow():
    def __init__(self, owner, owner_employee_window, add_log_function):
        self.owner = owner
        self.owner_employee_window = owner_employee_window
        self.add_log_function = add_log_function

    def create_new_window(self, event_root):
        desk_action_window = tk.Toplevel(event_root)
        desk_action_window.title("액션...")
        desk_action_window.geometry("+500+300")
        desk_action_window.geometry("+1000+200")

        see_id_card_button = tk.Button(
            desk_action_window, 
            text="사원증 보기", 
            command=self.on_press_see_id_card)
        see_id_card_button.pack()

        ask_salary_button = tk.Button(
            desk_action_window, 
            text="연봉 물어보기", 
            command=self.on_press_ask_salary)
        ask_salary_button.pack()

        ask_rank_button = tk.Button(
            desk_action_window, 
            text="직급 물어보기", 
            command=self.on_press_ask_rank)
        ask_rank_button.pack()

        ask_job_group_button = tk.Button(
            desk_action_window, 
            text="직군 물어보기", 
            command=self.on_press_ask_job_group)
        ask_job_group_button.pack()

    def on_press_see_id_card(self):
        self.add_log_function("사원증을 슬쩍 보았다... " + \
            f"이름이 {self.owner.name}(이)신듯 하다.")
        self.owner.reveal_name()
        self.owner_employee_window.update_var()

    def on_press_ask_salary(self):
        self.add_log_function("연봉을 물어보았다... ")
        self.add_log_function(f"{self.owner_employee_window.name.get()}: " + \
            "내가 왜 연봉을 알려주어야 하지?!")
    
    def on_press_ask_job_group(self):
        self.add_log_function("직군을 물어보았다... ")
        self.add_log_function(f"{self.owner_employee_window.name.get()}: " + \
            f"저는 {self.owner.get_job_group_name()}입니다.")
        self.owner.reveal_job_group()
        self.owner_employee_window.update_var()

    def on_press_ask_rank(self):
        self.add_log_function("직급을 물어보았다... ")
        self.add_log_function(f"{self.owner_employee_window.name.get()}: " + \
            f"저는 {self.owner.get_rank_name()}입니다. 근데, 왜 물어보시죠...?")
        self.owner.reveal_rank()
        self.owner_employee_window.update_var()
    