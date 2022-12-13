def csum(s):
   sm=0
   cum_list=[]
   for i in s:
      sm=sm+i
      cum_list.append(sm)
   return cum_list

a=[1,2,3,4,5]
print(csum(a))
