def canPartitionKSubsets(nums, k):
        N = len(nums)
        nums.sort(reverse = True)

        basket, rem = divmod(sum(nums), k)
        if rem or nums[0] > basket: return False
        print(basket, rem)
        dp = [-1] * (1<<N) 
        dp[0] = 0
        for mask in range(1<<N):
            for j in range(N):
                neib = dp[mask ^ (1<<j)]
                print(bin(mask), bin(neib), j)
                if mask & (1<<j) and neib >= 0 and neib + nums[j] <= basket:
                    dp[mask] = (neib + nums[j]) % basket
                    break
        print(dp)
        return dp[-1] == 0

print(canPartitionKSubsets([4,3,2,3,5,2,1], 4))
