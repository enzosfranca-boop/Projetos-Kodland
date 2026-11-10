meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "GAG" and "GAG DE LA GAG": 'Estar "Chocado", Perplexo, Estupefato',
            "LARP": "Fingir ser algo que nao e/mentir"
            }
word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")
if word in meme_dict.keys():
    # O que devemos fazer se a palavra for encontrada?
else:
    print("Desculpe, mas essa palavra nao esta no banco de dados")
