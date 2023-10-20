
try:
    f=open("D:\\python\\CodeBytes\\one.txt",'r')
    f1=f.read().split()
    k=[]
    k=f1.copy()

    word_counts={}
    for i in k:
        word_counts[i]=word_counts.get(i,0)+1
    for item,val in word_counts.items():
        print(item ,":", val)
except Exception as e:
    print (e)


