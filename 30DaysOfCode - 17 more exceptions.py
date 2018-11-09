class Calculator:
    @staticmethod  # static method 
    def power(n, p):
        if n < 0 or p < 0:
            raise ValueError('n and p should be non-negative') # raising ValueError exception
        return n ** p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
