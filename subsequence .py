def main():
    result=[]
    def subsec(bi, v, m, n):

        if m == 0:
            return True
        if n == 0:
            return False
        if bi[m-1] == v[n-1]:
            return subsec(bi, v, m-1, n-1)
     
        # If last characters are not matching
        return subsec(bi, v, m, n-1)
    v=input()
    n=int(input())


    for p in range(n):
        
        bi=input()
        if subsec(bi, v, len(bi), len(v)):
            result.append("POSITIVE")
        else:
            result.append("NEGATIVE")
            
    for p in range(n):
        print(result[p])
    
main()

