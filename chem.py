from chemlib import Element

def getElementProperties(ElementSymbol):
    if len(ElementSymbol) != 2:
        return "Invalid Element"
    formattedSymbol = ElementSymbol[0].upper() + ElementSymbol[1].upper()
    cur_element = Element(formattedSymbol)
    return cur_element.properties