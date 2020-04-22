import sys
R=range
X='S'
I=int
_,e,f=sys.argv
z=[[(I(a),I(b)),c,d=='1',I(a)<<2^7*(I(b)<<3)^5,14]for a,b,c,d in f.split(',')]
for i in R(I(e)):
	for p in z:
		a,b,c,d,e=p
		if b==X:p[4]-=1
		if not p[4]:p[1]='R'
		d^=d<<13;d^=d>>17;d^=d<<5;p[3]=d%(1<<30);x,y=a;n=p[3]%4;f=(x+1if not n else~-x if n==1else x)%8,(y+1if n==2else~-y if n==3else y)%8
		if not c and all((f!=o[0]for o in z)):p[0]=f
		(j,k)=f
		if b=='H'and any(u==X and~-j<=o<=j+1and~-k<=e<=-~k for(o,e),u,*_ in z):p[1]=X
for i in R(64):print(next((m[1]for m in z if m[0]==(i%8,I(i/8))),'.'),end=['','\n'][i%8==7])
