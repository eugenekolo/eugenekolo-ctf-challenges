#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define DO_ROUND_ONE
#define DO_ROUND_TWO
#define DO_ROUND_THREE

#define END 1337
#define MULT 191
#define ADD 3

void shuffle(long long *deck, int size) {
  int i;
  for (i = 0; i < size; i++) {
    long long val = deck[i];
    if (val < 0ll) {
      val = -val;
    }

    long long temp = deck[val % size];
    deck[val % size] = deck[(i + 1) % size];
    deck[(i + 1) % size] = temp;
  }
}

void sort(long long* deck, long long* sorted, int size) {
    for (int i = 0; i < size; i++) {
        sorted[i] = deck[i];
    }

    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
            if (sorted[i] > sorted[j]) {
                long long temp = sorted[i];
                sorted[i] = sorted[j];
                sorted[j] = temp;
            }
        }
    }
}


int main() {
    setbuf(stdout, NULL);
    
    char* flag[21];
    FILE* f = fopen("flag.txt", "r");
    fread (flag, 1, 21, f);

    printf("Let's play some games\n");

#ifdef DO_ROUND_ONE
    printf("1. Solve the following equations:\n");
    printf("X > %i\n", END);
    printf("X * %i + %i = %i\n", MULT, ADD, END);
    
    unsigned int x = 0;

    printf("Enter the solution X: ");
    scanf("%d", &x);

    if(x <= END) {
        printf("Go to school and learn some math!\n");
        return 1;
    }

    x *= MULT;
    x += ADD;

    if (x != 1337) {
        printf("Go to school and learn some math!\n");
        return 2;
    }
#endif
#ifdef DO_ROUND_TWO
    printf("Excellent.\n");

    printf("\n2. Beat my card, we each draw one, bigger number wins\n");
    long long deck[5];

    printf("You get two cards: ");
    long long card;
    scanf("%lld", &card);
    deck[0] = card;
    printf("Added %lld\n", card);
    scanf("%lld", &card);
    deck[1] = card;
    printf("Added %lld\n", card);

    printf("I get three cards\n");
    deck[2] = 314;
    printf("Adding 314\n");
    deck[3] = 159;
    printf("Adding 159\n");
    deck[4] = 265;
    printf("Adding 265\n");

    long long sorted[5];
    sort(deck, sorted, 5);
    long long mycard = sorted[4];
    
    // Pretend to shuffle and have a fair game
    shuffle(deck, 5);
    printf("Cards: %lld %lld %lld %lld %lld\n", deck[0], deck[1], deck[2], deck[3], deck[4]);
    srand(time(0));
    long long theircard = deck[rand() % 5];

    if (theircard <= mycard) {
        printf("Your card: %lld\n", theircard); 
        printf("My card: %lld\n", mycard);
        printf("Better luck next time punk.\n");
        return 3;
    }

    printf("Your card: %lld\n", theircard); 
    printf("My card: %lld\n", mycard);
    printf("What, you win?! okay...\n");
#endif
#ifdef DO_ROUND_THREE
    printf("\n3. What... is your quest?\n");
    struct {
        unsigned long long buf[16];
        int is_correct;
        unsigned long long term;
        unsigned long long term_sz;
    } locals;
    locals.term = 0x20677261696c21;
    locals.term_sz = sizeof(locals.term_sz);
    locals.is_correct = 0;

    printf("Size in bytes: ");
    unsigned long long sz = 0;
    scanf("%llu", &sz);

    if ((sz + locals.term_sz) > sizeof(locals.buf)) {
        printf("Boiiiing!\n");
        return 4;
    }

    printf("Answer in 8 byte pieces: ");
    unsigned long long c = 0;
    unsigned long long cnt = 0;
    while (cnt < (sz / sizeof(unsigned long long))) {
        scanf("%lld", &c);
        if (c != locals.term) {
            locals.buf[cnt] = c;
            cnt++;
        } else {
            break;
        }
    }

    if (!locals.is_correct) {
        printf("Boiiiing!\n");
        return 5;
    }
#endif
    printf("Well done.");
    printf("Flag: %s\n", flag);
    return 0;
}
