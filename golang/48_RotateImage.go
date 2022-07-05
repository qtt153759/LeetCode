package main

import "fmt"
func main(){
	matrix:=[][]int{{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}}
	rotate(matrix)
	fmt.Println("check",matrix)
}
func rotate(matrix [][]int)  {
	size:=len(matrix)
	for y:=0;y<size/2;y++{
		for x:=y;x<size-y-1;x++{
			tmp:=matrix[y][x]
			matrix[y][x]=matrix[size-1-x][y]
			matrix[size-1-x][y]=matrix[size-1-y][size-1-x]
			matrix[size-1-y][size-1-x]=matrix[x][size-1-y]
			matrix[x][size-1-y]=tmp
		}
	}
}