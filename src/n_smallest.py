def first_n_smallest(arr, n):
    pequeno= sorted(arr)[:n]
    output=[]
    
    for num in arr:
        if num in pequeno:
            output.append(num)
            pequeno.remove(num)
    return output
            

if __name__ == "__main__":

    assert first_n_smallest([5, 1, 3, 2, 4], 3) == [1, 3, 2]
    assert first_n_smallest([4, 2, 1, 2, 5], 3) == [2, 1, 2]
    assert first_n_smallest([7, 3], 5) == [7, 3]
    assert first_n_smallest([], 3) == []
    assert first_n_smallest([1, 2, 3], 0) == []
    assert first_n_smallest([5, 5, 5, 5], 2) == [5, 5]
    assert first_n_smallest([1, 2, 3, 4], 2) == [1, 2]