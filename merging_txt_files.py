import os

list_filenames =[]
directory = r'/home/ameer/Downloads/ArabicBible'

for filename in os.listdir(directory):
    if filename.endswith(".txt") :
        list_filenames.append(filename)
    else:
        continue
        
#print (len(list_filenames))
# Create a file in write mode with the correct encoding to accumulate the other files in
with open('bible.txt', 'w',encoding='utf-16') as outfile:
  
    # Iterate through list
    for names in list_filenames:

  
        # Open each file in read mode with the correct encoding
        with open(names,encoding='utf-16') as infile:
  
            # read the data from the files and write them in bible.txt
            contents = infile.read()
            outfile.write(contents)
            
