#def filter_list(l):
l=[1,2,'aasf','1','123',123],[1,2,123]
filtered_list = []
for i in l:
    for a in i:
        comprovacio = isinstance(a,int)
        if comprovacio:
            filtered_list.append(a)
print(filtered_list)

