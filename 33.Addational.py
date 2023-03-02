secret = "gen"
pw = ''
attemps = 3
auth = False
count =  0
while(pw!=secret):
    count+=1
    if count > attemps:break
    if count ==2:continue
    pw = input(f'{count}:Enter who :')
    if count == 3:
        print("you have typed 3 times .")
else:
    auth = True
print("Authorized" if auth else "calling police.....")