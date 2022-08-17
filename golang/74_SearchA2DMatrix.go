package main

func searchMatrix(matrix [][]int, target int) bool {
	left, right := 0, len(matrix)-1
	var row int = 0
	if len(matrix) == 1 {
		row = 0
		if matrix[row][0] > target || matrix[row][len(matrix[row])-1] < target {
			return false
		}
	} else {
		if matrix[0][0] > target || matrix[len(matrix)-1][len(matrix[row])-1] < target {
			return false
		}
		for left <= right {
			mid := (left + right) / 2
			if matrix[mid][0] == target {
				right = mid
				break
			} else if matrix[mid][0] > target {
				right = mid - 1
			} else {
				left = mid + 1
			}
		}
		row = right
	}
	// fmt.Println(row)
	if len(matrix[row]) == 1 {
		if matrix[row][0] != target {
			return false
		}
	}
	left, right = 0, len(matrix[row])-1
	for left <= right {
		mid := (left + right) / 2
		if matrix[row][mid] == target {
			return true
		} else if matrix[row][mid] > target {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return false
}
