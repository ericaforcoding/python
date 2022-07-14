#> 문자열 word가 주어질 때, 해당 문자열에서 `a` 의 모든 위치(index)를 출력해주세요.
#**`find()` `index()` 메서드 사용 금지**
### Input HappyHacking





word = input()
result = 0
for char in range(len(word)):
    if word[char] == 'a':
     print(char)  #print(word[char]) print(word[char]) 는 a 나옴 -> print(char) 로 바꾸셔야 그 떄의 인덱스가 나옵니다!