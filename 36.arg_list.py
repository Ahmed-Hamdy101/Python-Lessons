#function -- looping through args  with astrict 
def main():
    voice("Meow.....","woof","OOOOOW")
    
def voice(*v):
    if len(v):
        for i in v:
            print(i)
    else:
        print("single line...")
       

# main function that execute the code and note also we can import this code inside a file
if __name__== '__main__':main()