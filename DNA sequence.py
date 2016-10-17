s=[list('GTCACCAC'),list('GTCCGAAT'),list('GACCTATC'),
   list('TCCAACCC'),list('CCAATAGC'),list('GAGGCCGA'),
   list('ATTCCAAT'),list('GACCATTT')]

def dnapermutation(m,n):
    m=[]
    for a in range(4):
        x=s[n][a:a+5]
        m.append(x)
        a+=1
    return m
#将每一条脱氧核糖核酸的可能序列（4种）求出再合并为一个列表，分别赋值到sdna1~8变量里
s1=[]
n=0
sdna1=dnapermutation(s1,n)

s2=[]
n=1
sdna2=dnapermutation(s2,n)

s3=[]
n=2
sdna3=dnapermutation(s3,n)

s4=[]
n=3
sdna4=dnapermutation(s4,n)

s5=[]
n=4
sdna5=dnapermutation(s5,n)

s6=[]
n=5
sdna6=dnapermutation(s6,n)

s7=[]
n=6
sdna7=dnapermutation(s7,n)

s8=[]
n=7
sdna8=dnapermutation(s8,n)
##dna={}
##for i in range(8):
##    lt=dnapermutation(i)
##    dna['s'+str(i)]=lt

dnalist=[]
for a in sdna1:
    for b in sdna2:
        for c in sdna3:
            for d in sdna4:
                for e in sdna5:
                    for f in sdna6:
                        for g in sdna7:
                            for h in sdna8:
                                dnalist.append((a,b,c,d,e,f,g,h))
pass
#一种可能下的分值
dnazero=[]
dnaone=[]
dnatwo=[]
dnathree=[]
dnafour=[]
for n in range(0,4**8):
    for i in range(8):
        dnazero.append(dnalist[n][i][0])
        dnaone.append(dnalist[n][i][1])
        dnatwo.append(dnalist[n][i][2])
        dnathree.append(dnalist[n][i][3])
        dnafour.append(dnalist[n][i][4])
pass
def f(list,width):
    return [list[x:x+width] for x in range(0,len(list),width)]

dnazeroslice=f(dnazero,8)
dnaoneslice=f(dnaone,8)
dnatwoslice=f(dnatwo,8)
dnathreeslice=f(dnathree,8)
dnafourslice=f(dnafour,8)

def my_func(num):
    singlezero=[]
    singleone=[]
    singletwo=[]
    singlethree=[]
    singlefour=[]
    basicgroup=['A','G','C','T']
    for m in basicgroup:
        letterzero=dnazeroslice[num].count(m)
        letterone=dnaoneslice[num].count(m)
        lettertwo=dnatwoslice[num].count(m)
        letterthree=dnathreeslice[num].count(m)
        letterfour=dnafourslice[num].count(m)
        singlezero.append(letterzero)
        singleone.append(letterone)
        singletwo.append(lettertwo)
        singlethree.append(letterthree)
        singlefour.append(letterfour)
        scorelist=[max(singlezero),max(singleone),max(singletwo),max(singlethree),max(singlefour)]
        scorezero=sum(scorelist)
    return scorezero
    
scorelist=[]
for x in range(0,4**8):
    score=my_func(x)
    scorelist.append(score)
pass

bestscore=max(scorelist)
print bestscore


d={}
for num in range(0,4**8):
    d.setdefault(my_func(num),num)
pass
#算出my_func的目标参数是31038，29分
target=d[bestscore]
#在解释器里分别打出dnazero(one,two,three,four)sliece[350742],
##['T', 'C', 'C', 'C', 'C', 'G', 'C', 'C']---------C
##['C', 'G', 'C', 'C', 'C', 'C', 'C', 'C']---------C
##['A', 'A', 'T', 'A', 'A', 'C', 'A', 'A']---------A
##['C', 'A', 'A', 'A', 'A', 'G', 'A', 'T']---------A
##['C', 'T', 'T', 'C', 'T', 'A', 'T', 'T']---------T
##即 模体是CCAA
    












