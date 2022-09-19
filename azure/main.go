package main

import (
	"encoding/json"
	"log"
	"net/http"
	//"math/rand"
	//"strconv"
	"github.com/gorilla/mux"
	
)
//Book sruct (model)
type Book struct {
    ID    string  `json:"id"`
	Isbn   string  `json:"Isbn"`
	Title  string  `json:"Title"`
	Author *Author `json:"Author"`
}
//author Struct
type Author struct {
	Firstname string `json:"Firstname"`
	Lastname  string `json:"Lastname"`
}
//init books var as a slice book struct
var books []Book

//get all books
func getBooks(w http.ResponseWriter, r *http.Request){
	w.Header().Set("Content-type","application/json")
	json.NewEncoder(w).Encode(books)
	
}
//get single book
func getBook(w http.ResponseWriter, r *http.Request){
	//w.Header().Set("Content-type","application/json")
	//Parms :=mux.Vars(r)
	//for _,item :=range books{
		//if item.ID ==Parms["id"]{
			//json.NewEncoder(w).Encode(item)
			//return
		//}

	//}
	

}
//create a new book
func createBook(w http.ResponseWriter, r *http.Request){

}
func updateBook(w http.ResponseWriter, r *http.Request){

}
func deleteBook(w http.ResponseWriter,r *http.Request){

}
func main() {
	//init Router
	r :=mux.NewRouter()

	//mock data
	books = append(books, Book{ID:"1", Isbn:"448743", Title:"Book one", Author: &Author{Firstname:"john", Lastname:"doe"}})
	books = append(books, Book{ID:"2", Isbn:"847564", Title:"Book two", Author: &Author{Firstname:"steve", Lastname:"simth"}})
	
	//router handlers /end points
	r.HandleFunc("/api/books", getBooks).Methods("GET")
	r.HandleFunc("/api/books/{id}", getBook).Methods("GET")
	r.HandleFunc("/api/books", createBook).Methods("POST")
	r.HandleFunc("/api/books/{id}", updateBook).Methods("PUT")
	r.HandleFunc("/api/books{id}", deleteBook).Methods("DELETE")

    log.Fatal(http.ListenAndServe(":8000", r))
}
