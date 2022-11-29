def linearSearch(arr,value):
   for i in range(len(arr)):
      if(arr[i]==value):
         return i
   return -1
array=[1,2,3,4,5,6,7,8,9,10]
value=5
a=linearSearch(array,value)
if(a==-1):
   print("Element not present")
else:
   print("Element present at index",a)
