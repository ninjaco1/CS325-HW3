class Data(object):
    def __init__(self,N,val,wt,family_members,max_wt):
        self.N=N #number of items
        self.val = val # price
        self.wt = wt # weight
        self.family_members = family_members # number of members
        self.max_wt = max_wt # each family member max weight
        self.price = 0
        self.member_price =[]#each family member price
        self.item_used =[] #0/1 knapsack
        self.format = ""

    def run(self):
        self.family_price()
        #self.list_values()
        self.formatting()

    def list_values(self):
        print("N=%s" % self.N)
        print("val=%s" % self.val)
        print("wt=%s" % self.wt)
        print("fm=%s" % self.family_members)
        print("max_wt=%s" % self.max_wt)
        print("member_price= %s"% self.member_price)
        print("item_used=%s"%self.item_used)
        print("total price=%s"%self.price)
        print("")

    def family_price(self):
        for member in range(self.family_members):
            W = self.max_wt[member]
            price,items = self.shopping_max(W,self.N)
            self.member_price.append(price)
            self.item_used.append(items)
            self.price += price

    def formatting(self):
        #print test cases outside of function
        format ="Total Price %s\nMember Items: \n" % (self.price)
        #print("Total Price %s\nMember Items: \n" % (self.price))
        #take out all 0s
        for member in range(self.family_members):
            string_items = ""
            for number in self.item_used[member]:
                #adds item to string
                if number !=0:
                    string_items += str(number) + " "
            format += "%s: %s \n"%(member+1,string_items)
            #print("%s: %s "%(member+1,string_items))
        format +="\n"
        self.format = format
        print(self.format)

    def shopping_max(self,W,N):
        V = [[-1 for w in range(W+1)] for i in range(N+1)]
        item_used = [-1]*N
        for w in range(W+1):
            V[0][w]=0
        for i in range(1,N+1):
            V[i][0]=0

        for i in range(1,N+1):
            # for y in range(n+1): # display the rows
            #     print (V[y])
            for w in range(1,W+1):# creating the table
                #V[i][w] = max(V[i-1][w], V[i-1][w-wt[i-1]] + val[i-1])
                check_index = w-self.wt[i-1]
                if check_index >= 0:
                    V[i][w] = max(V[i-1][w], V[i-1][w-self.wt[i-1]] + self.val[i-1])
                else:
                    V[i][w] = V[i-1][w]

                #print (check_index)

        # for i in range(n+1): # display the rows
        #     print (V[i])

                #find the item used
        max_price = temp = V[N][W]
        for i in range(N,0,-1):
            #if V[n-1][W-1] != V[n-1][W-1]
            #print(i)
            if temp not in V[i-1]:
                #print("temp = %s"%temp)
                item_used[i-1] = i
                temp -= self.val[i-1]
            else:
                #continue
                item_used[i-1] = 0

        #print(max_price)
        #print (item_used)
        return max_price, item_used


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
            # val.insert(0,PW[0])
            # wt.insert(0,PW[1])
            val.append(PW[0])
            wt.append(PW[1])
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

        #print(val)
        #print(wt)
    print ("test_cases = %s"%(test_cases))



def main():
    create_class()
    results = open("results.txt", "w")
    results.truncate(0)
    for i in range(len(test)):
        test[i].run()
        results.write(test[i].format)

    results.close()



main()
