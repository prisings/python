text = 'abc' # 해당 문자하나당 인덱스가 존재 
#음수로도 출력가능 but 정반대 문자가 n 개일때 첫번째가 -n이 된다


#문자열 슬라이스 
#위의 인덱스를 이용하는것은 똑같으나 [2:4] => 2번째 3번째 문자를 선택하는게 된다
#[2:8:2] 2칸씩 이동 ? 

#출력지정 format
text = '{}{}'
print(text.format(123,456))
#합치기
text = 'abced'
print('/'.join(text))
#개수확인하기
text.count('a')
#제거하기
text.strip() #양쪽다제거
text.lstrip() #왼쪽에서제거
text.rstrip() #오른쪽에서 제거
