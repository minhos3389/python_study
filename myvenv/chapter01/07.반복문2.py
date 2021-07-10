korean_word_list = ["안녕", "반가워", "친구"]
correct = 0

for i in korean_word_list:
    print("Let's learning Korean")
    print(i)
    word = str(input("해당 단어를 입력해주세요 >>> "))
    # if data != word:
    #   break
    if i == word:
        print("맞았습니다.")
        correct += 1
    else:
        print('틀렸습니다.')

        

print(f"전체 문제 개수: {len(korean_word_list)} 개")
print(f"맞힌 문제 개수: {correct} 개")
print(f"틀린 문제 개수: {len(korean_word_list) - correct} 개")