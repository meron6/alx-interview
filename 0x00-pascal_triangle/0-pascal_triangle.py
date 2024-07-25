#!/usr/bin/env python3
"""Calculate Pascal's Triangle"""

def get_triangle(num):
    """Return 2D list of Pascal's Triangle up to num rows"""
    if num <= 0:
        return []
    
    ret = [[1]]
    for i in range(1, num):
        row = [1]  # Start with 1
        for j in range(1, i):
            row.append(ret[i-1][j-1] + ret[i-1][j])
        row.append(1)  # End with 1
        ret.append(row)
    
    return ret

def main():
    """Get number of rows to calculate from the user and show a pretty triangle"""
    try:
        num = int(input('Number of rows: '))
    except ValueError:
        print('Please input a valid integer.')
        exit(1)
    
    triangle = get_triangle(num)
    
    if not triangle:
        print('Number of rows must be a positive integer.')
        return
    
    length = len(triangle)
    
    if length > 100:
        print('Too large, not displaying.')
        return
    
    for i in range(length):
        row = triangle[i]
        print(' ' * (length - i - 1) + ' '.join(str(j) for j in row))

if __name__ == '__main__':
    main()
