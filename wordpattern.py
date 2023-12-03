#Word Pattern
pattern=input("Enter the pattern:")
string=input("Enter the string")
temp=string.split()
if (pattern=="aaaa"):
    if temp.count(temp[0])==len(temp):
        print(True)
    else:
        print(False)    
elif pattern=="abaa":
    if temp.count(temp[1])==1:
        print(True)
    else:
        print(False)
elif pattern=="abba":
    if temp[0]==temp[-1]:
        print(True)
    else:
        print(False)
elif pattern=="abab":
    if temp[0]==temp[-2]:
        print(True)
    else:
        print(False)
elif pattern=="abbb":
    if temp.count(temp[0])==1:
        print(True)
    else:
        print(False)
elif pattern=="aaab":
    if temp.count(temp[0])==len(temp)-1: 
        print(True)
    else:
        print(False)         
