flname=input('Enter the filename:\n')
print('The entered filename is:',flname)
i=0
brk=flname[i]
while brk!='.':
    i=i+1
    brk=flname[i]
brk=flname[i+1:]
if brk=='py':
    print('It is a python file.\n')
elif brk=='c':
    print('It is a c file.\n')
elif brk=='java':
    print('It is a java file.\n')
elif brk=='cpp':
    print('It is a c++ file.\n')
elif brk=='pdf':
    print('It is a pdf file.\n')
elif brk=='ppt':
    print('It is a ppt file.\n')
elif brk=='doc':
    print('It is a document file.\n')
elif brk=='xls':
    print('It is an excel file.\n')
elif brk==('jpg'or'jpeg'or'png'or'tiff'or'raw'):
    print('It is an image file.\n')
else:
    print('Filename not identified.')
