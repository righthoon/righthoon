import random

def rsp(my, computer):
    if my == computer:
        return '무승부'
    elif (my - computer) == -1 or (my==2 and computer == 0):
        return '컴퓨터 승리'
    else :
        return '나 승리'

def change_a(a):
    if a == '가위':
        return 0
    elif a == '바위':
        return 1
    elif a == '보':
        return 2
def change_n(a):
    if a == 0:
        return '가위'
    elif a == 1:
        return '바위'
    elif a == 2:
        return '보'

my = input('가위 바위 보 : ')
computer = random.randint(0,2)

if my=='0' or my=='1' or my=='2' or my=='가위'or my=='바위'or my=='보':
    try :
        print('나 : ',change_n(int(my)))
    except :
        print('나 : ', my)
    print('컴퓨터 : ', change_n(computer))
    try:
        print(rsp(change_a(my), computer))
    except:
        print(rsp(int(my),computer))
else:
    print("가위,바위,보,0,1,2 중 하나로 입력해주세요")
