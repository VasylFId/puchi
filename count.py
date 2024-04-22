a = True
b = 0
c  = [5]
l = len(c)
while a:
    if b%2 == 0 or b%3 == 0 :
       b=b
    else :
            e = 0
            for i in c:
                if(b%i>0 and b!=1):
                    e=e+1
            if e ==  len(c) :
                print(b)
                c.append(b)
    b=b+1
    
    print("count" , b)
    for y in c:
        print(y)
         
