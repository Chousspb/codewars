def find_outlier(integers):
    even=[]
    odd=[]
    for i in integers:
        if i%2 > 0:
            odd.append(i)
        if i%2==0:
            even.append(i)
    if len(even) > len(odd):
        return odd[0]
    else:
        return even[0]