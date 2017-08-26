package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) (float64, int) {
	zn := x
	zn1 := 0.0
	i:=0
	for ; ; i++ {
		zn1 = zn - (zn*zn - x)/2/zn
		zn = zn1
		if math.Abs(zn1*zn1-x) < 0.0000000001 {
			break
		}
	}
	return zn1, i
}

func main() {
	fmt.Println(Sqrt(20))
	fmt.Println(math.Sqrt(20))
}
