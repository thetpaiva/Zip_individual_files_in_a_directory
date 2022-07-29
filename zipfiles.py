import zipfile
from os import listdir
from os.path import isfile, join

#Function for creating a zip file, with the same name of the original file
def zip(file_name, file_type, path):
    with zipfile.ZipFile(path + '/' + file_name + '.zip', 'w') as my_zip:
        my_zip.write(file_name + '.' + file_type)
        
#input
path = input('Insert folder path (ex: /mnt/c/Users/tiago/OneDrive/Área de Trabalho/Pasta teste):\n') 
file_type = input("Insert file type (ex: mzML, mzXML):\n")

#list of files names
file_list = [f for f in listdir(path) if isfile(join(f))]

#loop for zip all the files, individually
for i in file_list:
    i_split = i.split('.')
    if i_split[1] == file_type: zip(i_split[0], i_split[1], path)



