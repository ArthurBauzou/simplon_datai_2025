words = input("entrez plusieurs mots, séparés par des virgules : \n")
word_list = words.split(",")
word_list = [w.strip() for w in word_list]
word_list.sort()

print(word_list)