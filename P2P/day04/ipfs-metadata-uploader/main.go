package main

import (
	"fmt"
	"log"
	"os"

	"pool-metadataa-IPFS/api"
)

func main() {
	os.Getenv("STARTON_API_KEY")

	s := api.NewServer(":8080")
	fmt.Println("Server started on port: ", s)
	log.Fatal(s.Start())
	//http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
	//	fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
	//})
	//
	//log.Println("Listening on localhost:8080")
	//
	//log.Fatal(http.ListenAndServe(":8080", nil))
}
