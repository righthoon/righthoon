def yearly_payment(monthly_payment):
    before_tax=12*monthly_payment

    if before_tax<=1200:
        after_tax=before_tax*(1-0.06)
    elif before_tax<=4600:
        after_tax=before_tax*(1-0.15)
    elif before_tax<=8800:
        after_tax=before_tax*(1-0.24)
    elif before_tax<=15000:
        after_tax=before_tax*(1-0.35)
    elif before_tax<=30000:
        after_tax=before_tax*(1-0.38)
    elif before_tax<=50000:
        after_tax=before_tax*(1-0.40)
    else:
        after_tax=before_tax*(1-0.42)

    print("세전연봉",before_tax)
    print("세후연봉",after_tax)

monthly_payment=int(input('월급을 입력하세요 '))
yearly_payment(monthly_payment)
