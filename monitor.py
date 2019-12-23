import graph
import os

arr = os.listdir('data/.')

print ("client list\n")
l=1
for i in arr:
	print(str(l)+" "+i)
	l+=1

print("\nselect a client?")
x=0;
x=int(input())
print(str(arr[x-1])) 

graph.graphplot(str(arr[x-1]))