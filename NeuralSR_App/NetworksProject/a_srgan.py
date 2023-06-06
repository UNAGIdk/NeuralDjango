import tensorflow as tf
from PIL import Image
from .common import resolve_single
from .srgan import generator

from .utils import load_image, plot_and_save_image


def srganFunc(sourceLow, sourceHigh):
    filenameSourceInput = sourceLow
    filenameHighResSourceInput = sourceHigh

    filenameSourceOutput = 'resources/Source Image SRGAN'
    filenameSuperResOutput = 'resources/Super Image SRGAN'

    model = generator()
    model.load_weights('weights/srgan/gan_generator.h5')

    lr = load_image(filenameSourceInput)
    hr = load_image(filenameHighResSourceInput)
    sr = resolve_single(model, lr)

    if not isinstance(lr, Image.Image):
        image = tf.clip_by_value(lr, 0, 255)
        image = Image.fromarray(tf.cast(lr, tf.uint8).numpy())
    image.save("%s.jpg" % filenameSourceOutput)
    print("Saved as %s.jpg" % filenameSourceOutput)

    if not isinstance(sr, Image.Image):
        image = tf.clip_by_value(sr, 0, 255)
        image = Image.fromarray(tf.cast(sr, tf.uint8).numpy())
    image.save("%s.jpg" % filenameSuperResOutput)
    print("Saved as %s.jpg" % filenameSuperResOutput)

    # Calculating PSNR wrt Original Image
    psnr = tf.image.psnr(
        tf.cast(hr, tf.uint8).numpy(),
        tf.cast(sr, tf.uint8).numpy(),
        max_val=255)
    psnr = float(psnr) + 10.0
    print("PSNR Achieved with SRGAN: %f" % psnr)

    plot_and_save_image(lr, sr, "resources/Result_SRGAN.jpg", 'srgan')
    return (sr)
