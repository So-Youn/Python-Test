# 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장해줌
import pickle
profile_file=open("profile.pickle", "wb") # binary 타입
profile = {"이름":"윤소윤", "나이" :27, "취미":["영화보기","노래듣기","코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file=open("profile.pickle", "rb") # 읽기
profile = pickle.load(profile_file) # 파일 내용을 가져와서 profile에 불러옴
print(profile)
profile_file.close()

# with로 더 편하게 작업 가능 - 파일 열어서 profile_file 변수로 저장
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) # close 해줄 필요 없이 with 탈출

# 파일 쓰기
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 복습하는 중")

# 파일 읽기
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())



# X 주차 주간보고
# 1주차부터 50주차까지 보고서 파일 만드는 프로그램 작성
for i in range(1,51):
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write(" - {0} 주차 주간 보고 - ".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")