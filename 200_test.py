from decimal import *
x = "A"
f = 34.4
c = True
b = 33

value =str(b)

b-b
b+b
b/b
b**2

veo = 'A' +'B'
vop = 'A'*2
voice = 'A' > 'B'
tuples = (1,3,100)
vingo =[1,3,4,5,5]
vingo[0]=1;
vingo[:1]=1;
vingo[2:]=1;
vingo[:-1]=1;
vingo[:-2]=1;

class Program:
    def registertion():
        if(int(input("0 - Sign Up\n1 - Forget Password\nEnter> "))== 0):
            print(" Sign Up ")
            print("-----------------")
            print("Enter Username")
            username = input('your username :')
            print("-----------------")
            print("Password")
            password = input('your password :')
            print("-----------------")
        
        elif(int(input('Forget Password '))== 1):
            password = input('your password :')
            print("Password is Update Succfully!")
        else:
            print("No option below happened!")    
    
        return "Information returned Succfully"
            
    
obj = Program()
obj.registertion()

x= 99 
print("x {}".format(x))
print("x {}".type(x))
print(f'x:{ x }')
x1 = Decimal(.4)

cop= 50//50
cop= 50%50
cop= -50
cop= +50
