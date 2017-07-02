import re


def etiqueta_maestra(source, pattern):    
    matches = re.findall(pattern, source, re.DOTALL)

    return matches
    

def subetiqueta(source, pattern):
    result = ""

    try:    
        matches = re.findall(pattern, source, flags=re.DOTALL)
        result = matches[0]
    except:
        result = ""

    return result
    
