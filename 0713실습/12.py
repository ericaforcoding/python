#주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.
#apple

word = 'apple'   #[]??
for i in word:
    if i == 'a':
        continue     #if i != 'a':
                     #result = result +char
    print(i, end="")  #추가 설명을 해드리면 print() 함수의 매개변수 중 end는 데이터를 출력했을 때 마지막에 무엇을 출력할지 결정합니다.
                      #함수 정의에서 end의 디폴트 값이 \n(개행문자)라서 print() 를 사용하면 줄바꿈이 발생합니다.
