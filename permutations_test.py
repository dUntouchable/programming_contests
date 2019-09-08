'''
Arya Stark (100 Marks)
Arya Stark and Sansa Stark are sisters but often fight with each other for one or the other reason. Recently, Sansa beat Arya by cheating in the hunt game and made fun of her. Arya is full of anger and wants to take her revenge. Arya has called her elder sister Sansa for battle and Sansa has accepted it.
The battle consists of R rounds where in each round a different skill will be put to test. The skill may be Archery, Sword fighting or anything else. After each round, the winner of the round will be awarded a point. After all the R rounds are conducted, the one with maximum points is considered as the overall Winner.
Arya is angry and wants not just to win the battle but beat Sansa in such a way that after each round her points are atleast P times the points of Sansa. She is busy preparing for the battle and has heard about your skills. She wants you to find the number of ways in which she can beat Sansa with the provided condition and take her revenge.
The order of winning differentiates the different ways.

Example: Let's consider, there are 3 rounds.
Case 1: Arya won the first round, Sansa the second round and Arya the third round
Arya, Sansa, Arya

Case 2: Arya won the first round, Arya also won the second round and Sansa won the third round
Arya, Arya, Sansa

Both the cases above are different from each other and are considered two different ways.
Note: Since the answer can be large, take modulo by 10^9 + 7.

Input Format
The first line of input consists of number of test cases, T
The only line of each test case consists of two space separated integers R and P.

Constraints
1<= T <=10
1<= R <=1000
1<= P <=R

Output Format
For each test case, print the number of ways possible in a separate line.

Sample TestCase 1
Input
2
4 2
2 2
Output
3
1
'''
from itertools import permutations
def main():
    # Write code here
    #testcases = int(input().rstrip())
    testcases = 1
    for _ in range(testcases):
        #R, S = input().rstrip().split()
        #R, S = int(R), int(S)
        R, S = 20, 5
        arr = []
        # Creating the list
        count_arrya = 0
        for _ in range(R//S + 1):
            for _ in range(S):
                if len(arr) < R:
                    arr.append('A')
                    count_arrya += 1
            if len(arr) < R:
                arr.append('S')

        count = 0
        while('S' in arr):
            all_perm_set = list(set(permutations(arr,R)))
            for var in all_perm_set:
                count_a = 0
                count_s = 0
                flag = True
                for varvar in var:
                    if varvar == 'A':
                        count_a += 1
                    else:
                        count_s += 1
                    if count_a < 2*count_s:
                        flag = False
                        break
                if flag == True:
                    count += 1
            arr[arr.index('S')] = 'A'
        print(count+1)

main()


# 2nd Solution by recurssion, only few lines of codes

def recur(arr, R, S, count_a, count_b):
    if count_a < S * count_b:
        return 0
    if len(arr) == R:
        return 1
    return recur(arr + ['A'], R, S, count_a + 1, count_b) + recur(arr + ['S'], R, S, count_a, count_b + 1)
