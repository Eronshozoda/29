dict1={"Ten":10,"Twenty":20,"Thirty":30}
dict2={"Thirty":30,"Fourty":40,"Fifty":50}
for i in dict2.keys():
    dict1[i]=dict2[i]
print(dict1)
