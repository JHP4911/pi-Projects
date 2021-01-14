'''
You need to write a python script that generates an acronym word from a given sentence.
'''
text = str(input("Enter a String\n"))
text = text.split()
acronym = ""
for i in text: 
    acronym = acronym+str(i[0]).upper()
print(acronym)