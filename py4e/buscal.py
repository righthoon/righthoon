age=int(input('나이를 입력하세요 '))
payway=input('지불방법을 알려주세요 ')

def bus_fare(age,payway):
    if payway=='카드':
        if age<8:
            return '무료'
        elif age<14:
            return 450
        elif age<20:
            return 720
        elif age<75:
            return 1200
        else:
            return '무료'
    else:
        if age<8:
            return '무료'
        elif age<14:
            return 450
        elif age<20:
            return 1000
        elif age<75:
            return 1300
        else:
            return '무료'
print("나이:",age)
print("지불방법:",payway)
if(bus_fare(age,payway)=='무료'):
    print("버스요금:",bus_fare(age,payway))
else:
    print("버스요금:",bus_fare(age,payway),'원')
