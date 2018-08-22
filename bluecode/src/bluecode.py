#!/usr/bin/env python2
#
# BlueCode challenge for MITRE STEM CTF
#

import hashlib
import random

from PIL import Image

FLAG = 'MCA-27c0384c33a93172'
assert len(FLAG) == 20

def data_to_hashes(data):
    for idx, c in enumerate(data):
        salt = str(random.randint(0, 2**16-1))
        pepper = str(idx)
        myhash = hashlib.md5(salt + c.encode('utf') + pepper).hexdigest()
        yield myhash

def sha1_to_image(hash):
    # Create a list of big pixels
    pixels = []
    for idx, b in enumerate(range(0, 32, 2)):
        blue = int(hash[b:b+2], 16)
        for _ in range(64):
            pixels.append((0, 0, blue))

    # Grow the image from a 4x4 to a 32x32
    big_img = []
    for big_row in range(4):
        for row in range(8):
            for col in range(4):
                idx = row*8 + col*8*8 + big_row*64*4
                big_pixel_row = pixels[idx:idx+8]
                big_img.extend(big_pixel_row)

    img = Image.new('RGB', (32, 32))
    img.putdata(big_img)
    return img

def images_to_code(imgs):
    widths, heights = zip(*(part.size for part in imgs))
    total_width = sum(widths)
    max_height = max(heights)

    img = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for part in imgs:
        img.paste(part, (x_offset, 0))
        x_offset += part.size[0]

    img.save('code.png')
    return img

digits = []
for hash in data_to_hashes(FLAG):
    img = sha1_to_image(hash)
    digits.append(img)

img = images_to_code(digits)
img.show()
