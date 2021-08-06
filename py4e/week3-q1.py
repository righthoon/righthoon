def gugudan(number):
    i=1
    print(number,'단')
    while number*i<=50:
        print(number,'X',i,'=',number*i)
        i=i+2

number=int(input('몇 단?:'))
gugudan(number)
