list1=["Black","Maroon","Red","Yellow"] 
list2=["#000000","#FF0000","#800000","FFFF00"]
new_list=[]
for i in range(len(list1)):
    dict={
        "color_name": list1[i],
        "color_code": list2[i]
    }
    new_list.append(dict)
print(new_list)