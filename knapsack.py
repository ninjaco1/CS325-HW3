
# class Knapsack(object):
#     def __init__(self,val,wt):
#         self.val = val
#         self.wt = wt
#         self.n = len(wt) - 1
#
#     def knapsack(W,n): #recursive
#         # W is capacity
#         # n elements
#         #base case
#         if n==0 or W == 0:
#             return 0
#
#         if wt[n] > W:
#             return knapsack(W,n-1,val,wt)
#
#         else:
#             return max(val[n] + knapsack(W-wt[n],n-1,val,wt), knapsack(W,n-1,val,wt))


def main():
    val = [3,4,5,15,16] # values
    wt = [2,3,4,5,10] # weights
    n = len(wt)-1
    W = 13 # max capacity
    weight_used = []
    print("weights = " + str(wt))
    print("val =     " + str(val))
    total = knapsack(W,n,val,wt)
    print ("value = " + str(total))
    #print("N=%s W=%s  Rec time = %s DP time = %s max Rec = %s max DP = %s" % (n,W))
    #print weight


def knapsack(W,n,val,wt): #recursive
    # W is capacity
    # n elements
    #base case
    if n==0 or W == 0:
        return 0

    if wt[n] > W:
        return knapsack(W,n-1,val,wt)

    else:
        return max(val[n] + knapsack(W-wt[n],n-1,val,wt), knapsack(W,n-1,val,wt))


main()
