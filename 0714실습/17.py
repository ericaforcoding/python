#소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
#`**.upper()`, `.swapcase()` 사용 금지**
#Input banana
# Output BANANA
# 파이썬 활용
# 특정 문자에 대응 되는 유니코드 숫자로 반환하는 함수는 `ord` 이다.
# ord('a') 
# 97
#해당 유니코드 숫자를 문자로 반환하는 함수는 chr이다. 
#chr(97)
# 'a'

## ord() ->숫자 변환(str->int) ->chr()->문자변환

#  banana

#'big'='small'-32

#word = 'banana'
#result = 0 
#for i in word:
 #   if i == 'b':
  #      print(ord('b') - 32)   #66

   #     print(chr(ord('b') - 32), end="") #B


# 1. 

word = 'banana'
result = 0 
for i in word:
    if i == 'b':
        print(chr(ord('b') - 32),end="") 
    elif i == 'a':
        print(chr(ord('a') - 32),end="")
    elif i == 'n':
        print(chr(ord('n') - 32),end="")


#2. dic = {str : int}
#  [('b' : 98), ('B' : 66), ('a' : 97), ('A': 65), ('n' : 110), ('N' :78)]
#.update()

#dict = {'b' : 98, 'B' : 66, 'a' : 97, 'A': 65, 'n' : 110, 'N' :78}
dict = {'b' : ord('b'), 'B' : ord('b') - 32, 'a' : ord('a'), 'A': ord('a') - 32, 'n' : ord('n'), 'N' : ord('n') - 32}
'b' in dict 
for i in dict:
    if i == 'b':
        print(dict['b'])
        print(chr(dict['b']))

dict = {'b' : ord('b'), 'B' : ord('b') - 32, 'a' : ord('a'), 'A': ord('a') - 32, 'n' : ord('n'), 'N' : ord('n') - 32}

for i in dict:
    if i in dict:
        print(chr(dict['b']))


for i in dict:
    if i == 'b':
        print(dict['b'])
        print(chr(dict['b']))