//Dictionary-based Spelling Checker
valid_words = {'apple', 'banana', 'orange', 'grape'}
document = ['apple', 'aple', 'banana', 'bannana']
misspelled = [word for word in document if word not in valid_words]
print("Misspelled words:", misspelled)
