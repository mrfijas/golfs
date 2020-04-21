from sys import argv
R=range
X='S'
I=int
_,e,f=argv
def g(n):n^=n<<13;n^=n>>17;n^=n<<5;return n%(1<<30)
def q(p):B,C=p[0];A=p[3]%4;return(B+1 if not A else~(-B)if A==1 else B)%8,(C+1 if A==2 else~(-C)if A==3 else C)%8
z=[[(I(A),I(B)),C,D=='1',I(A)<<2^7*(I(B)<<3)^5,14]for(A,B,C,D)in f.split(',')]
for i in R(I(e)):
	for p in z:
		a,b,c,d,e=p
		if b==X:p[4]-=1
		if not e:p[1]='R'
		p[3]=g(d)
		if not c and all((q(p)!=A[0]for A in z)):p[0]=q(p)
		j=a
		if b=='H'and any((C==X and~(-j[0])<=A[0]<=-(~ j[0])and~(-j[1])<=A[1]<=-(~ j[1])for(A,C,B,B,B)in z)):p[1]=X
for i in R(64):print(next((A[1]for A in z if A[0]==(i%8,I(i/8))),'.'),end=''if i%8!=7 else'\n')
