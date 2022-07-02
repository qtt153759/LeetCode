package main

func main(){
		
}
func twoSum(nums []int, target int) []int {
	indexMap :=make(map[int]int)
	for index,num := range nums{
		if val,ok := indexMap[target-num];ok{
			return []int{val,index}
		}
		indexMap[num]=index
	}
	return []int{0,0}
	
}