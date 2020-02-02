#merge.py
f=open("C:\\Users\\lego0\\OneDrive\\바탕 화면\\merge\\merge.txt",'r')
while True:
    line=f.readline()
    if not line: break;
    print(line)
    array=line.split(" ")
f.close

def merge(lst1,lst2):
    i=0
    j=0
    lst=[]
    for k in range(0,2*len(lst1)):
        if (i==(len(lst1))):
            lst.append(lst2[j])
            j=j+1
        elif(j==(len(lst1))):
            lst.append(lst1[i])
            i=i+1
        elif (lst1[i]>lst2[j]):
            lst.append(lst2[j])
            j=j+1
        elif (lst1[i]<lst2[j]):
            lst.append(lst1[i])
            i=i+1
    return lst

print(len(array)/2)
print(array)
list = []
half=int(len(array)/2)
print(type(half))
for i in range(0,len(array)):
    if (i % 2==0):
        list.append([array[i],array[i+1]])

for i in range(0,len(list)):
    if list[i][0]>list[i][1]:
        list[i][0],list[i][1]=list[i][1],list[i][0]

for i in range(0,len(list)):
    print(list[i])

i=0
length=int(length/2)
while 1:
    if length==1:
        break
    else:
        for k in range(i,i+length-1):
            if k%2==0:
                list.append(merge(list[k],list[k+1]))
        i=i+length
        length=int(length/2)
        print(i)
print(list[i])
