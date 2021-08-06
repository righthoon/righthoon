import random
def change_s(a):
    if a == '가위':
        return 0
    elif a=='바위':
        return 1
    elif a=='보':
        return 2

def change_n(a):
    if a == '0':
        return '가위'
    elif a == '1':
        return '바위'
    elif a=='2':
        return '보'
def change_N(a):
    if a == 0:
        return '가위'
    elif a == 1:
        return '바위'
    elif a==2:
        return '보'
def rsp_advanced(games):
    i=0
    user_win=0
    user_defeat=0

    computer_win=0
    computer_defeat=0

    draw=0#비기는 경우는 컴퓨터와 나 모두 동시에 +1되기 때문
    while i<games:
        print(' ')#문단 띄어쓰기
        print('가위 바위 보:',i+1,'판')
        my=input('나: ')
        computer=random.randint(0,2)
        computer=change_N(computer)
        print('컴퓨터:',computer)
        if(my=='가위'or my=='바위'or my=='보'):
            i=i+1
            if my == computer:
                print('무승부')
                print(' ')#문단 띄어쓰기
                draw=draw+1
            elif (my=='가위' and computer=='바위')or (my=='바위' and computer == '보')or(my=='보' and computer=='가위'):
                print ('컴퓨터 승리')
                print(' ')
                computer_win=computer_win+1
                user_defeat=user_defeat+1
            else:
                print('나 승리')
                print(' ')
                user_win=user_win+1
                computer_defeat=computer_defeat+1
        elif(my=='0' or my=='1' or my=='2'):
            my=change_n(my)
            i=i+1
            if my == computer:
                print('무승부')
                print(' ')
                draw=draw+1
            elif (my=='가위' and computer=='바위')or (my=='바위' and computer == '보')or(my=='보' and computer=='가위'):
                print ('컴퓨터 승리')
                print(' ')
                computer_win=computer_win+1
                user_defeat=user_defeat+1
            else:
                print('나 승리')
                print(' ')
                user_win=user_win+1
                computer_defeat=computer_defeat+1
        else:#그외로 잘못 입력하면 처음으로 돌아간다
            print(' ')#문단 띄어쓰기
            print('다시 입력해주세요')
            continue

    print('나의 전적:',user_win,'승',draw,'무',user_defeat,'패')
    print('컴퓨터의 전적:',computer_win,'승',draw,'무',computer_defeat,'패')


games=int(input('몇 판을 진행하시겠습니까?: '))
rsp_advanced(games)
