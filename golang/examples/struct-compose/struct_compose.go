package main

import "fmt"

type myPoint struct {
	x int
	y int
}

type myCircle struct {
	myPoint
	r int
}

func main() {
	p1 := myPoint{
		x: 1,
		y: 2,
	}
	c1 := myCircle{}
	c1.x = 3
	c1.y = 4
	c1.r = 5

	fmt.Println(p1)
	fmt.Println(c1)

	c2 := myCircle{
		myPoint: myPoint{x: 6, y: 7},
		r:       8,
	}
	fmt.Println(c2)

}
