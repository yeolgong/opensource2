
#컴퓨터전자시스템공학부 201902520 이상윤
a,b,c = input().split()
a,b,c = int(a), int(b), int(c)
mul1=a*b   #a와b의 값이 변하기 전에 곱한값을 구해놓음
a1=a			 #아래에서 값이 변하므로 미리 지정
b1=b
c2=c

while a1%b1 != 0:
	temp = a1%b1
	a1 = b1
	b1 = temp
midgys1=b1                    #유클리드 알고리즘을 이용하여 a와b의 최대공약수를 구함 midbys1로 저장.

midgbs1=mul1/midgys1          #유클리드 알고리즘으로 a와b의 최소공배수는 a*b의값에 최대공약수를 나눠주면 됨

mul2=midgbs1*c                #a와b의 최대공약수와 c의 최대공약수 구하는 알고리즘
while midgys1 % c!=0:
	temp = midgys1 % c
	midgys1 = c
	c=temp                     
gys=c
while midgbs1 %c2 !=0:		#a와b의 최소공배수와 c의 최소공배수 구하는 알고리즘(위의 c값이 바꼇으므로 다른 c2로 대체)
	temp = midgbs1 % c2
	midgbs1=c2
	c2=temp
midgys2=c2
gbs=mul2/midgys2

print("%d %d" %(gys,gbs)) 

