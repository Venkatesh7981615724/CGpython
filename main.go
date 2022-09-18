package main

import "fmt"

// no inheritance and no parent child things in Golang

func main() {
	fmt.Println("welcome to structs in Golang ")

	e1 := Employee{"mani", "mani@gmail.com", true, 25}
	fmt.Println(e1)
	fmt.Println(e1.Name, e1.Email)

	e2 := Employee{"prasad", "prasad@gmail.com", true, 25}
	fmt.Println(e2)
	fmt.Println(e2.Name, e2.Email)

}

type Employee struct {
	Name   string
	Email  string
	Status bool
	Age    int
}
