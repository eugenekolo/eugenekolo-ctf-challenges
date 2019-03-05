package main

import (
    "crypto/des"
    "crypto/cipher"
    "encoding/base64"
    "fmt"
    "io/ioutil"
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
    // ZOhw9d/k0DorBrBPs0d6EfqqO2xOGUeT
    key, _ := base64.StdEncoding.DecodeString(os.Args[1])
    // /tmp/safety-folder-18972910
    searchDir := os.Args[2]
    targetExt := []string{".enc"}
    fileList := []string{}

    filepath.Walk(searchDir, func(path string, f os.FileInfo, err error) error {
        if stringInSlice(filepath.Ext(path), targetExt) {
            fileList = append(fileList, path)
            encrypted, _ := ioutil.ReadFile(path)
            clean := decrypt(key, encrypted)
            ioutil.WriteFile(path+".dec", clean, 0644)
        }
        return nil
    })

    for _, file := range fileList {
        fmt.Println(file)
    }
}

func decrypt(key []byte, text []byte) []byte {
    ciphertext, _ := base64.URLEncoding.DecodeString(string(text))
    block, _ := des.NewTripleDESCipher(key)
    plaintext := make([]byte, len(ciphertext)-des.BlockSize)
    iv := ciphertext[:des.BlockSize];
    stream := cipher.NewCFBDecrypter(block, iv)
    stream.XORKeyStream(plaintext, ciphertext[des.BlockSize:])
    return plaintext
}
