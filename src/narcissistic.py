def narcissistic( value ):
    
    lista_numeros=[]
    for i in str(value):
        lista_numeros.append(int(i))
        
    longitud= len(lista_numeros)
    resultado = 0
    
    for i in lista_numeros:
        resultado += i**longitud
            
    return resultado == value


if __name__ == "__main__":

    assert narcissistic(153) is True
    assert narcissistic(9474) is True
    assert narcissistic(7) is True
    assert narcissistic(9475) is False
    assert narcissistic(10) is False