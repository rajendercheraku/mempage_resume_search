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
    with open(file_path) as f_input:
        for line in f_input:
            for i in words_list:
                if i in line:
                    print(f_input.name)
                    finding_words[i].append(f_input.name)
                    print(type(f_input))
print(finding_words)
a=0
with open("output_file.txt" ,"w") as f:
    for key,values in finding_words.items():
        f.write(key +": ")
        print(values)
        values = unique_values(values)
        if len(values)==0:
            f.write("this word is not existing in these files")
        else:
            for i in values:
                f.write(i + ",")    
        f.write('\n')
print(type(a))
        
                    
           
            
        

 
