import time
import random

file = open("time_r_dp.txt","w")
file.truncate(0)

def main():
    val = random.sample(range(1,100), 50)
    val.sort()
    wt =  random.sample(range(1,51), 50)
    wt.sort()

    # val = [3,4,5,15,16] # values
    # wt = [2,3,4,5,10] # weights
    n = len(wt)
    W = 100 # max capacity

    #print("weights = " + str(wt))
    #print("val =     " + str(val))
    #total = knapsack(W,n,val,wt)
    #print ("value = " + str(total))

    for i in range(10,n,10):
        #print(i)
        run_time(W,i,val,wt)
    #DP_knapsack(W,n,val,wt)
    #max is the max value
    #print weight


def run_time(W,n,val,wt):
    max_r, time_r= recursive_time(W,n,val,wt)
    max_dp, knapsack0_1, time_dp = DP_time(W,n,val,wt)
    print("N=%s W=%s  Rec time = %s DP time = %s max Rec = %s max DP = %s" % (n,W,time_r,time_dp,max_r,max_dp))

    data = "%s %s %s\n" %(n,time_r,time_dp)
    file.write(data)

def recursive_time(W,n,val,wt):
    start_time = time.time()
    max_r = knapsack(W,n,val,wt)
    end_time = time.time() - start_time
    return max_r, end_time

def DP_time(W,n,val,wt):
    start_time = time.time()
    max_dp, knapsack0_1 = DP_knapsack(W,n,val,wt)
    end_time = time.time() - start_time
    return max_dp, knapsack0_1, end_time


def knapsack(W,n,val,wt): #recursive
    # W is capacity
    # n elements
    #base case
    if n==0 or W == 0:
        return 0

    if wt[n-1] > W:
        return knapsack(W,n-1,val,wt)

    else:
        return max(val[n-1] + knapsack(W-wt[n-1],n-1,val,wt), knapsack(W,n-1,val,wt))

def DP_knapsack(W,n,val,wt):
    #n = n+1
    #print ("W= %s n=%s"%(W,n))
    V = [[-1 for w in range(W+1)] for i in range(n+1)]
    weight_used = [-1]*n
    for w in range(W+1):
        V[0][w]=0
    for i in range(1,n+1):
        V[i][0]=0

    for i in range(1,n+1):
        # for y in range(n+1): # display the rows
        #     print (V[y])
        for w in range(1,W+1):# creating the table
            #V[i][w] = max(V[i-1][w], V[i-1][w-wt[i-1]] + val[i-1])
            check_index = w-wt[i-1]
            if check_index >= 0:
                V[i][w] = max(V[i-1][w], V[i-1][w-wt[i-1]] + val[i-1])
            else:
                V[i][w] = V[i-1][w]

            #print (check_index)

    # for i in range(n+1): # display the rows
    #     print (V[i])

    #find the weighted used
    max_dp = temp = V[n][W]
    for i in range(n,0,-1):
        #if V[n-1][W-1] != V[n-1][W-1]
        #print(i)
        if temp not in V[i-1]:
            #print("temp = %s"%temp)
            weight_used[i-1] = 1
            temp -= val[i-1]
        else:
            weight_used[i-1] = 0

    #print(max_dp)
    #print (weight_used)
    return max_dp, weight_used



main()
file.close()
