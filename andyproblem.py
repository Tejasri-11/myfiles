"""Andy wants to go on a vacation to de-stress himself. Therefore he decides to take a trip to an island. It is given that he has as many consecutive days as           possible to rest, but he can only make one trip to the island. Suppose that the days are numbered from 1 to N. Andy has M obligations in his schedule, which     he has already undertaken and which correspond to some specific days. This means that ith obligation is scheduled for day Di. Andy is willing to cancel at         most k of his obligations in order to take more holidays.

    Your task is to find out the maximum days of vacation Andy can take by canceling at most K of his obligations.

    Input Format

The first line contains an integer N, denoting the total number of days
The next line contains an integer M denoting the total number of obligations.
The next line contains an integer K denoting the largest number of obligations he could cancel 
Each line i of the M subsequent lines (where 0<=i<=M) contains an integer describing Di.
    Constraints

1<=N<=10^6
1<=M<=2*10^6
1<=K<=2*10^6
1<=D[i]<=10^6
   Sample Input 1:

   10
    5
    2
    6
    9
     3
     2
     7

   Sample Output 1 :

    5"""
n = int(input())
m = int(input())
k = int(input())
arr = [0] * n
for i in range(m):
   arr[i] = int(input())
ans = 0
arr.sort()
if k > 0:
   for i in range(k + 1, m + 3, 1):
       ans = max(ans, arr[i] - arr[i - k - 1] - 1)
else:
   j = 0
   while arr[j] == 0:
       j = j + 1
   count = 0
   for i in range(1, n + 1, 1):
       count += 1
       if j < n and (i == arr[j]):
           count = 0

           j += 1
       ans = max(count, ans)
print(ans)
