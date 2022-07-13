#주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
#apple

word = 'apple'

#for 

result = ''
for char in word:
    result = char + result
print(result)

#2. pythonic
#print(word[::-1])
#word[len(word)-i]

#3. index
# for i in range(len(word)):
    #print(word[len(word)-i-1, end='']   #print 안에 기본으로 \n   #sep(' '):여러개를 동시에 출력할 때 사이에 구분값. #end('\n'):프린트 출력이 된 이후 뒤에 뭐를 붙일지
