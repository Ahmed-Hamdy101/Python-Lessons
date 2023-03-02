#function 
def main():
    voice("Meow.....")
    # another Core Value What if i want a value that's inside vaiables returning from func
    p=voice("Meow.....")
    print(p)
def voice(v):
    if v == "woofff":
        print("it's dog....")
    else:
        print("it's animal")
    return "value in variable"    

# main function that execute the code and note also we can import this code inside a file
if __name__== '__main__':main()