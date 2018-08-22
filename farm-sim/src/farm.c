/*
Farm Simulator Challenge for MITRE STEM CTF 2017
Author: Eugene Kolodenker <eugene@eugenekolo.com>
*/

#include <stdlib.h>
#include <stdio.h>
#include "util.h"


#define MAX_FARM_COUNT 10
#define MAX_INPUT_BYTES 1024
char* FARMS[MAX_FARM_COUNT];
int FARM_COUNT = 0;

void start_farm() {
  size_t sz;
  char* farm;
  char input[MAX_INPUT_BYTES];

  if (FARM_COUNT >= MAX_FARM_COUNT - 1) { 
    printf("Not enough room for another farm.\n");
    return; 
  }
  
  printf("Size: ");
  read_line(input, 10);
  sz = atoi(input);

  farm = malloc(sz);
  FARMS[FARM_COUNT] = farm;
  FARM_COUNT++;
  printf("Farm added!\n");
}

void harvest_farm() {
  int idx;
  char input[MAX_INPUT_BYTES];

  printf("Farm #: ");
  read_line(input, 4);
  idx = atoi(input);

  if (idx > FARM_COUNT + 1) { 
    printf("Invalid farm\n");
    return; 
  }
  
  if (FARMS[idx]) {
    free(FARMS[idx]);
  }
  FARMS[idx] = NULL;
  FARM_COUNT--;
  printf("Farm harvested!\n");
}

void add_crop() {
  int idx;
  size_t sz;
  char input[MAX_INPUT_BYTES];

  printf("Farm #: ");
  read_line(input, 4);
  idx = atoi(input);

  if (idx > FARM_COUNT + 1) { 
    printf("Invalid farm\n");
    return; 
  }

  if (!FARMS[idx]) {
    printf("Farm doesn't exist\n");
    return;
  }

  printf("Crop size (acres): ");
  read_line(input, 10);
  sz = atoi(input);

  printf("Crop data: ");
  read_line(input, sz + 1);
  strcpy(FARMS[idx], input);
  printf("Crop added!\n");
}

void view_farm() {
  int idx;
  char input[MAX_INPUT_BYTES];

  printf("Farm #: ");
  read_line(input, 4);
  idx = atoi(input);
  
  if (!FARMS[idx]) {
    printf("Invalid farm\n");
    return;
  }

  puts(FARMS[idx]);
}

void print_menu() {
  printf("1 - Start a farm\n");
  printf("2 - Harvest a farm\n");
  printf("3 - Edit a farm\n");
  printf("4 - View a farm\n");
  printf("5 - Exit\n");
  printf("> ");
}

int main() {
  int opt = 0;
  char input[MAX_INPUT_BYTES];

  setbuf(stdout, NULL);
  
  init_heap();
  
  printf("Welcome to Farm Simulator 1984!\n");
  printf("     r-------\n");
  printf("    _|     o\n");
  printf("   / |_____|/_\\_    \\\\\n");
  printf("  |          |o|----\\\\\n");
  printf("  |__MITRE______\\_--_\\\\\n");
  printf(" (O)_O_O_O_O_O_(O)    \\\\\n");

  while (opt != 5) {
    print_menu();
    read_line(input, 4);
    opt = atoi(input);

    switch (opt) {
    case 1:
      start_farm(); 
      break;
    case 2:
      harvest_farm(); 
      break;
    case 3:
      add_crop(); 
      break;
    case 4:
      view_farm(); 
      break;
    case 5:
      printf("Exit!\n");
      break;
    default:
      printf("Invalid option\n");
      exit(1);
      break;
    }

  }
  return 0;
}
