def sort(arr):
    count_0=arr.count(0)#declare 3 variables count_0,count_1,count_2
    count_1=arr.count(1)
    count_2=arr.count(2)
    #using count func it will print the nos of 0,1,2 and store in count_0,count_1,count_2
    #print an empty array to print new array after sorting
    new_arr=[]

    #append 0 to new array 
    for i in range(count_0):
        new_arr.append(0)
    #append 1 to new array
    for i in range(count_1):
        new_arr.append(1)
    #append 2 to new array
    for i in range(count_2):
        new_arr.append(2)
    print("After Coding",new_arr)
array=[0,1,2,1,0,2,1,0]
print("Before sorting",array)
sort(array)
        