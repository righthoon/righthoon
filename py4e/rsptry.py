import random
def rsp(my,computer):
    if my==computer:
        print('비겼습니다')
    elif my==0 and computer==2:
        return '당신이 이겼습니다'
    elif my==1 and computer==0:
        return '당신이 이겼습니다'
    elif my==2 and computer==1:
        return '당신이 이겼습니다'
    elif my==2 and computer==0:
        return '당신이 졌습니다'
    elif my==0 and computer==1:
        return '당신이 졌습니다'
    elif my==1 and computer==2:
        return '당신이 졌습니다'
    else:
        return '오류'



my=int(input('가위바위보 '))
computer=my
print("나:",my)
print("컴퓨터:",computer)
rsp(my,computer)
