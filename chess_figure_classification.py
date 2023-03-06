
import numpy as np
import PIL
import math
import json
from PIL import ImageFilter
import urllib.request
from fastapi import FastAPI




import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
urllib.request.urlretrieve(
  'https://lab.bpm.in.tum.de/img/high',
   "sch.png")

app = FastAPI()

w, h = 8, 8
chessboard = [[0 for x in range(w)] for y in range(h)] 



im = Image.open("sch.png")
#im.save('/Users/lukasdrobig/Documents/Master_TUM/SPA/blur_images/high_res.png', 'PNG')
enhancer = ImageEnhance.Contrast(im)

factor = 1.5 #gives original image
image = enhancer.enhance(factor)

def calculate_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)
    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)
    return 1 if brightness == 255 else brightness / scale

def adjust_brightness(brightness,image): 
    factor = 0.5-(brightness)**2
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1+factor)
    return image
    

def calculate_color(r,g,b):
    diff_blue = abs(r-0)+abs(g-0)+abs(b-255)
    #diff_blue = math.sqrt(((r-0)**2)+((g-0)**2)+((b-255)**2))
    diff_red = abs(r-255)+abs(g-0)+abs(b-0)
    diff_yellow = abs(r-255)+abs(g-255)+abs(b-0)
    #diff_red = math.sqrt(((r-255)**2)+((g-0)**2)+((b-0)**2))
    diff_white = abs(r-255)+abs(g-255)+abs(b-255)
    #diff_white = math.sqrt(((r-255)**2)+((g-255)**2)+((b-255)**2))
    diff_black = abs(r-0)+abs(g-0)+abs(b-0)
    #diff_black = math.sqrt(((r-0)**2)+((g-0)**2)+((b-0)**2))
    min_diff = min(diff_blue,diff_red,diff_yellow,diff_white,diff_black)
    if(min_diff == diff_red):
        color = 1
        return color
    if(min_diff == diff_blue): 
        color = 2
        return color
    if(min_diff == diff_yellow):
        color = 3
        return color
    if(min_diff == diff_white):
        color = 0
        return color
    if(min_diff == diff_black):
        color = 0
        return color

def calculate_average_rgb(image): 
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    for i in range(50): 
        for j in range(50):
            red,green,blue = image.getpixel((i+20,j+20))
            sum_red = sum_red+red
            sum_green = sum_green+green
            sum_blue = sum_blue+blue
            # 20x20 = 400 pixel rgb values, compute average
            
    return sum_red/2500,sum_green/2500,sum_blue/2500

imgplot = plt.imshow(image)
image = image.crop((320, 10, 1020, 710))
imgplot = plt.imshow(image)
imA1 = image.crop((0,0,90,90))
##imA1.save('turm_blau.png', 'PNG')
#shape of imA1 is 50x50
brightness = calculate_brightness(imA1)

red_avg, green_avg, blue_avg = calculate_average_rgb(imA1)

imA1plot = plt.imshow(imA1)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[0][0] =color

imA2 = image.crop((90,0,180,90))
#imA2.save('/Users/lukasdrobig/Documents/Master_TUM/SPA/blur_images/bauer_blau.png', 'PNG')
#imA2.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/bauer_blau.png', 'PNG')
brightness = calculate_brightness(imA2)
imA2 = adjust_brightness(brightness,imA2)
imA2plot = plt.imshow(imA2)
red_avg, green_avg, blue_avg = calculate_average_rgb(imA2)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[0][1] =color

imA3 = image.crop((180,0,260,85))
#imA3.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imA3.png', 'PNG')
brightness = calculate_brightness(imA3)
imA3 = adjust_brightness(brightness,imA3)
imA3plot = plt.imshow(imA3)
red_avg, green_avg, blue_avg = calculate_average_rgb(imA3)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[0][2] =color

imA4 = image.crop((260,0,350,85))
#imA4.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imA4.png', 'PNG')
imA4plot = plt.imshow(imA4)
red_avg, green_avg, blue_avg = calculate_average_rgb(imA4)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[0][3] =color

imA5 = image.crop((350,0,435,85))
#imA5.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imA5.png', 'PNG')
imA5plot = plt.imshow(imA5)
red_avg, green_avg, blue_avg = calculate_average_rgb(imA5)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[0][4] =color

imA6 = image.crop((435,0,520,85))
#imA6.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imA6.png', 'PNG')
imA6plot = plt.imshow(imA6)
red_avg, green_avg, blue_avg = calculate_average_rgb(imA6)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[0][5] =color

