def solution(array_a, array_b):
    if len(array_a) == 0:
        return 0
    suma_de_diferencia = 0
    for index, number in enumerate(array_a):
        numero_comparado = array_b[index]
        if numero_comparado > number:
            suma_de_diferencia += (numero_comparado - number)**2
        else:
            suma_de_diferencia += (number - numero_comparado)**2
    
    return suma_de_diferencia/len(array_a)

if __name__ == "__main__":

    assert solution([1, 2, 3], [4, 5, 6]) == ((3**2 + 3**2 + 3**2) / 3)
    assert solution([10, 20, 30], [13, 18, 35]) == ((3**2 + 2**2 + 5**2) / 3)
    assert solution([7, 7, 7], [7, 7, 7]) == 0
    assert solution([-1, -2, -3], [-1, -5, -6]) == ((0**2 + 3**2 + 3**2) / 3)
    assert solution([5], [10]) == 25
    assert solution([], []) == 0
