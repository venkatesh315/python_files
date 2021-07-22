if __name__ == '__main__':
    print("Enter the elements")
    arr=list(map(int,input().split()))
    ans=[0]*len(arr)
    mx=max(arr)
    freq=[0]* (mx+1)
    for ele in arr:
        if freq[ele] == 0:
            freq[ele] = arr.count(ele)
    for i in range(1,len(freq)):
        freq[i]+=freq[i-1]

    for j in range(len(arr)-1,-1,-1):
        num=arr[j]
        freq[num]-=1
        pos=freq[num]
        ans[pos]=num
    print("Input list: ",arr)
    print("Sorted list: ",ans)


