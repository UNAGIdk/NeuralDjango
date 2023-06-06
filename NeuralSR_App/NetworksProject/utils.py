import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from PIL import Image


def load_image(path):
    return np.array(Image.open(path))


def plot_and_save_image(lr, sr, outputPath, modelType):
    # plt.figure(figsize=(20, 10))

    # images = [lr, sr]
    # titles = ['LR', f'SR (x{sr.shape[0] // lr.shape[0]})']
    # titles = ['LR', 'SR']

    # for i, (img, title) in enumerate(zip(images, titles)):
    # plt.rcParams['figure.figsize'] = [8, 5]
    # plt.subplots(1, 2)

    # plt.rcParams['figure.figsize'] = [10, 15]
    fig, axes = plt.subplots(1, 2)
    fig.set_figheight(5)
    fig.set_figwidth(10)

    fig.tight_layout()
    plt.subplot(121)
    plt.title('Source Image')
    plt.imshow(lr)
    plt.axis("off")

    plt.subplot(122)
    fig.tight_layout()
    if modelType == 'edsr':
        plt.title('EDSR Super Resolution')
    elif modelType == 'wdsr':
        plt.title('WDSR Super Resolution')
    elif modelType == 'srgan':
        plt.title('SRGAN Super Resolution')
    plt.imshow(sr)
    plt.axis("off")

    plt.savefig(outputPath, bbox_inches="tight")

    plt.show()
