a = int(input("enter number1 :"))
a2 = int(input("enter number2  :"))
a3 = int(input("enter number3 :"))


if a>a2 and a2>a3 :
    bozorg=a
elif a2>a and a2>a3 :
    bozorg=a2  
elif a3>a and a3>a2 :  
   bozorg=a3
if a<a2 and a<a3 :
    small=a
elif a2<a and a2<a3 :
    small=a2
else :
    small=a3
if bozorg>a and a>small :
    mid=a
elif bozorg>a2 and a2>small :
    mid=a2
else :
    mid=a3

          

print(str(bozorg)+">"+str(mid)+">"+str(small) )    
      