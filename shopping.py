class Data(object):
    def __init__(self,N,val,wt,family_members,max_wt):
        self.N=N
        self.val = val
        self.wt = wt
        self.family_members = family_members
        self.max_wt = max_wt

    def list_values(self):
        print("N=%s" % self.N)
        print("val=%s" % self.val)
        print("wt=%s" % self.wt)
        print("fm=%s" % self.family_members)
        print("max_wt=%s" % self.max_wt)
        print("")


file = open("shopping.txt","r")
lines = file.readlines()#reads all the lines in the file
file.close()

test = []# class of data
def create_class():
    current_line = 0
    test_cases = [int(i) for i in lines[0].split() if i.isdigit()] # number of test cases
    current_line+=1
    #print(current_line)
    for cases in range(test_cases[0]):
        temp = [int(i) for i in lines[current_line].split() if i.isdigit()]
        N = temp[0]
        current_line+=1
        #PW= []
        val = [] #price
        wt = [] #weight
        for i in range(N):
            PW=[int(i) for i in lines[current_line].split() if i.isdigit()]# price, weight
            val.insert(0,PW[0])
            wt.insert(0,PW[1])
            current_line+=1
        temp = [int(i) for i in lines[current_line].split() if i.isdigit()]
        family_members = temp[0]
        current_line+=1
        max_wt = []
        for members in range(family_members):
            temp = [int(i) for i in lines[current_line].split() if i.isdigit()]
            max_wt.append(temp[0])
            current_line+=1
        test.append(Data(N,val,wt,family_members,max_wt))

        print(val)
        print(wt)
    print ("test_cases = %s"%(test_cases))



def main():
    create_class()
    test[0].list_values()
    test[1].list_values()
    test[2].list_values()
    test[3].list_values()




main()
