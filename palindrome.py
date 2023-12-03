x=input("Enter the string :")
n=x[::-1]
flag=0
if(x==n):
    print("String is palindrome")
    quit
else:
   for i in range(len(x)-1,0,-1):
       if(x[0]==x[i]):
           y=i
           n=x[:y+1:]
           m=x[y::-1]   
           if (n==m):
               palin=x[-1:y:-1]+x 
               flag=1
               break
if(flag==0):
    palin=x[-1:0:-1]+x
print("the new palindrone string is ",palin)


       
   
        
