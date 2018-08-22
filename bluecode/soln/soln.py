#!/usr/bin/env python2
#
# Solution for BlueCode challenge in MITRE STEM CTF
#
# Just does the reverse of bluecode and bruteforces ~3 bytes.
# Takes about 3 min on my computer. Also has potential exhaust memory...
#
# Eugene Kolodenker - eugenekolo.com
#

import hashlib
from collections import defaultdict
import math

from PIL import Image

def get_potential_hashes(data):
    potential_hashes = defaultdict(list)
    for c in data:
        for idx in range(20):
            for salt in range(0, 2**16):
                salt = str(salt)
                pepper = str(idx)
                hash = hashlib.md5(salt + c.encode('utf') + pepper).hexdigest()
                potential_hashes[hash].append(c)
    return potential_hashes

def horiz_slice(image_path, slice_size):
    img = Image.open(image_path)
    width, height = img.size
    upper = 0
    left = 0

    slices = int(math.ceil(width/slice_size))

    count = 1
    for slice in range(slices):
        if count == slices:
            lower = width
        else:
            lower = int(count * slice_size)

        bbox = (left, upper, lower, height)

        working_slice = img.crop(bbox)
        left += slice_size
        yield working_slice
        count += 1

def img_to_hash(img):
    hash = []
    for i in range(4):
        for j in range(4):
            r, g, b = img.getpixel((j * 8, i * 8))
            hash.append("%02x" % b)
    return ''.join(hash)


if __name__ == '__main__':
    possible_letters = 'MCA-0123456789abcdef'
    potential_hashes = get_potential_hashes(possible_letters)

    for img in horiz_slice('code.png', 32):
        hash = img_to_hash(img)
        if hash in potential_hashes:
            print('we good', potential_hashes[hash])
