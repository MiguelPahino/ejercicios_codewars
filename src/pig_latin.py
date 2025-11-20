def pig_it(text):
    
    output=""
    lista_texto= text.split()
    
    for posicion, i in enumerate(lista_texto):
        if i != "?" and i != "!":
            if posicion!= len(lista_texto)-1:
                palabra=i[1:]+i[:1]+"ay"
                output+= palabra+" "
            else:
                palabra=i[1:]+i[:1]+"ay"
                output+= palabra
        else:
            output+=i

    return output


if __name__ == "__main__":

    assert pig_it("Pig latin is cool") == "igPay atinlay siay oolcay"
    assert pig_it("This is my string") == "hisTay siay ymay tringsay"
    assert pig_it("Python") == "ythonPay"
    assert pig_it("") == ""