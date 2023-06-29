class Solution:
    def hn(self, n):
        a=0
        for i in str(n):
            a+=int(i)**2
        if len(str(a))>1:
            return self.hn(a)
        return a
    
    def nextHappy (self, n):
        # code here
            if self.hn(n+1) in [1,7]:
                return n+1
            return self.nextHappy(n+1)

if __name__ == '__main__': 
    N=1
    A=[]
    while N<5000:
        ob = Solution()
        A.append(ob.nextHappy(N))
        N=ob.nextHappy(N)
    print(A)
