# 직삼각형 별(*)찍기 프로젝트

#입력 받은 숫자의 줄만큼 직삼각형 모양의 별(*)을 찍는 프로그램을 만들기

# 프로젝트 흐름
#1. input() 함수를 통해 숫자를 입력 받습니다.
#2. for문을 두 번 사용합니다.
#3. 한 줄 출력하고 줄바꿈되도록 합니다.


#문제
#입력 받은 숫자(정수)의 줄만큼 직삼각형 모양의 별(*)을 찍는 프로그램을 만들어봅시다.
#[Hint] 이중 for문을 사용합니다. 

#입력
#1개의 정수

#출력
#입력 받은 정수의 줄만큼 별(*)이 직삼각형 모양으로 출력됨


# 1. 사용자로부터 입력을 받음
n = int(input("별을 몇 줄까지 찍을까요? "))  # 입력값을 정수로 변환

# 2. 입력받은 줄 수만큼 반복
for i in range(n):
    # 3. 현재 줄 번호(i+1)만큼 별을 찍음
    print("*" * (i + 1))


#i = n, n에 1을 더해 별줄을 만듬