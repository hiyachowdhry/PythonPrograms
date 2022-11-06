t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)
#1
even_t=()
for i in t1:
    if i%2==0:
        even_t+=(i,)
#2
conc=t1+t2

#3
maxval=max(conc)
minval=min(conc)

print("Original Tuple is: ", t1)
print("Tuple with only even values is: ",even_t)
print("Concatenated Tuple: ",conc)
print("Min Value: ",minval)
print("Max Value: ",maxval)
        
