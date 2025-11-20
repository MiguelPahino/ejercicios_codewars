def find_outlier(integers):
    odd_number=None
    even_number=None
    even_count=0
    odd_count=0
    
    for i in integers:
        if not i%2==0:
            odd_count+=1
            odd_number=i
    for i in integers:
        if i%2==0:
            even_count+=1
            even_number=i
            
    if even_count > odd_count:
        output=odd_number
    else:
        output=even_number
        
    return output


if __name__ == "__main__":

    assert find_outlier([2, 4, 6, 8, 3]) == 3
    assert find_outlier([1, 3, 5, 7, 8]) == 8
    assert find_outlier([-2, -4, -6, -7]) == -7
    assert find_outlier([-1, -3, -5, -6]) == -6
    assert find_outlier([10, 1, 3, 5]) == 10
    assert find_outlier([9, 2, 4, 6, 8]) == 9
    assert find_outlier([1, 3, 5, 7, 2]) == 2