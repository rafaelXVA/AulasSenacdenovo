jan=[30,31]
feb=[32,33]
mar=[34,35]
apr=[36,37]
may=[29,28]
jun=[27,26]
jul=[25,24]
aug=[23,22]
sep=[21,20]
oct=[19,18]
nov=[17,16]
dec=[15,14]
list=[]
list.extend(jan)
list.extend(feb)
list.extend(mar)
list.extend(apr)
list.extend(may)
list.extend(jun)
list.extend(jul)
list.extend(aug)
list.extend(sep)
list.extend(oct)
list.extend(nov)
list.extend(dec)
list.sort()
average=sum(list)/len(list)
print("ordem crescente: ",list)
list.sort(reverse=True)
print("ordem decrescente: ",list)
print("menor temperatura: ",list[-1])
print("maior temperatura: ",list[0])
print("média de temperatura: ",average)