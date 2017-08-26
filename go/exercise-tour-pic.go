package main

import (
	"golang.org/x/tour/pic"
	"math"
)

func Pic(dx, dy int) [][]uint8 {
	a := make([][]uint8, dx)

	for i := 0; i<dx; i++ {
		a[i] = make([]uint8, dy)
		for j:=0; j<dy; j++ {
			//a[i][j] = uint8(i+j)/2
			//a[i][j] = uint8(i*j)
			a[i][j] = uint8(math.Pow(float64(i),float64(j)))
		}
	}
	return a
}

func main() {

	pic.Show(Pic)

}
