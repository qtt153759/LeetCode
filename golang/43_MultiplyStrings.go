package main

import (
	"fmt"
	"strconv"
)
func main(){
	fmt.Println("res",multiply("123","456"))
}
func multiply(num1 string, num2 string) string {
	num := make([]byte,len(num1)+len(num2))
	tmp:=0
  for i:=len(num1)-1;i>=0;i--{
		for j:=len(num2)-1;j>=0;j--{
			// fmt.Println("strat",int(num1[i]-'0'),int(num2[j]-'0'),tmp,int(num[i+j+1]))
			tmp=tmp+int(num1[i]-'0')*int(num2[j]-'0')+int(num[i+j+1])
			num[i+j+1]=byte(tmp%10)
			// fmt.Println("laan",tmp,num)
			tmp=tmp/10

		}
		k:=1
		for tmp>0{
			tmp=tmp+int(num[i+1-k])
			num[i+1-k]=byte(tmp%10)
			tmp=tmp/10
		}
	}
	k:=0
	for k<len(num)-1&&num[k]==0{
		k++
	}
	res:=""
	for i:=len(num)-1;i>=k;i--{
		res=strconv.Itoa((int(num[i])))+res
	}
	return res
}