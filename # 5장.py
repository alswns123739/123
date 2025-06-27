# 5장

# 반복문
# 반복문이란?
# 반복문은 특정한 작업을 여러 번 반복할 때 사용하는 문법입니다.
# for문의 반복문과 while문의 반복문

# for문
# 지정된 횟수에 따라 반복

# "정해진 횟수만큼 ~을 반복 실행하라" 라는 의미
# fot문의 첫 줄 맨끝에는 콜론(:)이 있어야 함
# for문 안의 코드는 들여쓰기를 해야 함

# 형태
for 변수 in 리스트: # 콜론주의
    반복 실행 코드

# OR

for 변수 in range(): # in은 range()함수가 만든 값에서 하나씩 꺼내 변수에 대입(어디에서 값을 꺼낼지 지정하는 역할)
    반복 실행 코드

# 리스트
# 다양한 자료형의 데이터를 순서대로 저장하는 자료구조의 한 종류
# 인덱스(index)로 번호를 사용하여 리스트의 요소에 접근할 수 있음
# 대괄호[] 안에 각 콤마(,)로 구분
# 저장된 값의 순서는 유지/ 추가 or 변경 or 삭제 가능
# 형태
리스트 = [요소1, 요소2, 요소3, ...]
a = [1,'apple', 3.5]
# 리스트a[0] a[1]    a[2]
 
# 리스트 활용된 for문
# 리스트의 값을 순서대로 출력 가능
for 변수 in 리스트: 
    print(변수)

# 리스트 출력
for i in [1,2,3]:
    print(i)

a = [4,5,6]
for i in a:
    print(i)

# range() 함수
# 변수에 0부터 range() 함수의 인자 -1까지의 정수를 대입
# range() 함수는 일정범위의 연속된 정수를 생성

# 형태
for 변수 in range(숫자):
    반복 실행 코드

# range(시작, 끝, 변화량) 함수
# 시작부터 끝 미만의 범위에서, 변화량만큼 증가 or 감소
# range(숫자1): '0부터 숫자-1까지 1씩 중가
# range(숫자1, 숫자2): '숫자1부터 숫자2-1까지 1씩 증가
# range(숫자1, 숫자2, 숫자3): '숫자1'부터 '숫자2-1'까지 '숫자3'만큼 증가 or 감소

#example
for i in range(5): #0부터 4까지 1씩 증가하며 5번 반복
 print("Codle") #코들 5번 출력
print()

for i in range(5,10):      # 5부터 9까지 1씩 증가하며 5번 반복합니다.
    print(i) # 5~9까지 출력
print()

for i in range(5,10,2):    # 5부터 9까지 2씩 증가하며 3번 반복합니다.
    print(i) # 5, 7, 9 출력
print()

for i in range(4,0,-1):    # 4부터 시작해 1까지 1씩 감소합니다.
    print(i) # 4, 3, 2, 1 출력
print()

# 예제 2
# 1개의 정수(integer) (1 ~ 100)를 입력받아 카운트다운을 출력하는 프로그램을 작성해봅시다. (입력받은 수부터 시작해 0까지 1씩 줄이면서 출력합니다.)
n = int(input())

for n in range(n, -1, -1): 
    print(n) 

# 예제 3
# 1개의 정수(integer) (1 ~ 100)를 입력받아 거꾸로 카운트다운하는 프로그램을 작성해봅시다. (0부터 시작해 입력받은 정수까지 1씩 증가시키며 출력합니다.)
n = int(input())
for n in range(0, n+1, 1): 
# 변화량 1로 0부터 n까지를 순회하는 반복문을 for문과 range함수를 활용하여 작성해보자
    print(n)



# 중첩제어구조
# 선택구조와 반복구조 2개이상 결합하여 사용하는 구조
# for문과 if문을 중첩하여 사용하는 코드

# OR

# for문 안에 또 다른 for문 중첩 작성하는 코드
# for문을 2번 중첩해서 사용하는 것을 이중 for문

# 이중for문 예제
for i in range(4):
    for j in range(3):
        print("i=", i, "j=", j)
    print("===============")

# 예제1 해설
# for i in range(4)와 같이 바깥에 있는 for문과 for j in range(3)과 같이 안 쪽에 있는 for문으로 이루어져 있습니다. 바깥쪽 for문이 실행되어 데이터 하나를 i에 저장하면, 그때 안쪽 for문이 실행됩니다. 안쪽 for문의 반복이 모두 끝날 때까지 i는 처음 저장된 그 값을 유지하고, 안쪽 for문 반복이 전부 끝난 후에야 바깥쪽 for문이 다시 실행되어 i의 값이 바뀝니다.

# i가 0일 때 j가 0에서 2까지 반복되고, 그 다음 i가 1일 때 다시 j가 반복되며, 동일한 방식으로 i가 3, j가 2일 때까지 맨 안쪽 코드는 총 12번 반복 실행되고 코드가 종료됩니다.

# 예제 2, for문과 if문을 함께 사용하여 3의 배수만 더해보기

n =input("정수 입력")
n = int(n)
sum = 0

# 0에서 n까지 순서대로 i에 대입하고, i가 3의 배수일 때에만 sum에 더해주는 반복문입니다. 
for i in range(n+1):
    if i % 3 == 0:
        sum = sum +i
print(sum)


# 예제3
# 양의 정수 n을 입력받고 * 표시로 세로 길이 n, 가로 길이 n인 사각형을 그려 봅시다. (사각형 내부도 *로 채워지도록 합니다.) 각 별표는 공백으로 구분되어 출력됩니다
n = int(input())  # Get input for the size of the pattern

# Loop for the vertical length
for i in range(n):
    # Loop for the horizontal length
    for j in range(n):
        print("*", end=' ')  # Print '*' without going to the next line
    print()  # Move to the next line after printing n stars

