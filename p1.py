import numpy as np

# print(np.__version__)

# list1=[12,23,22,23,2,45,5,6,5,4,8,565]
# tuple1=(65,5,6,78,89,8,9,45,12)
# arr1=np.array(list1)
# arr2=np.array(tuple1)
# print(list1)
# print(tuple1)
# print(arr1)
# print(arr2)
# list2=[[1,2,3,4],[4,5,6,5],[7,8,9,78]]
# arr4=np.array(list2)
# print(arr4)
# list3=[[[1,2,3],[7,8,9],[9,8,7]],[[1,2,3],[7,8,9],[9,8,7]]]
# arr4=np.array(list3)
# print(arr4)

# list1=[12,23,22,23,2,45,5,6,5,4,8,565]
# list2=[[1,2,3,4],[4,5,6,5],[7,8,9,78]]
# list3=[[[1,2,3],[7,8,9],[9,8,7]],[[1,2,3],[7,8,9],[9,8,7]]]

# print(len(list1))
# arr7=np.array(list1)
# arr8=np.array(list2)
# arr9=np.array(list3)
# # print(100*'-')
# print(arr7)
# print(100*'-')
# print(arr8)
# print(100*'-')
# print(arr9)
# print(100*'-')

# print(arr7.ndim)
# print(arr7.ndim)
# print(arr7.ndim)
# print(list1[3])
# print(arr7[3])

# find  index
# print(list3[1][1][2])
# print(arr9[1][1][2])


# print(arr8[1,3])
# print(arr9[1,2,2]) 
# print(arr7[-6])



#==============================================================
# list1=[12,23,22,23,2,45,5,6,5,4,8,565]
# list2=[[1,2,3,4],[4,5,6,5],[7,8,9,78]]
# list3=[[[1,2,3],[7,8,9],[9,8,7]],[[1,2,3],[7,8,9],[9,8,7]]]

# arr1=np.array(list1)
# arr2=np.array(list2)
# arr3=np.array(list3)
#slice
# print(arr1[1:5])
# print(arr2[1,1:3])
# print(arr2[:2,1:3])

# print(arr3[0,1:,1:])

 

#DataType



# list1=[12,23,22,23,2,45,5,6,5,4,8,565]
# list4=[12.5,385.78,12.5]
# list2=['andy','George']
# list3=[True,False,True]

# arr1=np.array(list1)
# arr2=np.array(list2)
# arr3=np.array(list3)
# arr4=np.array(list4)

# print(arr1.dtype)
# print(arr2.dtype)
# print(arr3.dtype)
# print(arr4.dtype)
# newArr1=arr1.astype('U5')
#To change to  string  U5  is a string
# print(newArr1)

# newArr4=arr4.astype('i')  
#convert to  integer,('f)=float,b=boolean


# print(newArr4)


# arr1=np.array([12,5,4,45,58,9,8,7])
# arry2=arr1.copy()
# arr1[0]=55
# print(arr1)
# print(arry2)

# arr1=np.array([12,5,4,45,58,9,8,7])
# arry2=arr1.view()
# arr1[0]=55
# print(arr1)
# print(arry2)



# list1=[12,23,22,23,2,45,5,6,5,4,8,565]
# list2=[[1,2,3,4],[4,5,6,5],[7,8,9,78]]
# list3=[[[1,2,3],[7,8,9],[9,8,7]],[[1,2,3],[7,8,9],[9,8,7]]]

# arr1=np.array(list1)
# arr2=np.array(list2)
# arr3=np.array(list3)
# print(arr1.ndim)
# print(arr2.ndim)

# print(arr1.shape)
# print(arr2.shape)
# print(arr3.shape)

# print(arr1.reshape(3,4))
# print(arr2.reshape(12))
# print(arr3.reshape(2,9))

# print(arr2.reshape(-1)) 
# To delete one Dimenstion -1


#Iterable in Numpy 


# for item in arr2:
#     print(item)

# list2=[[1,2,3,4],[4,5,6,5],[7,8,9,78]]
# for row in arr2:
#     for col in row:
#         print(col,end='\t')
#     print()


#To join tow array together
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([10,20,30,40,50])
# arr3=np.concatenate((arr1,arr2)) # must add one tuple to it 
# print(arr3)


#To join Two dimenstion array


# arr1=np.array([[1,2,3],[4,5,6]])
# arr2=np.array([[13,25,3],[10,51,68]])
# arr3=np.concatenate((arr1,arr2))


# arr3=np.stack((arr1,arr2))
# print(arr3)


# arr3=np.concatenate((arr1,arr2),axis=1)
# print(arr3)
# print(arr3.shape)


#================================================
# arr1=np.array([12,23,22,23,2,45,5,6,5,4,8,565])
# print(np.array_split(arr1,3))


# list1=[12,23,22,23,2,45,5,6,5,4,8,565]
# list2=[[1,2,3,4],[4,5,6,5],[7,8,9,78]]
# list3=[[[1,2,3],[7,8,9],[9,8,7]],[[1,2,3],[7,8,9],[9,8,7]]]




# arr2=np.array([[1,2,3,4],[4,5,6,5],[7,8,9,78]])

# newArr2=np.array_split(arr2,3)
# print(newArr2[0])
# print(newArr2[1])
# print(newArr2[2])


#search and  manage


# list1=[12,23,22,23,2,45,5,6,5,4,8,565]
# list2=[[1,2,3,4],[4,5,6,5],[7,8,9,78]]
# list3=[[[1,2,3],[7,8,9],[9,8,7]],[[1,2,3],[7,8,9],[9,8,7]]]

# arr1=np.array([12,23,22,23,2,45,5,6,5,4,8,565])
# list2=[[1,2,3,4],[4,5,6,5],[7,8,9,78]]
# list3=[[[1,2,3],[7,8,9],[9,8,7]],[[1,2,3],[7,8,9],[9,8,7]]]
# arr4=np.array([2,5,6,8,9,12,23,56,89])

# x=np.where(arr1%2==0)
# x=np.where(arr1==23)

# x=np.searchsorted(arr4,8)
# x=np.searchsorted(arr4,8,side='right')
#array must be in normal number from small to big
# print(x)


# arr1=np.array([12,23,22,23,2,45,5,6,5,4,8,565])
# list2=[[1,2,3,4],[4,5,6,5],[7,8,9,78]]
# list3=[[[1,2,3],[7,8,9],[9,8,7]],[[1,2,3],[7,8,9],[9,8,7]]]
# arr4=np.array([2,5,6,8,9,12,23,56,89])

# print(np.sort(arr1))

# filter ++++++++++++++++++++++++++++++++++++++++


# arr1=np.array([12,45,5,8,565])
# listfilter=[True,True,False,False,True]
# print(arr1[listfilter])


# arr1=np.array([12,45,5,8,565])

# listfilter=[]
# for item in arr1:
#     if item %2==0:
#         listfilter.append(True)
#     else:
#         listfilter.append(False)    
# # print(listfilter)
# print(arr1[listfilter])




# arr1=np.array([12,45,5,8,565])

# listFilter=arr1 % 2==1
# print(listFilter)
# print(arr1[listFilter])


# listFilter=arr1>20
# print(arr1[listFilter])

#==============================PART 4===============================
from numpy import random
#rand function produces random numbers between 0 and 1 , 5 times
x=random.rand(5) 
print(x)
























































































