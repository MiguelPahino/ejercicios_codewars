import string

def mix(s1, s2):
    abecedario = string.ascii_lowercase
    repeticiones1 = {}
    repeticiones2 = {}

    for letra in abecedario:
        repeticiones1[letra] = s1.count(letra)
        repeticiones2[letra] = s2.count(letra)

    comparaciones = []
    for letra in abecedario:
        if repeticiones1[letra] > 1 or repeticiones2[letra] > 1:
            if repeticiones1[letra] > repeticiones2[letra]:
                comparaciones.append(f"1:{letra * repeticiones1[letra]}")
            elif repeticiones2[letra] > repeticiones1[letra]:
                comparaciones.append(f"2:{letra * repeticiones2[letra]}")
            else: 
                comparaciones.append(f"=:{letra * repeticiones1[letra]}")
    comparaciones.sort()
    comparaciones.sort(key=len, reverse=True)
    return "/".join(comparaciones)

if __name__ == "__main__":

    assert mix("Are they here", "yes, they are here") == "2:eee/2:yy/=:hh/=:rr"
    assert mix("looping is fun but dangerous", "less dangerous than coding") == "1:ooo/=:nnn/1:uuu/2:sss/=:gg"
    assert mix(" In many languages", " there's a pair of functions") == "1:aaa/1:nn/2:tt/2:ss/=:ii"
    assert mix("Lords of the Fallen", "gamekult") == "1:ll/=:oo"
    assert mix("codewars", "codewars") == ""
    assert mix("A generation must confront the looming ", "codewarrs") == "1:nnn/1:ooo/=:tt"

