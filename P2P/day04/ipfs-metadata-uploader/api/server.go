package api

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"strings"

	"pool-metadataa-IPFS/types"

	"github.com/google/uuid"
)

type Server struct {
	listenAddr string
}

func NewServer(listenAddr string) *Server {
	return &Server{
		listenAddr: listenAddr,
	}
}

func (s *Server) Start() error {

	http.HandleFunc("/upload", s.uploadIPFS)
	return http.ListenAndServe(s.listenAddr, nil)
}

func (s *Server) uploadIPFS(w http.ResponseWriter, r *http.Request) {
	var meta types.Request

	w.Header().Set("Access-Control-Allow-Origin", "http://localhost:3000")
	w.Header().Set("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE")
	w.Header().Set("Access-Control-Allow-Headers", "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization")
	w.Header().Set("Access-Control-Allow-Credentials", "true")
	if r.Method == "OPTIONS" {
		return
	}
	if err := json.NewDecoder(r.Body).Decode(&meta); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	metaB, err := json.Marshal(meta.Content)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	x := fmt.Sprintf(`{
		"name": "%s",
		"content": %s
	}`, uuid.NewString(), metaB)

	fmt.Println(x)
	req, err := http.NewRequest("POST", "https://api.starton.io/v3/ipfs/json", strings.NewReader(x))
	if err != nil {
		return
	}
	req.Header.Set("x-api-key", os.Getenv("STARTON_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	res, err := http.DefaultClient.Do(req)
	if err != nil {
		return
	}

	var body types.Response

	if err := json.NewDecoder(res.Body).Decode(&body); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	b, err := json.Marshal(&body)
	if err != nil {
		return
	}
	_, err = w.Write(b)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
	}
}
