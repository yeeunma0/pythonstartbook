#6-1
s,c=0,1
while c<=100:
    s+=c
    c+=1
print(s)

#6-2
s,c=0,1
while s<10000:
    s+=c
    c+=1
print(f'{c-1}일 째에 총 금액이 {s}$가 됩니다.')

#6-5
total=0
for x in [1,2,8,4]:
    total+=x
print(total)

#6-6
L=['egg','onion','carrot']
for x in L:
    print(x)

#6-7
total=0
for x in range(101):
    total+=x
print(total)

#6-8
import math
for i in (1,2,3,4):
    print(math.factorial(i))

#6-9
for c in 'a-#@A^%':
    print(c, ord(c))

#6-10
s=0
for i in range(1,101):
    if i%7==0:
        print(i)
        s=s+i
print(f'합계={s}')

#6-11
nums=[]
while True:
    num=int(input('숫자를 입력하시오. (종료: -999)'))
    if num==-999:
        break
    nums.append(num)
print(f'당신은 {nums}를 입력했습니다.')
print(f'합은 {sum(nums)}입니다.')

#6-12
for x in range(2,11):
    isPrime=True
    for y in range(2,x//2):
        if x%y==0:
            isPrime=False
            break
    if isPrime:
        print()

#6-13
nums=[]
for x in range(1,21):
    if x%3==0 or x%7==0:
        continue
    nums.append(x)
print(nums)

#7-1
L=[1,0,0,5,0,3,0,0,2,0,1,0]
while 0 in L:
    L.remove(0)
print(L)

#7-2
del_list=[4,7]
L=[1,3,4,4,3,2,7,4,1,7,4]
for x in del_list:
    while x in L:
        L.remove(x)
print(L)

#7-3
a=[-3.2, 5.5, 4.1, 1.1, -1.3, 2.7, 0.5]
temp=a.copy()
temp.sort(reverse=True)
print(f'sorted={temp}')
for x in temp[:3]:
    while x in a:
        a.remove(x)
print(f'removed={a}')

#7-4
a=['K','o','r','e','a']
buff=[]
for x in a[:4]:
    buff.append(x)
for _ in range(3):
    b=buff.pop()
    print(b)

#7-5
s=[1.0,0,5,0,3,0,0,2,0,1,0]
while s.count(0)>4:
    s.remove(0)
print(s)

#7-6
s=[7,8,8,7,5,6,8,9,8]
n=s.count(8)
L=[];p=0
for _ in range(n) :
    p=s.index(8,p)
    L.append(p)
    p+=1
print(L)

#8-20
import random as rm
coin=['앞','뒤']
res=[rm.choice(coin) for _ in range(10)]
print(res)

#8-21
import random as rm
res=[rm.randint(1,6) for _ in range(10)]
print(res)

#8-22
import random as rm
tong=range(1,46)
lotto=[rm.choice(tong) for _ in range(7)]
print(lotto)

#8-23
import random as rm
tong=range(1,46)
lotto=rm.sample(tong,7)
print(lotto)

#8-24
import random as rm
faces=13*['♠']+13*['◇']+13*['♡']+13*['♣']
numbers=4*(['A']+[str(i) for i in range(2,11)]+['J','Q','K'])
deck=[f+n for f,n in zip(faces,numbers)]
for i in range(5):
    cards=rm.sample(deck,7)
    for x in cards:deck.remove(x)
    print('player'+str(i+1),cards)

#9-1
def add(a,b):
    c=a+b
    return c

#9-2
def add(a,b):
    c=a+b
    return c
ret=add(3,4)
print(ret)

#9-3
def add(a,b):
    return a+b
print(add(3,4))
print(add(3.1,4.7))
print(add([1,2,3],[4,5,6]))
print(add((1,2,3),(4,5,6)))
print(add('Apple','mango'))
print(add(['Rock'],['paper','Scissors']))

#9-4
def CtoF(C):
    return [c*1.8+32 for c in C]
C=[25.4, 33.2, 66.7]
F=CtoF(C)
print(f'섭씨 : {C} [C]')
print(f'화씨 : {F} [F]\n')

#9-5
def getDivisors(n):
    res=[]
    for i in range(1,n//2+1):
        if n%i==0:
            res.append(i)
    return res
print(getDivisors(28))

#9-6
def getDivisors(n):
    res=[]
    for i in range(1,n//2+1):
        if n%i==0:
            res.append(i)
        return res
def checkPerfect(n):
    div=getDivisors(n)
    return sum(div)==n
num=[]
for n in range(2,10000):
    if checkPerfect(n):
        num.append(n)
print(f'10000이하의 완전수는 = {num}')

#9-7
def getDivisors(n):
    return [i for i in range(1,n//2+1) if n%1==0]
def checkPerfect(n):
    return sum(getDivisors(n))==n
num=[n for n in range(2,10000) if checkPerfect(n)]
print(f'10000이하의 완전수는 = {num}')

#9-8
def fun():
    global a
    a=5
    print(a)
a=100
print(a)
fun()
print(a)

#9-9
def add(a,b=1):
    c=a+b
    return c
print(add(3,4))
print(add(3))

#9-10
def cylinder(radius,height=1):
    pi=3.141592
    surf=2*pi*radius**2+2*pi*radius*height
    volumn=pi*radius**2*height
    return surf,volumn
r,h=1,2
a,v=cylinder(r,h)
print(f'반경이 {r} 높이가 {h}인 원통은')
print(f'표면적은 {a} 부피는 {v}이다.')

#9-11
def printVal(a,b,c):
    s=f'a is {a}, b is {b} and c is {c}'
    print(s)
printVal(1,2,3)

#9-12
def printVal(a,b,c):
    s=f'a is {a},b is {b} and c is {c}'
    print(s)
printVal(1,c=33,b=0.1)

#9-13
def printVal(*a):
    print(type(a))
    for v in a:
        print(v)
printVal(1,2,3)

#9-14
def printVal(a):
    for v in a:
        print(v)
printVal((1,2,3))

#9-15
def sum0sequence(*seq):
    print(f'sum{seq}={sum(seq)}')
sum0sequence(1,9,8,7)

#9-16
def todaysmenu(*menu):
    print('* 오늘의 메뉴 *')
    for m in menu:
        print(f'▷{m}')
todaysmenu('김밥','샐러드','짜장면','햄버거')

#9-17 
def register(**kwd):
    print(f"name:{kwd['name']},age:{kwd['age']}")
register(name='마이클',age=39)
register(age=15,name='엘사')

#9-18
def printVal(**kw):
    for k,v in kw.items():
        print(k,v)
printVal(a='one',b='two',c='ten')
d={'a':'one','b':'two'}
printVal(**d)

#9-19
def evalBMI(**kw):
    weight=kw['weight']
    height=kw['height']
    BMI=weight/height**2
    if BMI<18.5:
        return '마른 체형'
    if BMI<25.0:
        return '표준'
    elif BMI<30.0:
        return '비만'
    else:
        return '고도비만'
res=evalBMI(weight=72,height=1.76)
print(f'당신은 {res}입니다.')

#9-20
g=lambda x,y:x+y
print(g(3,4))

#9-21
finc=lambda x, inc=1:x+inc
print(finc(3))
print(finc(3,6))

#9-22
power=lambda x,y=0:x**y
print(power(2,4))
print(power(2))

#9-23
genSet=lambda x,y:{e for e in range(x,y+1)}
print(genSet(5,13))

#9-24
L=[]
g=lambda x:x**2+1
for i in range(10):
    L.append(g(i))

#9-25
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def compute(s):
    if '+' in s:
        arg=s.split('+')
        res=d['+'](float(arg[0]),float(arg[1]))
    else:
        arg=s.split('*')
        res=d['*'](float(arg[0]),float(arg[1]))
    print(f'{s}={res:.3f}')
d={'*':mul,'+':add}
compute('10.2+5.6')
compute('33.3*2')

#9-26
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def f(g,a,b):
    return g(a,b)
print(f(add,2,7))
print(f(mul,13,5))

#9-27
def gen(fun):
    res=[]
    for x in range(-5,5):
        res.append(fun(x))
    return res
y=gen(lambda x:x*x-3*x-10)
print(y)

#9-28
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def selector(c):
    return add if c=='+' else mul
print(f"2.54*3={selector('*')(2.54,3)}")
