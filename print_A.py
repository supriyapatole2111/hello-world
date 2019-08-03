def A(n):
    for i in range(n):
        for j in range((n // 2) + 1):
            if (i==0 or i==n//2)and (j!=0 and j!=n//2):
                print("*",end=" ")
            elif(j==0 or j==n//2)and(i!=0):
                print("*",end=" ")
            else:
                print(end="  ")
          
        print() 
      
def M(n):
    for i in range(n):
        for j in range(n+1):
            if(i==j and i<=n//2):
                print("*",end="")
            elif(j==n//2+1 and i==n//2-1):
                print("*",end="")
            elif(j==n//2+2 and i==n//2-2):
                print("*",end="")
            elif(j==n//2+3 and i==n//2-3):
                print("*",end="")
            elif j==0 or j==n and i!=0:
                print("*",end="")
            else:
                print(end=" ")
                
        print()

def O(n):
    for i in range(n):
        for j in range(n//2+1):
            if(i!=0 and j==0):
                print("*",end=" ")
            elif(i==0 and j!=0):
                print("*",end=" ")
            elif(j==n//2 and i!=0):
                print("*",end="")
            elif(i==n-1 and j!=0 and j!=n//2):
                print("*",end=" ")
            elif(i==0 and j==0):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def L(n):
    for i in range(n):
        for j in range(n//2+1):
            if(i==n-1 or j==0):
                print("*",end=" ")
            else:
                print(end="")
        print()



print(A(7))
print(M(7))
print(O(7))
print(L(7))
