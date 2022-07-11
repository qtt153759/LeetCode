package main

import "sort"

//four sum thi chi con cach nang bac + three sum thoi
func fourSum(nums []int, target int) [][]int {
	if len(nums) <=3 {
			return [][]int{}
	}

// Time: O(nlogn)
	sort.Ints(nums)
	
// Time: O(n^3)
	result := make([][]int, 0)
	ptr1 := 0
	for ptr1 < len(nums)-3 {
			val1 := nums[ptr1]
			ptr2 := ptr1+1
			for ptr2 < len(nums)-2 {
					val2 := nums[ptr2]
					
					/* 2Sum (begin) */
					ptr3, ptr4 := ptr2+1, len(nums)-1
					val3, val4 :=  nums[ptr3], nums[ptr4]
					for ptr3 < ptr4 {
							val3, val4 = nums[ptr3], nums[ptr4]
							sum := val1 + val2 + val3 + val4
							if sum == target {
									result = append(result, []int{val1, val2, val3, val4})
									for prevVal3 := val3; ptr3 < ptr4 && prevVal3 == val3; {
											ptr3++
											val3 = nums[ptr3]
									}
							} else if sum < target {
									ptr3++
							} else {
									ptr4--
							}
					}
					/* 2Sum (end) */
		
		// To not have duplicated results (ex: `[2, 2, 2, 2]` & `[2, 2, 2, 2]`
					for prevVal2 := val2; ptr2 < len(nums)-2 && prevVal2 == val2; {
							ptr2++
							val2 = nums[ptr2]
					}
			}

	// To not have duplicated results (ex: `[2, 2, 2, 2]` & `[2, 2, 2, 2]`
			for preVal1 := val1; ptr1 < len(nums)-1 && preVal1 == val1; {
					ptr1++
					val1 = nums[ptr1]
			}
	}
	return result
}