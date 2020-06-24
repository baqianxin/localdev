package main

import "fmt"

/// pa楼梯DP
func climbStairs(n int) int {
	rel := map[int]int{}
	for i := 1; i <= n; i++ {
		if i < 3 {
			rel[i] = i
		} else {
			rel[i] = rel[i-1] + rel[i-2]
		}
	}

	return rel[n]
}

// 跳数组-DP
func canJump(nums []int) bool {

	var n = len(nums)
	if n == 1 {
		return true
	}

	for i := 0; i < n; {
		if nums[i] == 0 || nums[i+nums[i]] == 0 {
			return false
		}
		if i+nums[i] >= n-1 {
			fmt.Println(i, nums[i])
			return true
		}
		i += nums[i]
	}
	return false
}

func main() {
	// fmt.Println(climbStairs(5))
	arr := []int{1, 0, 1, 0} //[2,5,0,0]
	fmt.Println(canJump(arr))

}
