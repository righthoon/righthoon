mp = int(input('월급 입력 : '))
yp = 12 * mp

def tax_rate(num):
    if num <= 1200:
        return 0.06
    elif  num <= 4600:
        return 0.15
    elif num <= 8800:
        return 0.24
    elif num <= 15000:
        return 0.35
    elif num <= 30000:
        return 0.38
    elif num <= 50000:
        return 0.4
    else
        return 0.42

ap = yp * (1 - tax_rate(yp))

print('세전 연봉: ', yp, '만원')
print('세후 연봉: ', ap, '만원')
