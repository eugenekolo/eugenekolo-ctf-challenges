#!/bin/bash
gcc -m32 -z execstack -fno-stack-protector -std=c99 -w farm.c util.c -o farm

