######################################
# Function to get sum of two numbers #
#        written by AB.John          #
######################################
def sum(a,b):
    return a+b
#main start
x,y=3.78,5.43
#x,y=3.78,5.43
print('sum=',sum(x,y)) #simple form
#comment out print using f string
print(f'sum of {x},{y}={sum(x,y):7.2f}') #f-string

def sumTwo(a,b) :
    '''이것은 두 개의 수를 더하는 함수이다.
                             작성자 심민희'''
    return a+b
#main start
x,y=3.78,5.43
print('sum=',sumTwo(x,y))
'''comment out print using f string
print(f'sum of {x},{y}={sumTwo(w,y):7.2f}')'''

a=100;b=10
c=a+b
print('a=',a,'b=',b,'c=',c)

name='김명수';age=18
print('이름=',name,'나이=',age)

#2-3
'''num=int(input('정수를 입력하세요:'))
if num%2==0:
    print('당신은 짝수를 입력했습니다!')
else:
    print('당신은 홀수를 입력했습니다!')'''

#2-4
'''answer=7
while int(input('0에서 9까지의 숫자를 맞춰주세요 : '))!=answer:
    print('답이 아닙니다!')
print('축하합니다!!! 답은 ',answer,'이었습니다.')'''

#2-5
'''import random
answer=random.randint(0,9)
while int(input('0에서 9까지의 숫자를 맞춰주세요:'))!=answer:
    print('답이 아닙니다!')
print'''

#2-6
for e in [7,33,58] : #list
    print(e)

#2-7
for e in ['ham','egg','cheese']: #list
    print(e)

#2-8
for e in 'love': #string
    print(e)

#2-9
for x in range(4): #0~3
    print('하')

#3-1
name='고민식'
age=17
temperature=37.1
print('이름:',name,'나이:',age,'체온:',temperature,'도')

#4-2
pi=3.141592
반경=float(input('원의 반경을 입력하시오 : '))
원주=2*pi*반경
면적=pi*반경**2
print('면적 : ',면적, '원주 :', 원주)

#4-3
숫자=int(input('세 자리 정수를 입력하시오 : '))
백자리=숫자//100
십자리=(숫자//10)%10
일자리=숫자%10
print('백의 자리: ',백자리,', 십의 자리:',십자리,'일의 자리 : ', 일자리)

#4-4
hue, saturation, value=355,85,55
weight = 88
if weight>80:
    if(hue<=10 or hue>=350) and saturation>=85 and value>=65:
        print('합격!!')
    else:
        print('컬러 불합격!')
else:
    print('중량 불합격!!')

#4-5
data=0b00110101
mask=0b00011000
res=data&mask
print(bin(res))
print(bin(res>>3))#비트 오른쪽으로 3칸 이동
'''출력값:0b10'''

#4-6(p.108)
data=0b00110101
m,n=2,6
print(bin(1<<m))
res_m=(data&1<<m)>>m
res_n=(data&1<<n)>>n
print(bin(res_m|res_n<<1))
'''출력값:0b1'''

#4-7(p.110)
data=0b00110101
m,n=2,6
mask=1<<m|1<<n
result=data^mask
print(f'data={bin(data)}')
print(f'mask={bin(mask)}')
print(f'result={bin(result)}')
'''data =0b110101
mask =0b1000100
result =0b1110001'''

#4-8
fact=1
for n in range(1,11):
    fact*=n
print(f'10!={fact}')

#4-9
사용자수 =int(input('정수를 입력하세요:'))
판단='3의 배수' if 사용자수%3==0 else '3의 배수 아님'
print(사용자수,'은/는', 판단)

#4-10
import random as rd
for _ in range (4):
    v=rd.randint(0,15)
    for i in range(4):
        y='x' if (v&1<<i) else '0'
        print(y, end='')
        print('')

#4-11
a=int(input('시작 수를 입력하시오:'))
b=int(input('끝 수를 입력하시오 :'))
for n in range(a,b+1):
    print(n,':', bin(n),':',hex(n))

#4-12
import math
DEG2RAD=math.pi/180
for d in range(0,181,30):
    print(d,':',math.sin(DEG2RAD*d))

#5-1
a=14
if a>=13:
    print('Pass')

#5-2
age,height=8,135
if age>=13 or height>=130:
    print('놀이기구를 탈 수 있습니다.')
    print('입장하세요')

#5-3
n=int(input('임의의 정수를 입력하시오:'))
if n%2==0:
    print('짝수')
else:
    print('홀수')

#5-4
s=88
print('당신의 점수 : ',s)
print('등급 : ', end='')
if s>=90:
    print('A')
elif s>=80:
    print('B')
elif s>=70:
    print('C')
elif s>=60:
    print('D')
else:
    print('F')

#5-5
age=int(input('나이를 입력하시오:'))
if age>= 65:
    print('노년입니다.')
elif age>=40:
    print('중년입니다.')
elif age>=20:
    print('청년입니다.')
else:
    print('소년입니다.')

#5-6
data=input('2차 방정식의 계수 a,b,c를 입력하시오 : ')
a,b,c=[float(x) for x in data.split(',')]
if a==0.:
    print('한 개의 실근')
else:
    if b**2>4*a*c:
        print('서로 다른 두 개의 실근')
    elif b**2==4*a*c:
        print('중근')
    else:
        print('복소근')

#5-7
order='햄버거'
menu={'커피':4000, '햄버거':5000, '콜라':3000, '프라이드 치킨':7000}
price=menu.get(order,0)
print(price)

#5-8
order='햄버거'
if order=='커피':
    price=4.0
elif order=='햄버거':
    price=5.0
elif order=='콜라':
    price=3.0
elif order=='프라이드 치킨' :
    price=7.0
else :
    price=0.0
print(price)
