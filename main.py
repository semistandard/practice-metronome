# import winsound
import time
import streamlit as st
import sys

st.title('指板の音階を覚えるためのメトロノーム')
import pyaudio 
import numpy as np
 # 音声を出力するためのストリームを開く --- (*1) 
p = pyaudio.PyAudio() 
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, frames_per_buffer=1024, output=True) 
# 適当なサイン波を生成する --- (*2) 
samples = np.sin(np.arange(50000) / 20) 
# サイン波を再生する --- (*3) 
print("play") 
stream.write(samples.astype(np.float32).tostring()) 
stream.close()

#設定
beat = st.slider('拍子', 1, 10, 4)
BPM = 240
duration = 60/BPM
duration = 150
cycle = st.slider('繰り返し数', 1, 10, 2)


run_button = st.button('run')
stop_button = st.button('stop')

import pygame.midi
import random

def tone1(out, n1, vol1 ): 
    out.note_on( n1[0]+oct1*12, vol1 )
    time.sleep( n1[1] ) 
    out.note_off( n1[0]+oct1*12, vol1 )
    for _ in range(3):
        out.note_on( 50, vol1 )
        time.sleep( 0.1 ) 
        out.note_off( 50, vol1 )
        time.sleep( n1[1]-0.1 ) 



a1 = [[60, duration], [62, duration], [64, duration], [65, duration], [67, duration], [69, duration], [71, duration], [72, duration]]     # C, D, E, F, G, A, B, C 
random.shuffle(a1)

vol1 = 127 
oct1 = 0 
chn1 = 0
ins1 = 30
ins2 = 18

pygame.midi.init()
out = pygame.midi.Output(0)
out.set_instrument(ins1, chn1)

# pygame.midi.init()
# out2 = pygame.midi.Output(1)
# out2.set_instrument(ins2, 1)


for n1 in a1:
    tone1(out, n1, vol1 ) 
    # for _ in range(3):
    #     tone1(out2, n1, vol1 ) 

out.close()
# out2.close()

pygame.midi.quit()
