package main

import (
	"fmt"
	"testing"
)

// test function
func Test(t *testing.T) {
	res := searchMatrix([][]int{{1}, {3}}, 0)
	fmt.Println(res)
	expectedRes := false
	if res != expectedRes {
		t.Errorf("Expected res(%v) is not same as actual res (%v)", expectedRes, res)
	}
}
