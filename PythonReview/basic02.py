# 지역변수 : 함수 내에서만 사용 가능한 변수
# 전역변수 : 프로그램 내에서 어디든지 사용 가능한 변수
gun = 10
def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun)) 

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun)) # 지역변수 계산
    return gun # 바뀐 값을 외부로 던짐

print("전체 총 :{}".format(gun)) 
# checkpoint(2)
gun = checkpoint_ret(gun,2)
print("남은 총:{}".format(gun)) 


# 퀴즈
# 표준 체중을 구하는 프로그램 작성

# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시
print()

def std_weight(height, gender) : # 키는 m단위(실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else : 
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height/100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height,gender,weight))

