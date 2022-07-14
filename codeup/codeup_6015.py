# 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.


# input 한 번에 값을 여러 개 입력받으려면 어떻게 해야 할까요? 이때는 input에서 split을 사용한 변수 여러 개에 저장해주면 됩니다
a, b =input().split()  #input().split() 를 사용하면, 공백을 기준으로 입력된 값들을 나누어(split) 자른다.
a = int(a)
b = int(b)
print (a)
print (b)

print(int(input().split()))