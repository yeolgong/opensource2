
#컴퓨터전자시스템공학부 201902520 이상윤
#최대공약수와 최소공배수를 구하는 문제
a,b,c = input().split()
a,b,c = int(a), int(b), int(c)
def gcd(x,y,z):         #최대공약수 구하는 함수
    while x%y !=0:      #x,y의 최대공약수
        temp= x%y
        x = y
        y = temp
    xygys = y           

    while xygys % z !=0:     #x,y의 최대공약수와 z의 최대공약수

        temp= xygys % z
        xygys = z
        z= temp
    xyzgcd=z
    return xyzgcd      
def lcm(x2,y2,z2):      #최소공배수 구하는 함수
    x1=x2
    y1=y2
    z1=z2
    mul1=x2*y2
    while x1%y1 !=0:        #x,y의 최소공배수
        temp= x1%y1
        x1 = y1
        y1 = temp
    xygys = y1
    xygbs=mul1/xygys
    
    mul2=xygbs*z2           #x,y의 최소공배수와 z의 최소공배수
    while xygbs%z1 !=0:
        temp= xygbs%z1
        xygbs=z1
        z1=temp
    midgys2=z1
    xyzlcm=mul2/midgys2
    
    return xyzlcm
    
print("%d %d" %(gcd(a,b,c) ,lcm(a,b,c)))

    
