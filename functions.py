import unidecode

def no_aplica(datos, array):
    ouString = unidecode.unidecode(datos).lower().lstrip()
    ouList = [unidecode.unidecode(x.lower().lstrip()) for x in array]
    if ouString in ouList:
        return array[ouList.index(ouString)]
    else:
        #print(datos, 'No aplica')
        return 'No aplica'