def myfucn(mylist):
    ctr=0
    mylist1=[]
    for item in mylist:
        if len(item)>1 and item[0]==item[-1]:
            ctr+=1
            mylist1.append(item)
    print("listbof words with first and last charecter same\n",mylist1)
    return ctr

count=myfucn(['aba','boda','hfdgddghg','jhjsjfdagSsfsfdsgsdarwagj','hiihihihihihihiiihih'])  
print("no of word having first and last charecter same:--",count)      



