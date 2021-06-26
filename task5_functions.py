######FUNCTIONS in Python#######

print("please enter your input string")
x=str(input())

def most_frequent(x):        #function definition
   i=0
   while i!=len(str(x)):
     print(x[i])              #prints alla the characters in a string
     i=i+1
   print("sorted frequency in decreasing order is: ")
   freq=dict()                 
   for keys in x:
     freq[keys]=freq.get(keys,0)+1
     sort_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)    #sort the letters in descending order
  
   return sort_freq
 
print("output is: ")
print(most_frequent(x))          #function call

