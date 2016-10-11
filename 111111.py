f=open(r'D:\python\Δ£Με.txt')
d={1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{}}
for i in range(1,9):
    m=f.readline()
    m=m.replace('\n','')        
    for j in range(0,4):
        d[i][j+1]=m[j:j+5]
f.close()
def Score(Di,n):
    score=0
    motif=[]
    for l in range(0,5):
        a,t,c,g=0,0,0,0
        for i in range(0,n):
            if Di[i][l]=='A':
                a+=1
            elif Di[i][l]=='T':
                t+=1
            elif Di[i][l]=='C':
                c+=1
            elif Di[i][l]=='G':
                g+=1
            print a,t,c,g
        s=max(a,t,c,g)
        if s==a:
            motif.append('A')
        elif s==t:
            motif.append('T')
        elif s==c:
            motif.append('C')
        elif s==g:
            motif.append('G')
        score+=s                              
    return (motif,score)
##mo2=[]
##sco2=0
for i in range(1,5):
    for j in range(1,5):
        d1=[d[1][i],d[2][j]]
        print d1
##        (m,s)=Score(d1,2)
##        if s>sco2:
##            sco2=s
##            mo2=''.join(m)
