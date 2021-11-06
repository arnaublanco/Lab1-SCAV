from rgb_yuv_conversion import rgb2yuv, yuv2rgb

# EXERCISE 1
R = 10
G = 40
B = 50
print("----------")
print("Exercise 1")
print("----------")
print("Input RGB values: (",R,",",G,",",B,")")
y,u,v = rgb2yuv(R,G,B)
print("Converted YUV values: (",y,",",u,",",v,")")

r,g,b = yuv2rgb(y,u,v)
print("Converted RGB values: (",r,",",g,",",b,")")

# EXERCISE 4

from run_length_algorithm import run_length

sequence = "AABFDAHSFJASQWDBBBBJJJKKKKWWFASJDHJ"

print("----------")
print("Exercise 4")
print("----------")
print("Input sequence:",sequence)
print("Output sequence:",run_length(sequence))
print("----------")

# EXERCISE 5

from scipy.fftpack import dct
import soundfile as sf
#import matplotlib.pyplot as plt

y,sr = sf.read("audio/song.wav")
y_comp = dct(y)
sf.write('audio/song_comp.wav',y_comp,sr)


