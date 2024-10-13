#10-1
class Dog:
    name='Rocky'
dog1=Dog()
print(Dog.name) #Rocky
print(dog1.name) #Rocky
Dog.name='Cody'
print(dog1.name) #Cody
dog1.name='Pepe'
print(Dog.name) #Cody
print(dog1.name) #Pepe

#10-2
class Dog:
    name='Rocky'
    def show(self):
        print(self.name)
puppy=Dog()
puppy.name='Toby'
print(puppy.name)
puppy.show()

#10-3
class Dog:
    name='happy'
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
name='badugi'
a=Dog('angry')
s=Dog('sad')
a.show()
s.show()
print(Dog.name)
print(name)

#10-4
import math
class Line:
    def __init__(self,start=(0,0),end=(0,0),color='black'):
        self.start=start
        self.end=end
        self.color=color
    def show(self):
        print(f'from {self.start} to {self.end}')
        print(f'with {self.color}')
    def length(self):
        dx=(self.start[0]-self.end[0])
        dy=(self.start[1]-self.end[1])
        return math.sqrt(dx**2+dy**2)
li=Line((1.0,2.0),(-1.0,3.0),'red')
li.show()
print(f'length={li.length():.5f}')
li2=Line(end=(-1.0,3.0))
li2.show()

#10-5
import random as rm
class Dice:
    def __init__(self,face=6):
        self.face=face
        self.num=1
    def roll(self):
        self.num=rm.randint(1,self.face)
        print(f'n={self.num}')
d=Dice()
for _ in range(5):
    d.roll()

#10-6
d=Dice(12)
for _ in range(5):
    d.roll()

#10-7
class Car:
    def __init__(self,model,engine,color='black'):
        self.model=model
        self.engine=engine
        self.color=color
    def info(self):
        print(f'Model: {self.model}/{self.engine}cc')
        print(f'Color {self.color}')
    def run(self):
        print(f'{self.color}{self.model} 붕붕~~~')

#10-8
bz=Car('Benz E400',4000,'silver')
hd=Car('현대 아반떼',2000,'blue')
bz.info()
bz.run()
hd.info()
hd.run()

#10-9
class Trader:
    def __init__(self,name,*goods):
        self.name=name
        self.goods=list(goods)
    def showGoods(self):
        print(f'{self.name} has {self.goods}')
    def addGood(self,good):
        self.goods.append(good)
    def removeGood(self,good):
        self.goods.remove(good)
    def trade(self,mine,other,his):
        if mine not in self.goods:
            print('{self.name} has no {mine}')
            return
        if his not in other.goods:
            print('{other.name} has no {his}!')
            return
        self.removeGood(mine)
        self.addGood(his)
        other.removeGood(his)
        other.addGood(mine)
        print('Trade is finished..')

#10-10
Persian=Trader('호람','석류','피스타치오','양탄자','샤프란')
Chinese=Trader('왕친친','비단','접시','종이','화약')
Persian.showGoods()
Chinese.showGoods()
Persian.trade('양탄자',Chinese,'비단')
Persian.showGoods()
Chinese.showGoods()

#10-11
class People:
    def __init__(self,name):
        self.__weight=88
        self.__height=1.50
        self.name=name
    def __calc(self):
        return self.__weight/self.__height**2
    def BMI(self):
        return self.__calc()
me=People('Mario')
print(me.BMI())
print(me.__weight)
print(me.__calc())

#p.371 예제1
class Father:
    def __init__(self):
        print('Father')
class Son(Father):
    def __init__(self):
        super().__init__()
son=Son()

#10-12
class Animal:
    def __init__(self,name):
        self.name=name
    def run(self):
        print(f'{self.name} 달려')
class Dog(Animal):
    def shout(self):
        print(f'{self.name} 멍멍~')
class Cat(Animal):
    def shout(self):
        print(f'{self.name} 이야옹~')
d=Dog('마음이')
c=Cat('냥냥이')
d.run()
c.shout()
d.shout()

#10-13
class Car:
    def __init__(self,model,engine,color='black'):
        self.model=model
        self.engine=engine
        self.color=color
    def info(self):
        print(f'Model: {self.model}/{self.engine}cc')
        print(f'Color {self.color}')
    def run(self):
        print(f'{self.color}{self.model} 붕붕~~~')

#10-14
class Truck(Car):
    def __init__(self,model,engine,color='blue',cap=5000):
        #super(Truck,self).__init__(model,engine,color)
        Car.__init__(self,model,engine,color)
        self.capacity=cap
        self.loading=0
    def load(self,w):
        self.loading+=w
    def info(self):
        #super(Truck,self).info()
        Car.info(self)
        print(f'Capacity : {self.capacity/1000:.1f} ton')
        print(f'Current loading: {self.loading} kg')
tr=Truck('Mighty',3900,'White',2500)
tr.load(700)
tr.info()
tr.run()

