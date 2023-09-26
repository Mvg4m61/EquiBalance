def equilibrium():
    l1 = []
    n = int(input("\nEnter number of elements: "))
    for i in range(n):
        num = int(input("Enter number: "))
        l1.append(num)
    sum1 = 0
    sum2 = 0
    i = 1
    flag = 0
    pos = 0
    ele = 0
    fin = 0
    while(i<n-1):
        if i>n-i-1:
            flag = 1
            break
        for j in range(0,i):
            sum1 = sum1 + l1[j]
        j = i+1
        while(j<n and sum2<sum1):
            sum2 = sum2 +l1[j]
            j+=1
        else:
            if sum2==sum1 and j==n:
                flag = 0
                pos = i
                ele = l1[i]
                fin = sum1
                break
            else:
                sum1 = 0
                sum2 = 0
                flag = 1
                i+=1
                
    if flag==0:
        print("\nFirst equilibrium traversed is ",ele," at position ",pos+1," with sum: ",fin)
    else:
        print("\nNo equilibrium exists.")
equilibrium()