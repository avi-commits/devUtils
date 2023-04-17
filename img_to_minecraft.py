#!/usr/bin/python3

#import PIL
from PIL import Image
import numpy as np
from collections import defaultdict


def image_to_minecraft(img_path, block_size=16, show_image=False):
    # Load the image
    img = Image.open(img_path)

    # Resize the image to the block size
    img = img.resize((img.width // block_size * block_size,
                      img.height // block_size * block_size))

    # Convert the image to a numpy array
    img = np.asarray(img)

    # Get the average color of each block
    blocks = defaultdict(int)
    for i in range(0, img.shape[0], block_size):
        for j in range(0, img.shape[1], block_size):
            block = img[i:i+block_size, j:j+block_size]
            avg_color = tuple(block.mean(axis=(0, 1)).astype(int))
            blocks[avg_color] += 1

    # Find the most common block
    most_common_block = max(blocks, key=blocks.get)

    # Print the Minecraft block corresponding to each color
    if show_image:
        import matplotlib.pyplot as plt
        plt.imshow(img)
        plt.show()

    for color, count in blocks.items():
        block = closest_block(color)
        print(f"{count} blocks of type {block}")

def closest_block(color):
    # Define the Minecraft blocks and their corresponding colors
    minecraft_blocks = {
        "Wool": (255, 255, 255),
        "Stone": (128, 128, 128),
        "Grass": (0, 255, 0),
        "Sand": (255, 255, 178),
        "Wood": (153, 76, 0),
        "Brick": (255, 0, 0),
        "Glass": (255, 255, 255),
        "Dirt": (114, 72, 56),
        "Cobblestone": (64, 64, 64),
        "Planks": (153, 76, 0),
        "Bedrock": (0, 0, 0)
    }

    # Find the Minecraft block with the closest color
    closest_block = min(minecraft_blocks, key=lambda b: euclidean_distance(color, minecraft_blocks[b]))
    return closest_block

def euclidean_distance(a, b):
    # Calculate the Euclidean distance between two colors
    return np.sqrt(np.sum((np.asarray(a) - np.asarray(b)) ** 2))


if __name__ == "__main__":
    image = '/Users/aviralchandra/Desktop/RawReels/van_gogh.jpeg'
    image_to_minecraft(image, show_image=True)