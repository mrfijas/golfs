import sys
R=range
X='S'
I=int
_,e,f=sys.argv
def g(n):n^=n<<13;n^=n>>17;n^=n<<5;return n%(1<<30)
def q(p):x,y=p[0];n=p[3]%4;return(x+1if not n else~-x if n==1else x)%8,(y+1if n==2else~-y if n==3else y)%8
z=[[(I(a),I(b)),c,d=='1',I(a)<<2^7*(I(b)<<3)^5,14]for a,b,c,d in f.split(',')]
for i in R(I(e)):
	for p in z:
		a,b,c,d,e=p
		if b==X:p[4]-=1
		if not p[4]:p[1]='R'
		p[3]=g(d)
		if not c and all((q(p)!=o[0]for o in z)):p[0]=q(p)
		(j,k)=p[0]
		if b=='H'and any(u==X and~-j<=o<=j+1and~-k<=e<=-~k for(o,e),u,_,_,_ in z):p[1]=X
for i in R(64):print(next((m[1]for m in z if m[0]==(i%8,I(i/8))),'.'),end=''if i%8!=7else'\n')