#11-1
import calendar
c=calendar.TextCalendar(calendar.SUNDAY) #첫 번째 요일 지정
s=c.formatmonth(2020,4) #년과 월 지정
print(s)

#11-2
import calendar
c=calendar.TextCalendar(calendar.SUNDAY)
s=c.formatyear(2020)
print(s)

#11-3
import pickle
data_L=['와플','아이스크림','커피']
data_T=('55','손흥민',187.3)
data_D={'kr':'한글','en':'english'}
with open('test.pkl','wb') as fw: #==WRITE
    pickle.dump(data_L,fw)
    pickle.dump(data_T,fw)
    pickle.dump(data_D,fw)
with open('test.pkl','rb') as fr: #==READ
    data_1=pickle.load(fr)
    data_2=pickle.load(fr)
    data_3=pickle.load(fr)
print(data_1);print(data_2);print(data_3)

#11-4
'''import time as t
import locale
locale.setlocale(category=locale.LC_ALL,locale="ko-KR")
while True:
    t_struct=t.localtime()
    t_string=t.strftime('%y-%b-%d[%a] %p %I:%M:%S', t_struct)
    print(t_string)
    t.sleep(1.0)'''

#11-5
import re
data='''날짜 5월 22일 우리집 상성아파트 401-1311, 02-3742-5534
대흥상회 032-232-3245 김연식 010-2011-2311 건물 평수 48-52평'''
pattern=re.compile('\d{2,3}-\d{3,4}-\d{4}')
matched=pattern.findall(data)
print(matched)

#11-6
import re
data='''김정미 900905-2049118 전화번호 02-3474-4567 나이 31
김정욱 850905-1059119 전화번호 02-5696-8282 나이 36'''
pattern1=re.compile("(\d{6}[-]\d)\d{6}")
data2=pattern1.sub("\g<1>******",data)
pattern2=re.compile("(\d{4}[-])\d{4}")
print(pattern2.sub("\g<1>####",data2))

#11-7
from bs4 import BeautifulSoup
import urllib.request
nav='http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date='
site=nav+'20209010'
soup=BeautifulSoup(urllib.request.urlopen(site).read(),'html.parser')
title=soup.find_all('div','tit5')
point=soup.find('td','point')
for i in range(10):
    print(title[i].get_text().strip(),point[i].string)

#11-8
f=open('d:/pytest.txt','w')
f.write('안녕 파이썬\n')
f.write('이건 파일 실험일뿐!!')
f.close()

#11-9
f=open('d:/pytest.txt','r')
lines=f.read()
print(lines)
f.close()

#11-10
with open('d:/pytest.txt','r') as f:
    lines=f.read()
print(lines)

#11-11
data={x:3.*x**2-5. for x in range(10)}
with open('d:/data.txt','w') as f:
    for x,y in data.items():
        f.write(f'{x:0.3f},{y:0.3f}\n')
with open('d:/data.txt','r') as f:
    lines=f.readlines()
data2=[[float(x) for x in line.split(',')] for line in lines]
print(dict(data2))

#11-12
a,b,c=12,'^.^',2.371
print("{0} {1} {2}".format(a,b,c))
print("{} {} {}".format(a,b,c))
print("{2} {0} {1}".format(a,b,c))

#11-13
a,b,c=12,'^.^',2.371
print("{0} {1} {2}".format(a,b,c))
print("{} {} {}".format(a,b,c))
print("{2} {0} {1}".format(a,b,c))
print("{:d},{:f}".format(a,c))
print("{0:5d},{1:7.5f}".format(a,c))

#11-13
L=[1,2,3]
print('{0[0]},{0[2]}'.format(L))
S='ABC'
print('{0[2]},{0[1]}'.format(S))

#11-15
class Banana:
    size=10; weight=3.5
    def eatme():
        print('Outch!')
ba=Banana()
print("{0.size} and {0.weight}".format(ba))

#11-16
a,b,c=12,'^.^',2.371
print(f'a={a},b={b},c={c}')

#11-17
import math as m
pi,s,c=m.pi, m.sin(m.pi/4), m.cos(m.pi/6)
print(f'pi       : {pi:10.5f}')
print(f'sin(pi/4): {s:10.5f}')
print(f'cos(pi/6): {c:10.5f}')

'''#11-18
try:
    c=1+something*3
except:
    print('예외가 발생하였습니다.')

#11-19
try:
    c=1+something*3
except Exception as e:
    print('예외가 발생하였습니다.')
    print(f'예외 원인: {e}')'''

#11-20
try:
    d='2'+2
except ZeroDivisionError as e:
    print(f'ZeroDivisionError가 발생하였습니다.')
    print(f'예외 유형: {e}')
except TypeError as e:
    print(f'TypeError가 발생하였습니다.')
    print(f'예외 원인: {e}')

#11-21
try:
    f=open('C:/Users/USER/pytest.txt','r')
    lines=f.read()
    print(lines)
except Exception as e:
    print(e)
finally:
    f.close()