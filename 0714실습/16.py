#문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
#모음 : a, e, i, o, u 
#**count()` 사용 금지**

##Input apple
### Output 2


#1.

word = 'apple'
cnt = 0
for vowels in word:
      if vowels == 'a' or 'e' or 'i' or 'o' or 'u':  # 이렇게 줄일 수 없음! a부터 e까지 다 들어가서 5나옴
        cnt += 1
print(cnt)  #5 나옴


#1. correction

word = 'apple'
cnt = 0
for vowels in word:
      if vowels == 'a' or vowels == 'e' or vowels == 'i' or vowels == 'o' or vowels =='u':  
        cnt += 1                                   
                                          
print(cnt)

#2. elif

word = 'apple'
cnt = 0
for vowels in word:
      if vowels == 'a' :
         cnt += 1 
      elif vowels == 'e':
         cnt += 1 
      elif vowels == 'i':
         cnt += 1 
      elif vowels == 'o':
         cnt += 1 
      elif vowels =='u':
         cnt += 1                                            
                                        
print(cnt)

word = 'apple'
cnt = 0
for vowels in word:
    if vowels == ['a', 'e', 'i', 'o', 'u']: #if 변수 in 리스트로 하시면 답이 뚝 나와버려요!
                                            #사용하시는 연산자가 == 는 같다인데 리스트와 그냥 문자열을 비교할 수는 없습니다!  따라서 in을 쓰면 이 문자열이 이 안에 있는가? 라는 조건으로 바뀌어서 원하시는 바에 딱 맞는 답이됩니다 ㅎㅎ
        cnt += 1
print(cnt) #0 나옴

#2. correction

word = 'apple'
cnt = 0
for vowels in word:
    if vowels in ['a', 'e', 'i', 'o', 'u']:
        cnt += 1
print(cnt)


#3. 2 풀려다가 틀림

word = 'apple'
cnt = 0
for vowels in word:
    if vowels == ['a', 'e', 'i', 'o', 'u']:
        cnt += 1
print(sum(cnt))   #'int' object is not iterable