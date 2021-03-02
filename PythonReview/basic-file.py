score_file=open("score.txt", "w",encoding="utf8") # 덮어쓰기
print("수학: 100", file=score_file)
print("영어 :50", file=score_file)
score_file.close()

score_file=open("score.txt", "a",encoding="utf8") # append
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# score_file = open("score.txt", "r",encoding="utf8") # 읽어오기
# print(score_file.read()) # 모든 내용 출력
# score_file.close()

score_file = open("score.txt", "r",encoding="utf8")
print(score_file.readline()) # 한 줄만 읽어오기 (줄별 읽기 -> 커서 다음 줄로 이동)
print(score_file.readline(), end="")
print(score_file.readline())
print(score_file.readline())
score_file.close()

# 몇 줄인지 모를 때
score_file = open("score.txt", "r",encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # 읽어 온 내용이 없으면
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r",encoding="utf8")
lines = score_file.readlines() # 모든 라인 가져와서 list에 저장
for line in lines:
    print(line, end="")
score_file.close()