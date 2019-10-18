M1 = [3, 4, 5]
M2 = [6, 7, 8]
m1 = M1[1]
m2 = M2[1]

result = [10, 11]
result.append(m1)
result.append(m2)
result.insert(3, 25)
result[3] = 27











def middle_way(A: list, B: list, i) -> list:
    """
    Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

    middle_way([1, 2, 3], [4, 5, 6]) ? [2, 5]
    middle_way([7, 7, 7], [3, 8, 0]) ? [7, 8]
    middle_way([5, 2, 9], [1, 4, 5]) ? [2, 4]

    :param a: List of integers of length 3.
    :param b: List of integers of length 3.
    :return: List of integers of length 2.
    """
    result = []
    if i >= len(A) or i >= len(B):
        print("Index out of range")
        return result
    
    mid_a = A[i]
    mid_b = B[i]
    result.append(mid_a)
    result.append(mid_b)
    
    return result
    
    
def test_for():
    """
    method prints elements
    
    test_for() -> None
    """
    
    X = [1,2,3,4,5]
    for x in "john doe":
        print(x + str(5))





def get_even_numbers(numbers: list) -> list:
    """
    method returns only even elements of the given collection

    >>> get_even_numbers([1,2,3,4,5] -> [2,4]
    >>> get_even_numbers([2,4,6] -> [2,4,6]

    :param numbers: List of integers
    :return: List of only even integers from `numbers` in the same sequence 
    """

    # for ... in ...:
    #     if ...:
    #         .append(some_even_number)
    #
    # return result
    pass
    
if __name__ == '__main__':
    A = [1,2,3,10]
    B = [4,5,6]
    #print(middle_way(A, B, 10))
    print(test_for())
    
                     
