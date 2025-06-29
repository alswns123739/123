# 7장 리스트, 튜플, 딕셔너리

# 리스트
# 리스트: 여러 데이터를 묶어 저장하는 자료구조의 유형
# 리스트는 대괄호 안에 쓰며, 콤마로 구분
# 저장된 값의 순서는 유지, 값의 추가 삭제 변경 자유롭게 가능
# 한자리 자료형, 여러가지 자료형 섞어서 사용가능

# 리스트 출력 방법
# print() 함수로 출력 가능
# print(리스트 입력시 전체 출력)
# 각각의 요소 출력시 인덱스로 접근

# index란?
# 각 요소의 위치를 가르키는 정수값
# 인덱스는 0부터 시작
# list[인덱스 번호]로 접근
# 접근하면 다른값으로 변경 가능
# 연산을 수행 할수 있다.

# 인덱스의 범위를 넘어 접근 시도시 "list index out of range"오류 출력


# 슬라이싱
# 인덱스를 활용하여 리스트의 필요 일부분만 잘라내어 활용하는 코드
# my_list[a:b]는 a에서 b-1까지 잘라냄
# a가 공란: 첫문자부터 b-1까지
# b가 공란: 가장 마지막까지 출력
# a,b에 음수도 가능
# 음수는 우측에서 해당 숫자만큼 딸어진 인덱스 의미

# 1)
#예제1_리스트를_만들고_출력해봅시다.

number_list = [1,2,3]
word_list = ['a','b','c']

print(number_list)
print(word_list)

# 2)
#예제2_여러_자료형을_저장한_리스트_만들어봅시다.

mix_list = [1,2,'codle',56]
print(mix_list)

mix_list[1:-3]

#예제3_mix_list의_요소들을_각각_출력해봅시다.   

print(mix_list[0])
print(mix_list[1])
print(mix_list[2])
print(mix_list[3])

# 4)
#예제4_리스트의_요소를_수정해봅시다.

# mix_list = [1,2,'codle',56]

mix_list[2] = "codle"
print(mix_list)

 # 리스트 압력 받기
 # 순서
 #1. 빈 리스트 생성
 #2. input 함수로 입력 후 새로운 변수 저장
 #3. append 함수로 입력 값을 변수에 추가

 # input 함수로 리스트 입력 받기
 # 여러개의 문자열 데이터 입력 받기
 # inpit().split()함수로 여러개 입력
 # 공백을 기준으로 나눠 리스트 변환

 # 여러개의 정수형 데이터
 # string의 형태로 리스트에 저장
 # int를 저장하려면 map함수도 포함
 # map(함수, 리스트): 주어진 함수를 이스트의 모든 요소 저장
 # map(()은 list로 변환하지 않아 강제 변환 필요

 #예제1_리스트와_관련된_함수를_사용해봅시다.

a = [3, 7, 4, 2, 5, 3]

a.append(8)
print("append 함수 테스트 a값 출력 : " ,a)

a.insert(2,10)
print("insert 함수 테스트 a값 출력 : " ,a)

a.remove(3)
print("remove 함수 테스트 a값 출력 : " ,a)

a.reverse()
print("reverse 함수 테스트 a값 출력 : " ,a)

a.sort()
print("sort 함수 테스트 a값 출력 : " ,a)

#예제2_1개의_값을_입력_받아_리스트에_저장해봅시다.

sample_list= []    # 빈 리스트 생성
n = int(input('숫자를 입력하세요: '))   
sample_list.append(n)

print(sample_list)

#예제3_여러_개의_문자열을_리스트에_저장해봅시다.

n = input().split()
print(n) 

#예제4_여러_개의_정수를_입력_받아_리스트에_저장해봅시다.

int_list = list(map(int, input("숫자를 입력하세요!").split()))
# input().split()으로 입력받은 리스트의 요소들에 int() 함수가 적용되어 map자료로 반환된 결과를 list 자료형으로 변환해주는 코드 

print(int_list)

#### 예제4 해설
#list(map(int, input("숫자를 입력하세요!").split()))` 함수는 세 부분으로 나누어볼 수 있습니다.  

#A = input("숫자를 입력하세요!").split()`는   
#입력된 문자열을 공백을 기준으로 나누어 리스트로 반환합니다.   
#(이때 반환한 리스트를 A라고 해봅시다.)  

#map(int, input("숫자를 입력하세요!").split())` 는   
#위의 리스트 A를 대입하면 `map(int, A)`로 정리될 수 있습니다.   
#즉 입력값을 공백으로 나누어 반환한 리스트의 모든 요소에 int()함수를 적용하는 것입니다.  

#list(map(int, A))`는 정수형으로 변환된 데이터들을 list로 묶어줍니다. 

# 듀플
# 리스트와 비슷한 데이터 묶어 사용하는 자료형
# 튜플은 내부 데이터 수정 불가
# 튜플은 메모리 효율이 좋음
# 튜플은 소괄호 및 콤마로 구분
# 인덱스 사용가능

#예제1_튜플을_만들고_출력해봅시다.

fruit_tuple = ("apple", "banana", "cherry")
price_tuple = (3000, 1800, 7000)

print(fruit_tuple)
print(price_tuple)

# 듀플 -> 리스트로 변환
# list(듀플 이름): 듀플을 리스트로 변환하는 함수

#예제2_튜플을_리스트로_변경해봅시다.

# 주어진 튜플
fruit_tuple = ("apple", "banana", "cherry")
price_tuple = (3000, 1800, 7000)

# 튜플을 리스트로 변환
fruit_list = list(fruit_tuple)
price_list = list(price_tuple)

# 변환된 리스트 출력
print("Fruit List:", fruit_list)
print("Price List:", price_list)


# 리스트를 다시 튜플로 변환
new_fruit_tuple = tuple(fruit_list)
new_price_tuple = tuple(price_list)

# 변환된 튜플 출력
print("New Fruit Tuple:", new_fruit_tuple)
print("New Price Tuple:", new_price_tuple)

# 리스트 -> 듀플로 변환
# tuple(리스트 이름): 리스트를 듀플로 변환하는 함수


# 딕셔너리
# 리스트와 함께 파이썬에서 자주 사용하는 자료형
# 키와 값으로 이루어짐
# 중괄호 및 키:값 형태로 구분
# 딕셔너리는 인덱스 대신 키로 접근

# 딕셔널이 조회
# 특정 아이템 조회 시 키를 이용
# 리스트의 인덱스와 같음

# 아이템 삽입
# 딕셔널이이름(키값)=값 의 형태로 작성
# 새키와 원래키는 중복 불가
# 중복시 키값은 새키로 변경됨

# 딕셔널이 주의 할점
# 키는 중복 불가
# 값은 중복 가능
# 키와 값 사용 데이터는 어떤 자료형이든 가능
# 문자열:정수, 정수:문자열, 문자열:실수, 문자열:문자열 모두 가능
# 문자열:리스트, 문자열:튜플, 문자열:딕셔너리도 사용 가능

#예제1_딕셔너리를_만들고_출력해봅시다.

menu_dict = {'커피':500, '우유':300, '물':200}

print(menu_dict)

#예제2_딕셔너리에_새로운_요소를_추가해봅시다.

menu_dict = {'커피':500, '우유':300, '물':200}
print(menu_dict)

menu_dict['주스'] = 400
print(menu_dict)