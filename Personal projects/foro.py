import random


words = '''En un sábado con cielo despejado y clima de verano hubo “tardecita” literaria y “nochecita” artística en distintos espacios culturales porteños. Mientras festival Filbita copó Biblioteca Parque de Estación, con talleres y rondas de lectura, Usina del Arte se disfrazó al estilo Harry Potter para recibir a familias con chicos de todas edades en segunda edición de Nochecita, una mini noche de museos que también se realizó Sívori, Larreta Moderno, entre otros.'''.split()
words2 = '''En un sábado con cielo despejado y clima de verano hubo “tardecita” literaria y “nochecita” artística en distintos espacios culturales porteños. Mientras el festival Filbita copó la Biblioteca Parque de la Estación, con talleres y rondas de lectura, la Usina del Arte se disfrazó al estilo Harry Potter para recibir a familias con chicos de todas las edades en la segunda edición de la Nochecita, una mini noche de los museos que también se realizó en el Sívori, el Larreta y el Moderno, entre otros.
'''.split()
def randomize(words_list):
    text_length = len(words_list)
    randomized_word_list = []
    for i in range(0, text_length):
        i = random.randrange(0, text_length)
        randomized_word_list.append(words_list[i])
        del words_list[i]
        if text_length > 0:
            text_length -= 1
        else:
            break
    return randomized_word_list

print(*randomize(words2))