imA7 = image.crop((520,0,610,85))
#imA7.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imA7.png', 'PNG')
#imA7.save('/Users/lukasdrobig/Documents/Master_TUM/SPA/blur_images/bauer_gelb.png', 'PNG')
imA7plot = plt.imshow(imA7)
red_avg, green_avg, blue_avg = calculate_average_rgb(imA7)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[0][6] =color

imA8 = image.crop((610,0,700,85))
#imA8.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imA8.png', 'PNG')
#imA8.save('/Users/lukasdrobig/Documents/Master_TUM/SPA/blur_images/turm_gelb.png', 'PNG')
imA8plot = plt.imshow(imA8)
red_avg, green_avg, blue_avg = calculate_average_rgb(imA8)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[0][7] =color

imB1 = image.crop((0,85,90,170))
#imB1.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imB1.png', 'PNG')
#imB1.save('/Users/lukasdrobig/Documents/Master_TUM/SPA/blur_images/pferd_blau.png', 'PNG')
imB1plot = plt.imshow(imB1)
red_avg, green_avg, blue_avg = calculate_average_rgb(imB1)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[1][0] =color

imB2 = image.crop((90,85,180,170))
#imB2.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imB2.png', 'PNG')
#imB2.save('/Users/lukasdrobig/Documents/Master_TUM/SPA/blur_images/bauer_blau.png', 'PNG')
imB2plot = plt.imshow(imB2)
red_avg, green_avg, blue_avg = calculate_average_rgb(imB2)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[1][1] =color

imB3 = image.crop((180,85,265,170))
#imB3.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imB3.png', 'PNG')
imB3plot = plt.imshow(imB3)
red_avg, green_avg, blue_avg = calculate_average_rgb(imB3)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[1][2] =color

imB4 = image.crop((265,85,350,170))
#imB4.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imB4.png', 'PNG')
imB4plot = plt.imshow(imB4)
red_avg, green_avg, blue_avg = calculate_average_rgb(imB4)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[1][3] =color

imB5 = image.crop((350,85,435,170))
#imB5.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imB5.png', 'PNG')
imB5plot = plt.imshow(imB5)
red_avg, green_avg, blue_avg = calculate_average_rgb(imB5)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[1][4] =color


imB6 = image.crop((435,85,520,170))
#imB6.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imB6.png', 'PNG')
imB6plot = plt.imshow(imB6)
red_avg, green_avg, blue_avg = calculate_average_rgb(imB6)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[1][5] =color


imB7 = image.crop((520,85,610,170))
#imB7.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imB7.png', 'PNG')
#imB7.save('/Users/lukasdrobig/Documents/Master_TUM/SPA/blur_images/bauer_geld.png', 'PNG')
imB7plot = plt.imshow(imB7)
red_avg, green_avg, blue_avg = calculate_average_rgb(imB7)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[1][6] =color

imB8 = image.crop((610,85,700,170))
#imB8.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imB8.png', 'PNG')
#imB8.save('/Users/lukasdrobig/Documents/Master_TUM/SPA/blur_images/pferd_gelb.png', 'PNG')
imB8plot = plt.imshow(imB8)
red_avg, green_avg, blue_avg = calculate_average_rgb(imB8)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[1][7] =color

imC1 = image.crop((0,170,90,255))
#imC1.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imC1.png', 'PNG')
#imC1.save('/Users/lukasdrobig/Documents/Master_TUM/SPA/blur_images/laufer_blau.png', 'PNG')
imC1plot = plt.imshow(imC1)
red_avg, green_avg, blue_avg = calculate_average_rgb(imC1)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[2][0] =color

imC2 = image.crop((90,170,180,255))
#imC2.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imC2.png', 'PNG')
#imC2.save('/Users/lukasdrobig/Documents/Master_TUM/SPA/blur_images/bauer_blau.png', 'PNG')
imC2plot = plt.imshow(imC2)
red_avg, green_avg, blue_avg = calculate_average_rgb(imC2)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[2][1] =color

imC3 = image.crop((180,170,265,255))
#imC3.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imC3.png', 'PNG')
imC3plot = plt.imshow(imC3)
red_avg, green_avg, blue_avg = calculate_average_rgb(imC3)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[2][2] =color

imC4 = image.crop((265,170,350,255))
#imC4.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imC4.png', 'PNG')
imC4plot = plt.imshow(imC4)
red_avg, green_avg, blue_avg = calculate_average_rgb(imC4)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[2][3] =color

imC5 = image.crop((350,170,435,255))
#imC5.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imC5.png', 'PNG')
imC5plot = plt.imshow(imC5)
red_avg, green_avg, blue_avg = calculate_average_rgb(imC5)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[2][4] =color

