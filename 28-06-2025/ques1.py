translations = {'hello': 'bonjour', 'world': 'monde'}
sentence = "hello world"
translated = ' '.join([translations.get(word, word) for word in sentence.split()])
print("Translated Sentence:", translated)


