package main

import (
	"fmt"
)
func main(){
	fmt.Println("check",findBall([][]int{{1,1,1,1,1,1},{-1,-1,-1,-1,-1,-1},{1,1,1,1,1,1},{-1,-1,-1,-1,-1,-1}}))
}
func findBall(grid [][]int) []int {
	n:=len(grid)
	m:=len(grid[0])
	res:=[]int{}
  for i:=0;i<m;i++{
		x1:=i
		var x2 int
		for j:=0;j<n;j++{
			x2=x1+grid[j][x1]
			if x2<0||x2>=m||grid[j][x1]!=grid[j][x2]{
				x1=-1
				// fmt.Println("break do",x2)
				break
			}
			// fmt.Println("chec",x2)
			x1=x2
		}
		res=append(res, x1)
	}
	return res
}