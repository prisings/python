#input시 입력받게되는 값은 숫자를 입력해도 string  cast 필요
#split
""" 
text = input("날")
y,m,d = text.split('.')

print ( text,y,m,d) """
#map(함수,배열) -> 배열의 값을 함수적용
a,b,c = map(int,input("값").split()) #이런경우 값을 입력할때 space bar 를 넣어 하나씩 입력해준다 ex) 1 2 3  
print(a,b,c,a+b+c)
# 문자 숫자 한번에 출력 자바 printf 와 비슷
print('{} 이 {} 더하면 {} 다'.format(1,2,3))

#반올림 round(a) or round(a,b) => b는 소수점 자리수 (반올림으로 올라가게되면 높아질자리)
#제곱 pow(a,b)
#절대값 abs(a)
#나눗셈 divmod(a,b)