"""
Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and may have distributed the chocolates unequally. One of the program managers gets to know this and orders Christy to make sure everyone gets equal number of chocolates.

But to make things difficult for the intern, she is ordered to equalize the number of chocolates for every colleague in the following manner,

For every operation, she can choose one of her colleagues and can do one of the three things.

    She can give one chocolate to every colleague other than chosen one.
    She can give two chocolates to every colleague other than chosen one.
    She can give five chocolates to every colleague other than chosen one.

Calculate minimum number of such operations needed to ensure that every colleague has the same number of chocolates.

Input Format

First line contains an integer denoting the number of testcases. testcases follow.
Each testcase has lines. First line of each testcase contains an integer denoting the number of co-interns. Second line contains N space separated integers denoting the current number of chocolates each colleague has.

Constraints



Number of initial chocolates each colleague has <

Output Format

lines, each containing the minimum number of operations needed to make sure all colleagues have the same number of chocolates.

Sample Input

1
4
2 2 3 7

Sample Output

2
"""

def incr_temp(temp):
    x = 0
    if temp >= 5:
        x = temp/5
        temp = temp%5
    if temp >=2:
        x += temp/2
        temp = temp%2
    x += temp
    return x

def main():
    T = int(raw_input().strip())
    
    
    while True:
        if T == 0:
            break
        minN = 1000000
        N   = int(raw_input().strip())
        A   = map(int,raw_input().strip().split(' '))
        for i in xrange(N):
            if A[i] < minN:
                minN = A[i]
        sumN = list()
        for j in xrange(6):
            sumN.append(0)
            for i in xrange(N):
                temp = abs(A[i] - (minN -j))
                sumN[j] = sumN[j] + incr_temp(temp)
        
        print min(sumN)
        T = T-1
    return 0;

if __name__ == '__main__':
    main()
