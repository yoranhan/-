1 번 문제
print("원의둘레와 면적을 계산")
r=float(input('cm'))
l1= str(2*r)
l2=l1+ 'ㅠ'

s1=str(r*r)
s2=s1+'ㅠ'

print('둘레 : ' +l2 ,'넓이 : ' +s2)

2번 문제
price = float(input('구매 가격'))
discount = float(input('할인율'))
delivery = float(input('배송비'))

nam = price - (discount/100 * price) +delivery

if nam<=0:
    print("다시 생각해보죠")
else:
    print(str(nam) +' 원 입니다')


3번 문제
year = int(input('현년도'))
birth = int(input('탄생년도'))

total= year - birth

print(str(total) + '세 입니다 .')

4번 문제
year = int(input('연도'))
month = int(input('달'))
day = int(input('일'))

if 0 < month < 10:
    month1 = 'O'+str(month)
elif 9< month <13:
    month1= str(month)
else:
    print("그러한 달은 없습니다.")
    
if 0 < day < 10:
    day1 = 'O' + str(day)
elif 9< day <32:
    day1 = str(day)
else:
    print("그러한 일은 없습니다.")
    
if 0 < year < 10:
    year1 = 'OOO' + str(year)
elif 9< year <100:
    year1 = 'OO' + str(year)
elif 99< year <1000:
    year1 = 'O'+str(year)
elif 999< year <10000:
    year1 = str(year)
else:
    print("지원하지 않습니다.")
    
print(year1+"-" + month1+"-" +day1 )
