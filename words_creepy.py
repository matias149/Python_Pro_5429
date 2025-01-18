meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "OMG": "Expresion de asombro",
            "NASHE": "Algo asombroso o divertido esta pasando",

            }



word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print('Aqui esta el significado de tu palabra' meme_dict[world])  
else:
    print('Ya que no lo tengo,por que no usas Google?')