imC6 = image.crop((435,170,520,255))
#imC6.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imC6.png', 'PNG')
imC6plot = plt.imshow(imC6)
red_avg, green_avg, blue_avg = calculate_average_rgb(imC6)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[2][5] =color

imC7 = image.crop((520,170,610,255))
#imC8.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imC8.png', 'PNG')
#imC7.save('/Users/lukasdrobig/Documents/Master_TUM/SPA/blur_images/turm_blau.png', 'PNG')
imC7plot = plt.imshow(imC7)
red_avg, green_avg, blue_avg = calculate_average_rgb(imC7)
chessboard[2][6] =color
color = calculate_color(red_avg,green_avg,blue_avg)

imC8 = image.crop((610,170,700,255))
#imC8.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imC8.png', 'PNG')
#imC8.save('/Users/lukasdrobig/Documents/Master_TUM/SPA/blur_images/turm_blau.png', 'PNG')
imC8plot = plt.imshow(imC8)
red_avg, green_avg, blue_avg = calculate_average_rgb(imC8)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[2][7] =color
imD1 = image.crop((5,255,90,340))
#imD1.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imD1.png', 'PNG')
brightness = calculate_brightness(imD1)

imD1 = adjust_brightness(brightness,imD1)
imD1plot = plt.imshow(imD1)
red_avg, green_avg, blue_avg = calculate_average_rgb(imD1)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[3][0] =color
imD2 = image.crop((90,255,180,340))
#imD2.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imD2.png', 'PNG')
brightness = calculate_brightness(imD2)

imD2 = adjust_brightness(brightness,imD2)
imD2plot = plt.imshow(imD2)
red_avg, green_avg, blue_avg = calculate_average_rgb(imD2)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[3][1] =color
imD3 = image.crop((180,255,265,340))
#imD3.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imD3.png', 'PNG')
imD3plot = plt.imshow(imD3)
red_avg, green_avg, blue_avg = calculate_average_rgb(imD3)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[3][2] =color
imD4 = image.crop((265,255,350,340))
#imD4.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imD4.png', 'PNG')
imD4plot = plt.imshow(imD4)
red_avg, green_avg, blue_avg = calculate_average_rgb(imD4)
color = calculate_color(red_avg,green_avg,blue_avg)

chessboard[3][3] =color
imD5 = image.crop((350,255,435,340))
#imD5.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imD5.png', 'PNG')
imD5plot = plt.imshow(imD5)
red_avg, green_avg, blue_avg = calculate_average_rgb(imD5)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[3][4] =color
imD6 = image.crop((435,255,520,340))
#imD6.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imD6.png', 'PNG')
imD6plot = plt.imshow(imD6)
red_avg, green_avg, blue_avg = calculate_average_rgb(imD6)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[3][5] =color
imD7 = image.crop((520,255,610,340))
#imD7.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imD7.png', 'PNG')
brightness = calculate_brightness(imD7)

imD7 = adjust_brightness(brightness,imD7)
imD7plot = plt.imshow(imD7)
red_avg, green_avg, blue_avg = calculate_average_rgb(imD7)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[3][6] =color
imD8 = image.crop((610,255,700,340))
#imD8.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imD8.png', 'PNG')

brightness = calculate_brightness(imD8)

imD8 = adjust_brightness(brightness,imD8)
imD8plot = plt.imshow(imD8)
red_avg, green_avg, blue_avg = calculate_average_rgb(imD8)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[3][7] =color
imE1 = image.crop((0,340,90,425))

#imE1.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imE1.png', 'PNG')
brightness = calculate_brightness(imE1)

imE1 = adjust_brightness(brightness,imE1)
imE1plot = plt.imshow(imE1)
red_avg, green_avg, blue_avg = calculate_average_rgb(imE1)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[4][0] =color
imE2 = image.crop((90,340,180,425))
#imE2.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imE2.png', 'PNG')
brightness = calculate_brightness(imE2)

imE2 = adjust_brightness(brightness,imE2)
imE2plot = plt.imshow(imE2)
red_avg, green_avg, blue_avg = calculate_average_rgb(imE2)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[4][1] =color
imE3 = image.crop((180,340,265,425))
#imE3.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imE3.png', 'PNG')
imE3plot = plt.imshow(imE3)
red_avg, green_avg, blue_avg = calculate_average_rgb(imE3)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[4][2] =color
imE4 = image.crop((265,340,350,425))
#imE4.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imE4.png', 'PNG')
imE4plot = plt.imshow(imE4)
red_avg, green_avg, blue_avg = calculate_average_rgb(imE4)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[4][3] =color
imE5 = image.crop((350,340,435,425))
#imE5.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imE5.png', 'PNG')
imE5plot = plt.imshow(imE5)
red_avg, green_avg, blue_avg = calculate_average_rgb(imE5)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[4][4] =color
imE6 = image.crop((435,340,520,425))
#imE6.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imE6.png', 'PNG')
imE6plot = plt.imshow(imE6)
red_avg, green_avg, blue_avg = calculate_average_rgb(imE6)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[4][5] =color
imE7 = image.crop((520,340,605,425))
#imE7.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imE7.png', 'PNG')
brightness = calculate_brightness(imE7)

