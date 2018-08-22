/*
Farm Simulator Challenge for MITRE STEM CTF 2017
Author: Eugene Kolodenker <eugene@eugenekolo.com>

Contains custom malloc implementation.
*/

#include <sys/mman.h>
#include <unistd.h>

#define THRESHOLD (sizeof(mchunk) * 4)
#define BASE_HEAP_SIZE 1024

struct mchunk {
  size_t sz; // Last bit used to keep track if inuse
  struct mchunk *fd;
  struct mchunk *bk;
  char data[0];
};
typedef struct mchunk mchunk;

mchunk* BASE;

// Start the linked list w/ a base, and 1 chunk
void init_heap(void) {
  // The first ancestor
  size_t base_amount = 2*sizeof(mchunk) + BASE_HEAP_SIZE;
  BASE = sbrk(base_amount);
  BASE->fd = NULL;
  BASE->bk = NULL;
  BASE->sz = sizeof(mchunk);

  // The first sweet child o' mine
  mchunk* first = BASE + 1;
  BASE->fd = first;
  first->bk = BASE;
  first->fd = NULL;
  first->sz = BASE_HEAP_SIZE;
}

#define is_inuse(ptr) ptr->sz & 1

void flag_inuse(mchunk* ptr) {
  ptr->sz |= 1;
}

void deflag_inuse(mchunk* ptr) {
  ptr->sz &= 0;
}

void* malloc(size_t sz) {
  mchunk* ret_chunk;

  // Calculate the real size of the chunk, add space for the mchunk header, and align it
  sz += sizeof(mchunk);
  sz += sizeof(mchunk) - (sz % sizeof(mchunk));
    
  // Try to find an chunk that fits our size
  ret_chunk = BASE;
  while (ret_chunk && (sz > ret_chunk->sz || (is_inuse(ret_chunk)))) {
    ret_chunk = ret_chunk->fd;
  }

  // No valid chunk was found
  if (!ret_chunk) {
    ret_chunk = sbrk(sz);

    // Find the previously last chunk, and update fd and bk ptrs
    mchunk* last_chunk = BASE;
    while (last_chunk->fd) { 
      last_chunk = last_chunk->fd;
    }
    ret_chunk->fd = NULL;
    ret_chunk->bk = last_chunk;
    ret_chunk->sz = sz;
    flag_inuse(ret_chunk);
    last_chunk->fd = ret_chunk;
    return &ret_chunk->data;
  }

  flag_inuse(ret_chunk);
  return &ret_chunk->data;
}

void free(void *ptr) {
  
  if (!ptr) {
    return;
  }

  // Assume the input (`ptr`) is pointing to the data of an mchunk
  mchunk* selected = (mchunk *)((char *)ptr - sizeof(mchunk));
  mchunk* fd = selected->fd;
  mchunk* bk = selected->bk;

  // If there's a chunk ahead us, make it bk point to the previous chunk instead of us
  // If there's a chunk before us, make it fd point to the next chunk instead of us
  if (fd) {
    fd->bk = bk;
  }
  if (bk) {
    bk->fd = fd; 
  }

  // Flag it freed
  deflag_inuse(selected);
}

int read_line(char* out, size_t len) {
  char c;
  int i;

  for (i = 0; i < len; i++) {
      read(STDIN_FILENO, &c, 1);
      if (c == '\n') {
        break;
      }
      out[i] = c;
  }
  out[i] = 0;
  return 0;
}
