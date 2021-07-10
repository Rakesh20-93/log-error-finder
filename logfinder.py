content= True
i=1

with open("logfile.txt") as f:
    while content:                 # while content in file then program will run
        content  = f.readline()     # to read lines
        if "python" in content.lower():    # lower is used to see all words in lower case in file
            print(content)
            print(f"python is present in line number {i}") 
        i+=1       # i will count to lines where content will be avilable