imE7 = adjust_brightness(brightness,imE7)
imE7plot = plt.imshow(imE7)
red_avg, green_avg, blue_avg = calculate_average_rgb(imE7)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[4][6] =color
imE8 = image.crop((605,340,700,425))
#imE8.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imE8.png', 'PNG')
imE8plot = plt.imshow(imE8)
red_avg, green_avg, blue_avg = calculate_average_rgb(imE8)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[4][7] =color

imF1 = image.crop((5,425,90,510))
#imF1.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imF1.png', 'PNG')
brightness = calculate_brightness(imF1)
imF1 = adjust_brightness(brightness,imF1)
imF1plot = plt.imshow(imF1)
red_avg, green_avg, blue_avg = calculate_average_rgb(imF1)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[5][0] = color

imF2 = image.crop((90,425,180,510))
#imF2.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imF2.png', 'PNG')
brightness = calculate_brightness(imF2)
imF2 = adjust_brightness(brightness,imF2)
imF2plot = plt.imshow(imF2)
red_avg, green_avg, blue_avg = calculate_average_rgb(imF2)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[5][1] = color

imF3 = image.crop((180,425,265,510))
#imF3.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imF3.png', 'PNG')
brightness = calculate_brightness(imF3)
imF3 = adjust_brightness(brightness,imF3)
imF3plot = plt.imshow(imF3)
red_avg, green_avg, blue_avg = calculate_average_rgb(imF3)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[5][2] = color

imF4 = image.crop((265,425,350,510))
#imF4.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imF4.png', 'PNG')
brightness = calculate_brightness(imF4)
imF4 = adjust_brightness(brightness,imF4)
imF4plot = plt.imshow(imF4)
red_avg, green_avg, blue_avg = calculate_average_rgb(imF4)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[5][3] = color

imF5 = image.crop((350,425,435,510))
#imF5.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imF5.png', 'PNG')
brightness = calculate_brightness(imF5)
imF5 = adjust_brightness(brightness,imF5)
imF5plot = plt.imshow(imF5)
red_avg, green_avg, blue_avg = calculate_average_rgb(imF5)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[5][4] = color

imF6 = image.crop((435,425,520,510))
#imF6.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imF6.png', 'PNG')
brightness = calculate_brightness(imF6)
imF6 = adjust_brightness(brightness,imF6)
imF6plot = plt.imshow(imF6)
red_avg, green_avg, blue_avg = calculate_average_rgb(imF6)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[5][5] = color

imF7 = image.crop((520,425,610,510))
#imF7.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imF7.png', 'PNG')
brightness = calculate_brightness(imF7)
imF7 = adjust_brightness(brightness,imF7)
imF7plot = plt.imshow(imF7)
red_avg, green_avg, blue_avg = calculate_average_rgb(imF7)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[5][6] = color

imF8 = image.crop((610,425,700,510))
#imF8.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imF8.png', 'PNG')
brightness = calculate_brightness(imF8)
imF8 = adjust_brightness(brightness,imF8)
imF8plot = plt.imshow(imF8)
red_avg, green_avg, blue_avg = calculate_average_rgb(imF8)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[5][7] = color

imG1 = image.crop((0,510,90,600))
#imG1.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imG1.png', 'PNG')
imG1plot = plt.imshow(imG1)
red_avg, green_avg, blue_avg = calculate_average_rgb(imG1)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[6][0] = color

imG2 = image.crop((90,510,180,600))
#imG2.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imG2.png', 'PNG')
brightness = calculate_brightness(imG2)
imG2 = adjust_brightness(brightness,imG2)
imG2plot = plt.imshow(imG2)
red_avg, green_avg, blue_avg = calculate_average_rgb(imG2)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[6][1] = color

imG3 = image.crop((180,510,265,595))
#imG3.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imG3.png', 'PNG')
brightness = calculate_brightness(imG3)
imG3 = adjust_brightness(brightness,imG3)
imG3plot = plt.imshow(imG3)
red_avg, green_avg, blue_avg = calculate_average_rgb(imG3)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[6][2] = color

