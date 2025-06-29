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



# while문과 for문 비교
# for문과 while문은 비슷한 반복문 구현 가능
# for문은 횟수가 중요할때, while문은 특정조건이 중요할때

for i in range(1, 6, 1):
    print(i)

i = 1
while i < 6:
    print(i)
    i =+ 1

#예제1_구구단을_for문으로_작성해봅시다.

n = int(input("몇 단을 출력해볼까요?"))
for i in range(1,10):
    print(n,"*",i,"=",n*i)  # n은 고정되고, i만 1~9까지 반복하면 됩니다.

#예제2_구구단을_while문으로_작성해봅시다.

n = int(input("몇 단을 출력해볼까요?"))
i= 1
while i<10:
    print(n,"*",i,"=",n*i)
    i +=1  # i를 1~9까지 점점 커지도록 해줍니다.  



# Break문
# 코드 실행중 특정구간에서 정리를 하고 싶을 때 사용
# 반복운에서는 반복문은 중단
# 반복문을 강제로 중단시키는 역할

while True:  # 무한 루프 시작
    # 사용자로부터 정수 입력 받기
    num = int(input("정수를 입력하세요: "))

    # 입력한 수가 3의 배수인지 확인하기
    if num % 3 == 0:
        print(num, "은(는) 3의 배수입니다.")
        break  # 루프 종료
    else:
        print(num, "은(는) 3의 배수가 아닙니다. 다시 시도해주세요.")


# continue문
# 특정조건 이후 실행되는 것을 생략후 반복문의 처음으로 다시 돌아가서 반복문을 실행

total = 0  

# 1부터 100까지 반복
for num in range(1, 101):
    if num % 3 == 0:    # 현재 숫자가 3의 배수인지 확인하기
        continue        # 3의 배수일 경우 아래 코드를 실행하지 않고 다음 숫자로 넘어감    
    total += num        # 3의 배수가 아닌 경우에만 더함

print("1~100까지의 숫자 중 3의 배수를 제외한 합:", total)

# 음수를 제외한 숫자합
total = 0  # 합을 저장할 변수 초기화

# 무한 루프 시작
while True:
    num = int(input("숫자를 입력하세요 (음수는 더하지 않습니다): "))
    
    if num < 0:
        continue    # 여기에 입력해 주세요.
    
    elif num == 0:
        break    # 여기에 입력해 주세요.

    else:
    
        total += num

print(total)


