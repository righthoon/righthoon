#중앙값의 표본이 전체정수인 경우
n=int(input('처음 수: '))
m=int(input('마지막 수: '))
numbers=[i for i in range(n,m+1)]
for i in numbers:
    if i%2==0:
        print(i,'짝수')
    if(i==(n+m)/2 and i%2==0):
        print(i,'중앙값')
