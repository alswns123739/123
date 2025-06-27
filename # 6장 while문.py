# 6장 while문

# while문은 조건식이 참이면 반복, 거짓이면 중단
# 첫번째 줄 맨끝에는 콜론을 반드시
# 내부코드는 반드시 들여쓰기!

# while문을 종료시키기 위한 식
# 초기식, 변화식, 조건식

# 만약 변화식이 없다면 while문이 무한반복

i = 0 #초기식
while i <10: # 조건식
    print("Hello, Codle") #반복 실행 문장
    i +=1 # 변화식

# 무한 반복
# 반복문을 빠져 나오지 못하고 영원히 반복하는 것을 의미
# 변화식을 통해 조건식에 들어가는 변수에 변화가 생기고, 그로 인해 조건식의 결과로 거짓이 나올 수 있어야 무한 반복에 빠지지 않습니다

i = 0  
while i < 10:
    print("Hello, Codle") # 무한 반복 문장
                # 변화식 없음

#예제1_while문을_활용하여_팩토리얼을_계산해봅시다.

n = int(input())
res = 1         # 초기식

while n>0:      # n에서 1까지 반복하는 while문 조건식
    res*=n
    n-=1        # 변화식

print(res)


#예제2_각_자릿수를_더해_출력해봅시다.

n = int(input())
sum = 0            # 초기식

while n!=0:        # n이 0이 아닐 동안만 반복하는 while문 조건식
    sum += n%10    # n을 10으로 나눈 나머지를 sum에 더한다.
    n//=10         # 변화식(n을 10으로 나눈 몫)

print(sum)

#언제까지 더할까?1
#문제
#1개의 정수(integer) ( 0 ~ 1000)를 입력받아 입력받은 정수보다 작은동안 1, 2, 3 ... 을 계속 더하는 프로그램을 작성해봅시다.
#마지막에 더한 정수를 출력합니다.

#입력
#정수 1개가 입력됩니다.

#출력
#자연수를 순서대로 계속 더해 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.

n = int(input())  # Get input from the user 
a = 0
sum = 0

# Use while loop to keep adding to sum until it reaches or exceeds n
while sum < n: #n이 sum보다 크다
    a += 1 #그러면 a에 오른쪽 값을 왼쪽 변수에 더하고 저장
    sum += a

print(a)
