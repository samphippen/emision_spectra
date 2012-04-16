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
    if( wavelength < 3800 ):
        wavelengthColour = (0.0, 0.0, 0.0);
    # violet
    if( wavelength >= 3800 and wavelength < 4200 ):
        wavelengthColour = blend_value(3800,4200, (0,0,0), (0.5,0.0,1.0), wavelength)
    # indigo
    if( wavelength >= 4200 and wavelength < 4400 ):
        wavelengthColour = blend_value(4200, 4400, (0.5,0.0,1.0), (0.3, 0.0, 0.5), wavelength)
    # blue
    if( wavelength >= 4400 and wavelength < 5200 ):
        wavelengthColour = blend_value(4400, 5200, (0.3,0.0,0.5), (0.0, 0.0, 1.0), wavelength)
    # green
    if( wavelength >= 5200 and wavelength < 5700 ):
        wavelengthColour = blend_value(5200, 5700, (0.0, 0.0, 1.0), (0.0,1.0,0.0), wavelength)
    # yellow
    if( wavelength >= 5700 and wavelength < 5850 ):
        wavelengthColour = blend_value(5700, 5850, (0.0,1.0,0.0), (1.0,1.0,0.0), wavelength)
    # orange
    if( wavelength >= 5850 and wavelength < 6300 ):
        wavelengthColour = blend_value(5850, 6300, (1.0,1.0,0.0), (1.0,0.5,0.0), wavelength)
    # red
    if( wavelength >= 6300 and wavelength < 7400 ):
        wavelengthColour = blend_value(6300, 7400, (1.0,0.5,0.0),(1.0,0.0,0.0), wavelength)
    if( wavelength >= 7400 ):
        wavelengthColour = (0.0, 0.0, 0.0);
    return tuple( [x * intensity for x in wavelengthColour] );
