# First module

# importing required modules
from zipfile import ZipFile

# specifying the zip file name 
file_name = "theHarvester.zip"

# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip:
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')

fileNames = zip.namelist()
# opening the text file

for fileName in fileNames:
    if fileName[len(fileName) - 1] == '/':
        fileNames.remove(fileName)
        # print(fileName)

fileNames.remove('theHarvester-master/theHarvester/lib/')
fileNames.remove('theHarvester-master/wordlists/general/')
fileNames.remove('theHarvester-master/.github/workflows/')

for i in range(0, len(fileNames)):
    with open(fileNames[i], 'r', encoding="Latin-1") as file:
        # if ("password" in file.read()):
        #     print(fileNames[i])
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                # displaying the words
                # TODO extract to file??
                # TODO what is the password??
                if "password" in word:
                    print(word)

# Second module
# import os
# os.chdir('C:\\Users\\vadim\\PycharmProjects\\python_assignment\\theHarvester-master')  # set the path of the unzipped folder
# ListFiles = os.walk(os.getcwd())
# SplitTypes = []
# for walk_output in ListFiles:
#     for file_name in walk_output[-1]:
#         SplitTypes.append(file_name.split(".")[-1])
#
# #print(SplitTypes)
#
# from collections import Counter
# counter = Counter(SplitTypes)
# print counter

# Create a ZipFile Object and load sample.zip in it
file_name1 = "theHarvester.zip"
with ZipFile(file_name1, 'r') as zipObj:
    # Get list of ZipInfo objects
    listOfiles = zipObj.infolist()
    listOfiles = sorted(listOfiles, key=lambda x: x.file_size)

# TODO delete all folders properly
for element in listOfiles:
    if (element.filename[-1:] == '/'):
        listOfiles.remove(element)
        # print(fileName)

        # listOfiles.remove('theHarvester-master/bin/')
        # Iterate of over the list of ZipInfo objects & access members of the object
for elem in listOfiles:
    print(elem.filename + ' : ', elem.file_size)

from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_xy(0, 0)
pdf.set_font('arial', 'B', 10.0)
for i in range(1, 10):
    text = '\n' + str(i) + 'file name: ' + listOfiles[i].filename + '  size: ' + str(listOfiles[i].file_size)
    pdf.cell(ln=i, h=5.0, align='M', w=0, txt=text, border=0)
pdf.output('analyzed results.pdf', 'F')
