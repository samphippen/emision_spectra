#!/usr/bin/python
import Image, ImageDraw

#import colourmodel_rainbow
from colourmodel_monotone import angstromToRGB
colourModule = __import__( "colourmodel_rainbow" );

#def angstromToRGB( wavelength, intensity ):
import scarves;
scarves.angstromToRGB = colourModule.angstromToRGB;
#if( singleStripes ):
        #scarves.visualIntensityToColumns = lambda x, y: 1;
#        pass;
totalLength = 1280/2
borderLength = 2.5
rowLength = 0.5
lowerBand = 4000
upperBand = 8000
x = "<html><head><title>Spectrum!</title></head><body>"
element = "H"
colors = scarves.designScarf( totalLength, rowLength, borderLength, element, lowerBand, upperBand ) ;
height = 800
im = Image.new("RGB", (totalLength*2, height))
for i in range(0,len(colors)):
        c = colors[i]
        superColor = (int(c[0]*255), int(c[1]*255), int(c[2]*255))
        for j in range(0, height):
            im.putpixel((i,j), superColor)

im.save("bees.png", "PNG")



