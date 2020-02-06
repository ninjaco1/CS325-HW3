current_line = 0
file = open("shopping.txt","r")
lines = file.readlines()#reads all the lines in the file
file.close()

test_cases = [int(i) for i in lines[0].split() if i.isdigit()] # number of test cases
current_line+=1
print(current_line)
#for cases in range(test_cases[0]):

print (test_cases)

print (lines)
