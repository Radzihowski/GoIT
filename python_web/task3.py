""" Є список слів vocab, і список з одного єлемента query
Треба порахувати скільки разів кожен елемент з списка vocab зустрічається в query
vocab = ["who", "is", "vladimir", "zelensky", "bla", "bla2", "president", "ukraine", "a", "fact", "it"]
query = ["vladimir zelensky is president ukraine It is a fact"]

Результат повинен бути таким
output = [0, 2, 1, 1, 0, 0, 1, 1, 1, 1, 1] """

vocab = ["who", "is", "vladimir", "zelensky", "bla", "bla2", "president", "ukraine", "a", "fact", "it"]
query = ["vladimir zelensky is president ukraine It is a fact"]
def counter(vacab:list, query:list):
    dict_vocab = {}
    for el in vocab:
        dict_vocab[el.lower()] = 0

    reformated_query = query[0].split(' ')

    for i in reformated_query:
        if i.lower() in dict_vocab:
            dict_vocab[i.lower()] += 1
            print(dict_vocab[i.lower()])
    return dict_vocab.values()

print(counter(vocab, query))