imG4 = image.crop((265,510,350,595))
#imG4.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imG4.png', 'PNG')
brightness = calculate_brightness(imG4)
imG4 = adjust_brightness(brightness,imG4)
imG4plot = plt.imshow(imG4)
red_avg, green_avg, blue_avg = calculate_average_rgb(imG4)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[6][3] = color

imG5 = image.crop((350,510,435,595))
#imG5.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imG5.png', 'PNG')
brightness = calculate_brightness(imG5)
imG5 = adjust_brightness(brightness,imG5)
imG5plot = plt.imshow(imG5)
red_avg, green_avg, blue_avg = calculate_average_rgb(imG5)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[6][4] = color

imG6 = image.crop((435,510,520,595))
#imG6.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imG6.png', 'PNG')
imG6plot = plt.imshow(imG6)
red_avg, green_avg, blue_avg = calculate_average_rgb(imG6)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[6][5] = color

imG7 = image.crop((520,510,610,600))
#imG7.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imG7.png', 'PNG')
brightness = calculate_brightness(imG7)
imG7 = adjust_brightness(brightness,imG7)
imG7plot = plt.imshow(imG7)
red_avg, green_avg, blue_avg = calculate_average_rgb(imG7)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[6][6] = color

imG8 = image.crop((610,510,700,600))
#imG8.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imG8.png', 'PNG')
brightness = calculate_brightness(imG8)
imG8 = adjust_brightness(brightness,imG8)
imG8plot = plt.imshow(imG8)
red_avg, green_avg, blue_avg = calculate_average_rgb(imG8)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[6][7] = color

imH1 = image.crop((0,600,90,690))
#imH1.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imH1.png', 'PNG')
brightness = calculate_brightness(imH1)
imH1 = adjust_brightness(brightness,imH1)
imH1plot = plt.imshow(imH1)
red_avg, green_avg, blue_avg = calculate_average_rgb(imH1)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[7][0] = color

imH2 = image.crop((90,600,180,690))
#imH2.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imH2.png', 'PNG')
brightness = calculate_brightness(imH2)
imH2 = adjust_brightness(brightness,imH2)
imH2plot = plt.imshow(imH2)
red_avg, green_avg, blue_avg = calculate_average_rgb(imH2)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[7][1] = color

imH3 = image.crop((180,600,265,690))
#imH3.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imH3.png', 'PNG')
brightness = calculate_brightness(imH3)

imH3 = adjust_brightness(brightness,imH3)
imH3plot = plt.imshow(imH3)
red_avg, green_avg, blue_avg = calculate_average_rgb(imH3)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[7][2] = color

imH4 = image.crop((265,600,350,690))
#imH4.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imH4.png', 'PNG')
brightness = calculate_brightness(imH4)
imH4 = adjust_brightness(brightness,imH4)
imH4plot = plt.imshow(imH4)
red_avg, green_avg, blue_avg = calculate_average_rgb(imH4)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[7][3] = color

imH5 = image.crop((350,600,435,690))
#imH5.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imH5.png', 'PNG')
brightness = calculate_brightness(imH5)
imH5 = adjust_brightness(brightness,imH5)
imH5plot = plt.imshow(imH5)
red_avg, green_avg, blue_avg = calculate_average_rgb(imH5)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[7][4] = color

imH6 = image.crop((435,600,520,690))
#imH6.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imH6.png', 'PNG')
brightness = calculate_brightness(imH6)
imH6 = adjust_brightness(brightness,imH6)
imH6plot = plt.imshow(imH6)
red_avg, green_avg, blue_avg = calculate_average_rgb(imH6)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[7][5] = color

imH7 = image.crop((520,600,610,690))
#imH7.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imH7.png', 'PNG')
brightness = calculate_brightness(imH7)
imH7 = adjust_brightness(brightness,imH7)
imH7plot = plt.imshow(imH7)
red_avg, green_avg, blue_avg = calculate_average_rgb(imH7)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[7][6] = color

imH8 = image.crop((610,600,700,690))
#imH8.save('/Users/lukasdrobig/Documents/Master_TUM/schach_bilder/imH8.png', 'PNG')
brightness = calculate_brightness(imH8)
imH8 = adjust_brightness(brightness,imH8)
imH8plot = plt.imshow(imH8)
red_avg, green_avg, blue_avg = calculate_average_rgb(imH8)
color = calculate_color(red_avg,green_avg,blue_avg)
chessboard[7][7] = color




@app.get("/chess/")
async def root():
    return json.dumps(chessboard)


