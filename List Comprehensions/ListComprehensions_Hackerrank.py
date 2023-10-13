from typing import List


def main():
    '''
    Generate permutations and filter based on the sum of elements.

    @params:None
    @desc:
    This script takes four integer inputs (x, y, z, n) from the user and generates
    all possible permutations of (i, j, k) where i is in the range [0, x], j is in
    the range [0, y], and k is in the range [0, z]. It then filters these permutations
    to exclude those where the sum of elements is equal to n and prints the result.
    @returns: none
    '''
    
    
    x: int = int(input('Enter value for x: '))
    y: int = int(input('Enter value for y: '))
    z: int = int(input('Enter value for z: '))
    n: int = int(input('Enter value for n: '))
    
    
    # Generate list of numbers from 0 to x,y, and z
    x1 = [p for p in range(x + 1)]
    y1 = [p for p in range(y + 1)]
    z1 = [p for p in range(z + 1)]
    
    
    # Gives the required permutations
    permutations: List[List[int]] = [[i, j, k] for i in x1 for j in y1 for k in z1]
    
    # Gives the permutations that in which [i,j,k] sum not equal to n
    required_permutations: List[List[int]] = [perm for perm in permutations if sum(perm) != n]
    
    print(required_permutations)
    

if __name__ == '__main__':
    main()