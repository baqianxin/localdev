package main

import(

    "net/http"

    "fmt"

)

func main() {

    http.HandleFunc("/asd",hello)

    http.ListenAndServe(":88",nil)

}

func hello(w http.ResponseWriter, r *http.Request) {

    fmt.Fprintf(w,"Hello Docker Form Golang!")

}