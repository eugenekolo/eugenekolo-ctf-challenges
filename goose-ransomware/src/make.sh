#!/bin/bash
CGO_CFLAGS_ALLOW="-mllvm|-sub|-fla|-bcf|-split" GOPATH=/home/eugenek/projects/my-ctf-challenges/goose-ransomware CC=/home/eugenek/llvm-obfuscator/build/bin/clang go build -ldflags="-s -w" -o goose-ransomware-sample.exe
