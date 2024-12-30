

matrix = []

filename = open(r"\\ug.kth.se\dfs\home\p\e\peries\appdata\xp.V2\Documents\GitHub\Test_scripts\New_files\trail_number.txt", "r")  #this opens it for reading mode 

for lines in range(-1,10): 

    test = filename.readline()
    matrix.append(test)

    print (matrix)