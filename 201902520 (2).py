a=int(input())		
count=0

for i in range(1,a+1):  #입력받은 자연수 (a+1미만 range)=a와 같가나 작은 함수 구현 
	num=0									
	for j in range(1,i): #약수는 나머지가 0이되는 수를 구하는 방법으로 찾음. 자연수는 자기자신 제외 약수의 합이기 때문에 range(1,x)
		if i % j==0:
			num=num+j
	if num==i:              #약수의 합이 정수자신과  같은지 알아냄.
		count=count+1

print("%d" %(count))
