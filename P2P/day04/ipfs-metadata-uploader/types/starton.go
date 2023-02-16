package types

type Request struct {
	Name    string `json:"name"`
	Content struct {
		Image       string `json:"image"`
	} `json:"content"`
}

type Response struct {
	Cid string `json:"cid"`
}
