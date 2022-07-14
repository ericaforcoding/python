# 문자열 word가 주어질 때, 해당 문자열에서 `a` 가 처음으로 등장하는 위치(index)를 출력해주세요.
#`a` 가 없는 경우에는 `-1`을 출력해주세요.
#`**find()` `index()` 메서드 사용 금지**
# Input =banana
# output = 1


word = input()
result = 0
for char in range(len(word)):
    if char == 'a':                   
#char 를 range로 부터 인덱스로 활용하기로 했으니 word[char]가 되어야합니다!
#char == 'a'는 char가 [0,1,2,3,4] 같은 숫자로 값이 돌아가다보니
#숫자랑 문자열을 비교하는 꼴입니다
#그래서 오류가 나요!
        result += int(len(word))
        #아예 필요없는 라인
        print(result)

    else:
        print(-1)
#print = -1 역시 오류가 납니다!
#print는 변수가 아니고 함수로 사용하셔야해서 print(-1) 이 맞습니다!