# 4장 프로젝트
# 계절 맞히기 

# 선택구조를 활용하여 입력받은 월에 따라 해당 계절을 출력하는 프로그램 만들기

# 3~5월은 봄
# 6~8월은 여름
# 9~11월은 가을
# 12~2월은 겨울

num = int(input("월을 입력하세요(1~12): "))
if num == 12 or num == 1 or num == 2:
    print("겨울입니다.")    
elif num == 3 or num == 4 or num == 5:
    print("봄입니다.")  
elif num == 6 or num == 7 or num == 8:
    print("여름입니다.")    
elif num == 9 or num == 10 or num == 11:
    print("가을입니다.")        
else:
    print("잘못된 입력값입니다. 재입력 해주세요.")