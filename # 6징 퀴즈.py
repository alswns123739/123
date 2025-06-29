# 6징 퀴즈

# while의 설명에 대해 올바르지 않은것은?
# 1. while문은 조건식의 결과가 참이면 내부 실행문을 반복하고, 거짓이면 반복을 중단한다.
# 2. while문의 조건 뒤에 반드시 콜론(:)을 붙여야 한다.
# 3. while문 안에서 실행되는 코드는 반드시 들여쓰기를 해주어야 한다.
# 4. 정해진 횟수를 반복할 때 while문을 사용한다. 

# 2번
# 아래 코드에서 올바르지 않은 것은?
i = 0
while i < 10:
    print("Hello, codle")
    i=+1

# 1.위 코드는 'Hello, Codle'이 11번 출력된다. 
# 2.변화식을 통해 조건식에 들어가는 변수에 변화가 생기고, 그로 인해 조건식의 결과로 거짓이 나올 수 있어야 무한 반복에 빠지지 않는다.
# 3.초기식, 조건식, 변화식은 while문을 종료시키기 위한 식이다. 
# 4.변화식이 없다면, i는 계속 0이기 때문에 while문이 종료하지 않고 무한하게 반복된다.

#4번

#while문을 활용하여 팩토리얼을 구하는 코드입니다. 가에 알맞은 코드를 선택하세요.
n = int(input())
res = 1   
가 = 0

while n>0:
    res*=n
    가

print(res)

#n-=1
#n+=1
#n==1
#n*=1

# 1번: 4번
# while문은 무한 획수를 반복할 때 사용

# 2번: 1번
# i는 조건이 유지되어 무한반복

# 4번: 1번
# n이 1씩 줄이며, res *= n을 반복해야하기 때문





# while문 퀴즈
# 1. 코드를 실행시킨 결과로 알맞은 코드를 작성하시오
i = 0 
while i<10:
    print("Hello, world!")
    i+=1

# 문제2
n = int(input("몇 단을 출력해볼까요?"))
for i in range(1,10):
    print(n,"*",i,"=",n*i) 


n = int(input("몇 단을 출력해볼까요?"))
i= 1
가
    print(n,"*",i,"=",n*i)
    i +=1  # i를 1~9까지 점점 커지도록 해줍니다.  

# 1번 답: 1
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# i가 10미만일땐 입력수에 +1을 출력

# 답: while i> 10: