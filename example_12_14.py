#12-1
import matplotlib.pyplot as plt
y=[1.0, 2.4, 1.7, 0.3, 0.6, 1.8]
plt.plot(y)
plt.grid()
plt.show()

#12-2
import matplotlib.pyplot as plt
x=[0.0, 0.0, 5.0, 6.0, 0.0]
y=[0.0, 5.0, 5.0, 0.0, 0.0]
plt.plot(x,y)
plt.grid()
plt.show()

#12-3
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-1.0,2.0,100)
y=-x**2+5.0
plt.plot(x,y)
plt.grid()
plt.show()

#12-4
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,4*np.pi,100)
y=np.sin(x)
plt.plot(x,y)
plt.grid()
plt.show()

#12-5
import matplotlib.pyplot as plt
import numpy as np
data=[[1.,3.4],[2.,2.3],[3.,2.7],[5.,4.8]]
x=[row[0] for row in data]
y=[row[1] for row in data]
plt.plot(x,y)
plt.grid()
plt.show()

#12-6
import matplotlib.pyplot as plt
import numpy as np
data=[0.00,0.00,0.21,0.80,0.42,-0.15,0.63,-0.50,0.84,0.19,1.05,0.29,1.26,-0.18,1.47,-0.16,1.68,0.15,1.89,0.08,2.11,-0.11,2.32,-0.03,2.53,0.08,2.74,0.01,2.95,-0.05,3.16,0.01,3.37,0.03,3.58,-0.01,3.79,-0.02,4.00,0.01]
x=data[::2]
y=data[1::2]
plt.plot(x,y)
plt.grid()
plt.show()

#12-7
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,5,100)
g=x**2-2
f=0.5*x**3-4*4+1
plt.plot(x,g,x,f)
plt.grid()
plt.show()

#12-8
import matplotlib.pyplot as plt
import numpy as np
data=np.array([[1.,3.4,7.2,5.4],[2.,2.3,6.5,4.3],[3.,2.7,4.6,5.6],[4.,4.8,5.4,2.3]])
x=data[:,0]
y=data[:,1:]
plt.plot(x,y,marker='o')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(['y1','y2','y3'])
plt.grid()
plt.show()

#12-9
import matplotlib.pyplot as plt
import numpy as np
t=np.linspace(0,10,20)
y1=np.sin(t)
y2=np.cos(t)
plt.plot(t,y1,'r:',t,y2,'g--')
plt.xlim(0,10)
plt.ylim(-1.5,1.5)
plt.title('Sine Cosine Plot')
plt.xlabel('Time(t)')
plt.ylabel('y=sin(t),cos(t)')
plt.grid()
plt.show()

#12-10
import matplotlib.pyplot as plt
import numpy as plt
t=np.linspace(0,10,20)
y1=np.sin(t)
y2=np.cos(t)
y3=y1*y2
plt.plot(t,y1,'r:',t,y2,'g--',t,y3,'b-s')
plt.xlim(0,10)
plt.ylim(-1.5,1.5)
plt.title('Sine Cosine Plot')
plt.xlabel('Time(t)')
plt.ylabel('y1,y2,y3')
plt.legend(('y1=sin(t)','y2=cos(t)','y3=sin(t)cos(t)'))

#12-11
import matplotlib.font_manager as fm
font_path=fm.findSystemFonts(fontpaths=None,fontext='ttf')
print(f'총 {len(font_path)} 개의 폰트가 있습니다.')
fonts=[x[17:] for x in font_path]
fonts.sort()
print(f'폰트 파일 이름\n {fonts}')
fnames=[fm.FontProperties(fname=x).get_name() for x in font_path if 'Nanum' in x]
print(f'폰트 패밀리 이름 {fnames}')

#12-12
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family']='NanumGothic'
plt.rcParams['font.size']=14
plt.rcParams['axes.unicode_minus']=False #'-' 깨짐 대응
t=np.linspace(0,10,20)
y=np.sin(t)
plt.plot(t,y)
plt.xlim(0,10)
plt.ylim(-1.5,1.5)
plt.title('사인 그래프')
plt.xlabel('시간(t)')
plt.ylabel('출력값(y)')
plt.grid()
plt.show()

#12-13
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family']='NanumGothic'
plt.rcParams['font.size']=14
plt.rcParams['axes.unicode_minus']=False
과목=['국어','영어','수학','과학','사회']
x=np.arange(len(과목))
점수=[55,35,75,47,60]
plt.bar(x,점수,color='#AADD55',tick_label=과목,width=0.8)
plt.title('나의 성적',color='b')
plt.show()

#12-14
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family']='NamunGothic'
plt.rcParams['font.size']=14
plt.rcParams['axes.unicode_minus']=False
막대_색=[(0.9,0.1,0.6,0.3),(0.5,0.1,0.9,0.3),(0.1,0.9,0.6,0.3),(0.1,0.5,0.9,0.3),(0.6,0.6,0.6,0.3)]
테두리_색=[(0.9,0.1,0.6,0.3),(0.5,0.1,0.9,1.0),(0.1,0.9,0.6,1.0),(0.1,0.5,0.9,0.3),(0.6,0.6,0.6,1.0)]
과목=['국어','영어','수학','과학','사회']
x=np.arange(len(과목))
성적=[55,35,75,47,60]
plt.bar(x,성적,color=막대_색,edgecolor=테두리_색,tick_label=과목)
plt.ylabel('점수')
plt.title('나의 성적')
plt.show()

#12-15
str_data='미국 12, 중국 45, 일본 18, 한국 30, 베트남 8'
labs=[x.strip() for x in str_data.split(',')]
print('labs:',labs)
data=[tuple(x.split()) for x in labs]
countries=[x[0] for x in data]
students=[int(x[1]) for x in data]
print('countries:', countries)
print('students:',students)

#12-16
import matplotlib.pyplot as plt
plt.rcParams['font.family']='NamunGothic'
plt.rcParams['font.size']=10
str_data='미국 12, 중국 45, 일본 18, 한국 30, 베트남 8'
labs=[x.strip() for x in str_data.split(',')]
data=[tuple(x.split()) for x in labs]
countries=[x[0] for x in data]
students=[int(x[1]) for x in data]
plt.pie(students,labels=labs,counterclock=False,autopct='%0.1f %%',startangle=90)
plt.rcParams['font.size']=14
plt.title('국가별 학생수',color='b')
plt.show()

#12-17
import matplotlib.pyplot as plt
plt.rcParams['font.family']='NanumGothic'
plt.rcParams['font.size']=10
str_data='미국 12, 중국 45, 일본 18, 한국 30, 베트남 8'
labs=[x.strip() for x in str_data.split(',')]
data=[tuple(x.split()) for x  in labs]
countries=[x[0] for x in data]
students=[int(x[1]) for x in data]
sect_colors=[(0.9,0.1,0.6,0.3),(0.5,0.1,0.9,0.3),(0.1,0.9,0.6,0.3),(0.1,0.5,0.9,0.3),(0.6,0.6,0.6,0.3)]
explode=[0,0,0,0.2,0]
plt.pie(students,colors=sect_colors, labels=labs,radius=1.0,counterclock=False,startangle=90,explode=explode,autopct='%0.1f %%')
plt.rcParams['font.size']=14
plt.title('국가별 학생수',color='b')
plt.show()

#12-18
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['font.size']=14
data=np.loadtxt("data.txt",float)
x=data[:,0]
y=data[:,1]
z=data[:,2]
color=data[:,3]
plt.scatter(x,y,s=z,c=color,alpha=0.5)
plt.xlabel("온도")
plt.ylabel("압력")
plt.xlim(20,30); plt.ylim(200,500)
plt.show()

#13-1
import numpy as np
import timeit as ti
size_of_vec=1000
def py_version():
    A,B=range(size_of_vec), range(size_of_vec)
    C=[]
    for i in range(size_of_vec):
        C.append(A[i]+B[i])
def np_version():
    A,B=np.arange(size_of_vec), np.arange(size_of_vec)
    C=A+B
t_py=ti.timeit('py_version()',setup='from __main__ import py_version',number=100)
t_np=ti.timeit('np_version()',setup='from __main__ import np_version',number=100)
print(f'python version: {t_py*1000:8.3f}[ms]')
print(f'numpy  version: {t_np*1000:8.3f}[ms]')
print(f'numpy is {t_py/t_np:5.1f} times faster than pure python!')

#13-2
import numpy as np
a=np.arange(1,10)
print(a)
x=range(1,10)
print(x)
x=np.arange(10,4)
print(x)
x=np.arange(0.5,10.4,0.8)
print(x)
print(np.arange(start=7,stop=-3,step=-3))

#13-3
import numpy as np
print(np.linspace(1,10))
print(np.linspace(1,10,7))
print(np.linspace(1,10,7,endpoint=False))

#13-4
import numpy as np
a=np.array(99)
b=np.array([1,2,3,4])
c=np.array([[1,2,3,4]])
d=np.array([[1],[2],[3],[4]])
print(f'{a} shape:{a.shape} dim:{a.ndim}')
print(f'{b} shape:{b.shape} dim:{b.ndim}')
print(f'{c} shape:{c.shape} dim:{c.ndim}')
print(f'{d} shape:{d.shape} dim:{d.ndim}')

#13-5
import numpy as np
data=np.random.rand(3,3)
print(data)
print(data>0.5)
print(data[data>0.5])
data[data<=0.5]=0
print(data)

#13-6
import numpy as np
X=np.arange(28).reshape(4,7)
print(X)
print(X[::2,::3])
print(X[::,::3])

#13-7
import numpy as np
a=np.arange(3*2*4)
t=a.reshape([3,2,4])
print(f'a={t}')
print(f'sum(ax=0) = \n {t.sum(axis=0)}')
print(f'sum(ax=1) = \n {t.sum(axis=1)}')
print(f'sum(ax=2) = \n {t.sum(axis=2)}')

#13-8
import numpy as np
A=np.array([[42,22,12],[44,53,66]])
print(f'original A=\n{A}')
B=A.copy()
C=A
C[0,0]=99
print(f'affected A=\n{A}')
print(f'B=\n{B}')

#13-9
import numpy as np
A=np.array([[1,2,3],[3,2,1],[1,0,1]])
B=np.array([[2,3,4,-2],[1,-1,2,3],[1,2,3,0]])
x=np.array([[1,-1,1]])
print(f'A@B={A@B}')
print(f'x@A={x@A}')
print(f'x@x.T={x@x.T}')
print(f'x.T@x={x.T@x}')

#13-10
A=np.array([[5,1],[1,-2]])
b=np.array([[4],[-6]])
x=np.linalg.solve(A,b)
print(x)
print(A@x)

#13-11
import matplotlib.pyplot as plt
import numpy as np
x=np.array([0.,1.2,1.9,3.1])
y=np.array([-1.8,0.1,1.2,2.3])
b=y[:,np.newaxis]
A=np.vstack((x,np.ones_like(x))).T
print(f'A=\n{A}')
s,_,_=np.linalg.lstsq(A,b,rcond=None)
p,q=s[0,0],s[1,0]
print(f'p={p:0.4f},q={q:0.4f}')
plt.plot(x,y,'ro')
plt.plot(x,p*x+q,'b:')
plt.title(f'Fitting to y={p:0.3}x {q:0.3}')
plt.legend(['data','y=p*x+q'])
plt.grid()
plt.show()