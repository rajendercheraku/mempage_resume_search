import glob
import os
file_list = glob.glob(os.path.join(os.getcwd(), "word", "*.txt"))
words = int(input("enter the number of words you want to search"))
words_list = []
finding_words = {}
def unique_values(x):
     return list(dict.fromkeys(x))
for i in range(words):
    x = input("enter the word")
    words_list.append(x)
    finding_words.__setitem__(x, list())

for file_path in file_list:
    print(file_path)
    with open(file_path) as f_input:
        for line in f_input:
            for i in words_list:
                if i.upper() in line:
                    finding_words[i].append(f_input.name)
                elif i.lower() in line:
                      finding_words[i].append(f_input.name)
                     
with open("output_file.txt" ,"w") as f:
    for key,values in finding_words.items():
        f.write(key +": ")
        values = unique_values(values)
        if len(values)==0:
            f.write("this word is not existing in these files")
        else:
            for i in values:
                f.write(i + ",")    
        f.write('\n')

        
                    
           
            
        

 
