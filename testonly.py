import os

folder = os.getcwd()
check_folder = folder + "\\cruds"
print(check_folder)
listName = os.listdir(check_folder)
print(listName)
for idx in listName:
    print(idx)
    if idx.__contains__("CRUD"):
        print(idx)
        new_name = idx.replace("CRUD","Crud")
        print(new_name)
        os.rename(check_folder+"\\"+idx,check_folder+"\\"+new_name)