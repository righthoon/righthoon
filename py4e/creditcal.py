name=input('이름을 입력해주세요')
score=int(input('점수를 입력해주세요'))

def grader(name,score):
    print('이름:',name)
    print('점수:',score)
    if(score<60):
        credit=F
        print('학점:',credit)
    elif(score<64):
        credit='D'
        print('학점:',credit)
    elif(score<69):
        credit='D+'
        print('학점:',credit)
    elif(score<74):
        credit='C'
        print('학점:',credit)
    elif(score<79):
        credit='C+'
        print('학점:',credit)
    elif(score<84):
        credit='B'
        print('학점:',credit)
    elif(score<89):
        credit='B+'
        print('학점:',credit)
    elif(score<94):
        credit='A'
        print('학점:',credit)
    elif(score<=100):
        credit='A+'
        print('학점:',credit)

grader(name,score)
