import game.status as status

current_status = status.Status()

def start_game():
    print('게임을 시작합니다.')
    print(current_status)
    current_status.add_team('신입사원')
    print(current_status)    