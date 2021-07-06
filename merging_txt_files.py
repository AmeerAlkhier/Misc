import os


list_filenames =[]

directory = r'/home/ameer/Downloads/ArabicBible'
for filename in os.listdir(directory):
    if filename.endswith(".txt") :
        list_filenames.append(filename)
    else:
        continue
#print (len(list_filenames))






with open('bible.txt', 'w',encoding='utf-16') as outfile:
  
    # Iterate through list
    for names in list_filenames:

  
        # Open each file in read mode
        with open(names,encoding='utf-16') as infile:
  
            # read the data from the files and write them in bible.txt

            #with open(infile, 'rb') as f:
            contents = infile.read()
            outfile.write(contents)

            #readfile=infile.read()
            #outfile.write(readfile)
  
        # Add '\n' to enter data of from next file 
        outfile.write("++++")
