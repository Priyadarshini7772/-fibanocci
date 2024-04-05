def fibo(n):
    if n<=0:
        return None
    
    else:
        a=0
        b=1
        print(a)
        print(b)
        for i in range(n-2):
            c=a+b
            print(c)
            a,b=b,c

def fiborecur(n):
    series=[0,1]
    for i in range(2,n):
        series.append(series[i-1]+series[i-2])
    return series



n=int(input('Enter the no.of terms of fibanocci series you want: '))
fibo(n)
print("Or")
print(fiborecur(n))


