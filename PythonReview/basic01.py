
# list
family = ['mother', 'father', 'gentleman', 'sexy lady']
len(family) # 4

# 직각삼각형 그리기
length = int(input('변의 길이: '))
for i in range(length):
    print(' * ' * (i+1))

area = (length ** 2) /2
print('넓이 : ', area)

# 전달 함수
def profile(name, age, main_lang):
    print("이름: {0} \t 나이 : {1} \t 사용 언어: {2}".format(name, age, main_lang))

profile("윤소윤", 27, "파이썬")
profile("차은우", 26, "자바")

# 같은 학교, 같은 학년, 같은 반, 같은 수업
def profile(name, age=20, main_lang="파이썬"): # 기본값 셋팅
    print("이름: {0} \t 나이 : {1} \t 사용 언어: {2}".format(name, age, main_lang))

profile("유재석")
profile("박보검")