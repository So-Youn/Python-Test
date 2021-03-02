def profile(name, age, main_lang):
    print(name, age, main_lang)

# 함수 매개변수 값을 keword로 전달
profile(name="유재석", main_lang="파이썬", age=20) 

# 가변인자 함수 전달 1)
def profile2(name, age, lang1,lang2,lang3,lang4,lang5):
    print("이름 : {0} \t 나이 :{1} \t".format(name,age),end="") 
    print(lang1,lang2,lang3,lang4,lang5)

profile2("윤소윤", 27, "Python","Java","CSS", "Linux","JS")
profile2("차은우", 26, "Kotlin", "Swift", "","","")


# 가변인자 서로 다른 2)
def profile3(name, age, *language):
    print("이름 : {0} \t 나이 :{1} \t".format(name,age),end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile3("윤소윤", 27, "Python","Java","CSS", "Linux","JS")
profile3("차은우", 26, "Kotlin", "Swift")