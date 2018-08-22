/*
ROP 101 Challenge for MITRE STEM CTF 2017
Author: Eugene Kolodenker <eugene@eugenekolo.com>
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <fcntl.h>
#include <sys/stat.h>

#define STDIN 0
#define STDOUT 1
#define STDERR 2

void vuln_func() {
    char buf[100];
    read(STDIN, buf, 256);
}

void let_me_help_you() {
    setregid(1000, 1000);
}

void get_flag1() {
    printf("Here comes flag1: \n");
    char flag[21];
    let_me_help_you();
    int fd = open("flag1.txt", O_RDONLY);
    read(fd, flag, 21);
    write(STDOUT, flag, 21);
    close(fd);
}

int setup_get_flag2() {
    return 0x1337;
}

void get_flag2() {
    register int eax asm("eax");
    if (eax == 0x1337) {
        printf("Here comes flag2: \n");
        char flag[21];
        let_me_help_you();
        int fd = open("flag2.txt", O_RDONLY);
        read(fd, flag, 21);
        write(STDOUT, flag, 21);
        close(fd);
    }
}

int main() {
    printf("================================================\n");
    printf("Welcome to ROP (return-oriented programming) 101\n");
    printf("There's 3 flags\n");
    printf("Good luck\n");
    printf("================================================\n");

    vuln_func();
    return 0;
}
