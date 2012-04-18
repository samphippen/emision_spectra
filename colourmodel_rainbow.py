#!/sw/bin/python
# -*- coding: utf-8 -*-


def blend_value(lower, upper, lowercolor, uppercolor, value):
    along = (value-lower)*1.0/(upper-lower)
    assert along <= 1.0
    assert along >= 0
    blendcolor = [0,0,0] 
    for i in range(0,3):
        blendcolor[i] = (1.0-along)*lowercolor[i]+along*uppercolor[i]

    return tuple(blendcolor)

def angstromToRGB( wavelength, intensity ):
    t = wav2RGB(wavelength/10.0)
    return (t[0]*intensity,t[1]*intensity,t[2]*intensity)

def wav2RGB(wavelength):
    w = int(wavelength)
    print wavelength

    # colour
    if w >= 380 and w < 440:
        R = -(w - 440.) / (440. - 350.)
        G = 0.0
        B = 1.0
    elif w >= 440 and w < 490:
        R = 0.0
        G = (w - 440.) / (490. - 440.)
        B = 1.0
    elif w >= 490 and w < 510:
        R = 0.0
        G = 1.0
        B = -(w - 510.) / (510. - 490.)
    elif w >= 510 and w < 580:
        R = (w - 510.) / (580. - 510.)
        G = 1.0
        B = 0.0
    elif w >= 580 and w < 645:
        R = 1.0
        G = -(w - 645.) / (645. - 580.)
        B = 0.0
    elif w >= 645 and w <= 780:
        R = 1.0
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0

    # intensity correction
    if w >= 380 and w < 420:
        SSS = 0.3 + 0.7*(w - 350) / (420 - 350)
    elif w >= 420 and w <= 700:
        SSS = 1.0
    elif w > 700 and w <= 780:
        SSS = 0.3 + 0.7*(780 - w) / (780 - 700)
    else:
        SSS = 0.0
    SSS *= 255

    return [int(SSS*R), int(SSS*G), int(SSS*B)]
