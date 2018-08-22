/*
Crack Zet3 Challenge Requiring an SMT solver to solve for MITRE STEM CTF 2017
Author: Eugene Kolodenker <eugene@eugenekolo.com>
*/

#include <stdlib.h>
#include <stdio.h>

int fail() {
    exit(-1);
    return 0;
}

void check_0(char* key) {
    if (key[8]-key[13]+key[19]+key[9]!=104)  {
        fail();
    }
}
void check_1(char* key) {
    if (key[16]-key[8]-key[9]*key[1]-key[19]!=-4464)  {
        fail();
    }
}
void check_2(char* key) {
    if (key[2]-key[2]+key[14]*key[15]!=2912)  {
        fail();
    }
}
void check_3(char* key) {
    if (key[13]*key[2]+key[6]!=4541)  {
        fail();
    }
}
void check_4(char* key) {
    if (key[7]+key[7]*key[4]*key[2]!=211300)  {
        fail();
    }
}
void check_5(char* key) {
    if (key[12]*key[15]+key[15]+key[14]!=3748)  {
        fail();
    }
}
void check_6(char* key) {
    if (key[18]*key[19]-key[20]*key[4]-key[13]!=-5332)  {
        fail();
    }
}
void check_7(char* key) {
    if (key[0]*key[3]*key[5]!=454608)  {
        fail();
    }
}
void check_8(char* key) {
    if (key[9]*key[3]-key[8]!=8064)  {
        fail();
    }
}
void check_9(char* key) {
    if (key[1]-key[5]*key[9]-key[5]+key[1]!=-3082)  {
        fail();
    }
}
void check_10(char* key) {
    if (key[4]*key[11]+key[9]!=3511)  {
        fail();
    }
}
void check_11(char* key) {
    if (key[19]*key[14]+key[3]!=3091)  {
        fail();
    }
}
void check_12(char* key) {
    if (key[4]*key[0]*key[16]*key[18]!=17567550)  {
        fail();
    }
}
void check_13(char* key) {
    if (key[17]+key[16]*key[19]+key[13]*key[7]!=6950)  {
        fail();
    }
}
void check_14(char* key) {
    if (key[7]*key[4]+key[14]-key[8]!=3252)  {
        fail();
    }
}
void check_15(char* key) {
    if (key[17]+key[10]*key[0]*key[11]!=212267)  {
        fail();
    }
}
void check_16(char* key) {
    if (key[16]-key[15]+key[17]+key[12]!=138)  {
        fail();
    }
}
void check_17(char* key) {
    if (key[8]+key[5]*key[14]!=2742)  {
        fail();
    }
}
void check_18(char* key) {
    if (key[1]-key[1]+key[5]*key[2]!=3120)  {
        fail();
    }
}
void check_19(char* key) {
    if (key[20]-key[8]+key[1]*key[12]-key[12]!=4691)  {
        fail();
    }
}
void check_20(char* key) {
    if (key[6]+key[5]+key[9]!=170)  {
        fail();
    }
}



int main() {
	char key[21];
	printf("Give me a key: ");
	scanf("%21s", key);
	check_1(key);
	check_2(key);
	check_3(key);
	check_4(key);
	check_5(key);
	check_6(key);
	check_7(key);
	check_8(key);
	check_9(key);
	check_10(key);
	check_11(key);
	check_12(key);
	check_13(key);
	check_14(key);
	check_15(key);
	check_16(key);
	check_17(key);
	check_18(key);
	check_19(key);
	printf("Grats! You made it!");
	return 0;
}
