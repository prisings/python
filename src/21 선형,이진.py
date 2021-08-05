li = [1,2,3,4,5,6,7,8,9,10]
n = int(input("num"))
#선형
for i in range(len(li)):
    if li[i] ==n:
        print("선형",i)
        break


#이진(중간값) sort가 안되어있다면 거진 불가능한 방법

s_index = 0
e_index = len(li)-1

while s_index <= e_index:
    m_index = (s_index + e_index)//2
    if n < li[m_index]:
        e_index = m_index-1
    elif n > li[m_index]:
        s_index = m_index+1
    else:
        print("이진", m_index)
        break

    