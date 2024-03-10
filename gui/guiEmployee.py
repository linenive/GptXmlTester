import tkinter as tk

class EmployeeWindow():
    def __init__(self, employee):
        self.employee = employee
        self.name = tk.StringVar()
        self.salary = tk.StringVar()
        self.rank = tk.StringVar()
        self.job_group = tk.StringVar()

    def create_new_window(self, event_root):
        new_window = tk.Toplevel(event_root)
        new_window.title("직원 정보")
        new_window.geometry("300x500")  # 창 크기 설정
        new_window.geometry("+600+200")
        me_header = tk.Label(new_window, text="< 직원 정보 >", font=("Arial", 16))
        me_header.pack()

        self.name.set(f"이름: {self.employee.get_name()}")
        name_label = tk.Label(new_window, textvariable=self.name)
        name_label.pack()

        self.salary.set(f"연봉: {self.employee.get_salary()}")
        salary_label = tk.Label(new_window, textvariable=self.salary)
        salary_label.pack()

        self.rank.set(f"직급: {self.employee.get_rank_name()}")
        rank_label = tk.Label(new_window, textvariable=self.rank)
        rank_label.pack()

        self.job_group.set(f"직군: {self.employee.get_job_group_name()}")
        job_group_label = tk.Label(new_window, textvariable=self.job_group)
        job_group_label.pack()

    def update_var(self):
        self.name.set(f"이름: {self.employee.get_name()}")
        self.salary.set(f"연봉: {self.employee.get_salary()}")
        self.rank.set(f"직급: {self.employee.get_rank_name()}")
        self.job_group.set(f"직군: {self.employee.get_job_group_name()}")
