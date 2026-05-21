profit=[5,10,15,7,8,9,4]
weight=[1,3,5,4,1,3,2]
capacity=15
n=7 #no. of items
def sort(profit,weight,n):
    k=[]#p/w ratio
    for i in range(n):
        k.append(profit[i]/weight[i])
    for i in range(n):
        for j in range(n-i-1):
            if k[j]<k[j+1]: #p/w in non decreasing order
                
                temp1=k[j]
                k[j]=k[j+1]
                k[j+1]=temp1

                temp2=profit[j]
                profit[j]=profit[j+1]
                profit[j+1]=temp2

                temp3=weight[j]
                weight[j]=weight[j+1]
                weight[j+1]=temp3

def knapsack_cal(profit,weight,n):
    x=[]
    remaining_capacity=capacity
    val=0
    for i in range(n):
        if weight[i]<=remaining_capacity:
            x.append(1)
            remaining_capacity-=weight[i]
            val+=profit[i]
        elif weight[i]>remaining_capacity and remaining_capacity>0:
            x.append(remainign_capacitycapacity/weight[i])
            remainign_capacitycapacity=0
            val+=(profit[i]/weight[i])*remaining_capacity
        else:
            x.append(0)
    print("Selection of items:",x)
    print("Max Profit=",val)
sort(profit,weight,n) #p/w decreasing order
knapsack_cal(profit,weight,n)
