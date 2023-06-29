# SORT AND SEARCHING
1. Distinct numbers
2. Distinct Numbers
    - Sort and searh if i > 0 and arr[i] != arr[i-1] -> return
3. Apartments
    - Sort applicants and appartments. Use 2 pointer and compare each applicant vs appartment.
4. Ferris Wheel
    - Sort and greedily pair largest and smallest at a time.
5. Concert Tickets
    - Sort the ticket prices. For each customer, search for the lower_bound(customer_price + 1, 0)
6. Restaurant Customers
    - Sort arrive time, sort leave time. Use 2 pointer, diff between j and j is the number of current customer
7. Movie Festival
    - Greedy, sort by finish time, if current.start > last_finish_in_time -> take it
8. Sum of Two Values
    - sort/map
9. Maximum Subarray Sum
    - Kadane 's algorithm: 
10. Stick Lengths
    - find median, res += abs(num - median)
11. Missing Coin Sum
    - assume that we can built sum [1..k]a[i],if
      - a[i] > k+1 -> return k+1
      - a[i] = k+1 : obviously can built k+1
      - a[i] < k+1 -> a[i] is in [1..k]
      -> for n in nums:
            if n > sum +1:
                return n
            else:
                sum += n

12. Collecting Numbers
    - If the number x  occurs before x+1  then you can always take both of them in a single round and hence it won’t contribute anything to the answer but if x comes after x+1 then we cannot take them  in the single round hence we add 1 to the final answer.

13. Collecting Numbers II
14. Playlist
    - longest subarray having distinct elements
15. Towers
    - longest increasing subsequence
    - or: Greedy approach: always add the next cube on top of the tower with the smallest possible cube on top (or create a new tower if this isn't possible).
        - an set, for each cube, find the upper_bound:
            - if not found: -> insert
            - if found: -> insert + erase(larger_value)
16. Traffic Lights
    - need a data structure that can find + delete + insert efficiently
17. Josephus Problem I
18. Josephus Problem II
19. Nested Ranges Check
20. Nested Ranges Count
21. Room Allocation
    - sort by arrive time, heap to store depart time.
22. Factory Machines
23. Tasks and Deadlines
24. Reading Books
25. Sum of Three Values
26. Sum of Four Values
27. Nearest Smaller Values
28. Subarray Sums I
29. Subarray Sums II
30. Subarray Divisibility
31. Subarray Distinct Values
32. Array Division
33. Sliding Median
34. Sliding Cost
35. Movie Festival II
36. Maximum Subarray Sum II


# DYNAMIC PROGRAMMING

3. Coin combination 1
    - loop throught n and coins
4. Coin combination 2
    - loop throught coins and n
7. Book shop
    - 0/1 knapsack problem:
        - dp[i][j] = max(dp[i-1][j], reward[i] + dp[i-1][j-cost[i]])
8. Array description
    -
9. Removal game
    