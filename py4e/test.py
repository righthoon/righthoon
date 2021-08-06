age = int(input('나이를 입력하세요. : '))
pay = input('지불유형을 선택하세요. (현금/카드) : ')
def bus_fare(age, pay):
    if pay == '카드':
        if age<8 :
            return '무료'
        elif age<14:
            return 450
        elif age<20:
            return 720
        elif age<75:
            return 1200
        elif 75<=age:
            return '무료'
    elif pay == '현금':
        if age<8:
            return '무료'
        elif age<14:
            return 450
        elif age<20:
            return 1000
        elif age<75:
            return 1300
        elif 75<=age:
            return '무료'
print('나이 : ', age, '세')
print('지불유형 : ', pay)
if bus_fare(age, pay)=='무료':
    print('버스요금 : ', bus_fare(age, pay))
else:
    print('버스요금 : ', bus_fare(age, pay), '원')
