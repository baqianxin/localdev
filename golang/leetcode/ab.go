package leetcode

// 双数之和
func twoSum(list []int, tag int) []int {
	m := make(map[int]int)

	for i := 0; i < len(list); i++ {
		if tag-list[i] == 0 {
			return []int{i}
		}
		if m[tag-list[i]] > 0 {
			return []int{m[tag-list[i]], i}
		} else {
			m[tag-list[i]] = i
		}
	}

	return []int{-1, -1}
}
func twoSum2(nums []int, target int) []int {
	m := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		another := target - nums[i]
		if _, ok := m[another]; ok {
			return []int{m[another], i}
		}
		m[nums[i]] = i
	}
	return nil
}
