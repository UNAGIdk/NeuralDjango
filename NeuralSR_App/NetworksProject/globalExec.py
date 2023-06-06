from .a_edsr import edsrFunc
from .a_wdsr import wdsrFunc
from .a_srgan import srganFunc


def globalExec(source, networktype):

    lowResglobalSource = source
    highResGlobalSource = 'demo/manHR.jpg'

    if (networktype == 'edsrVal'):
        output = edsrFunc(lowResglobalSource, highResGlobalSource)

    if (networktype == 'wdsrVal'):
        output = wdsrFunc(lowResglobalSource, highResGlobalSource)

    if (networktype == 'srganVal'):
        output = srganFunc(lowResglobalSource, highResGlobalSource)

    return '123123'


# lowResglobalSource = 'demo/manLR.jpg'
# highResGlobalSource = 'demo/manHR.jpg'

# edsrFunc(lowResglobalSource, highResGlobalSource)

# wdsrFunc(lowResglobalSource, highResGlobalSource)

# srganFunc(lowResglobalSource, highResGlobalSource)
