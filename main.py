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

# #設定
# beat = st.slider('拍子', 1, 10, 4)
# BPM = st.slider('BPM', 1, 200, 120)
# scale = 0 #音の高さ
# duration = 150
# cycle = st.slider('繰り返し数', 1, 10, 2)


# run_button = st.button('run')
# stop_button = st.button('stop')


# tone_d = scale - 9
# beep = int(440*2**(tone_d/12)) #周波数
# sleep_time = (60/BPM) - (duration/1000)
# major = [0,2,4,5,7,9,11,12]
# scales = []
# for interval in major:
#     tone_d = scale - 9 + interval
#     freq = int(440*2**(tone_d/12))
#     scales.append(freq)
# scales *= cycle

# if run_button:
#     for freq in scales:
#         if stop_button:
#             sys.exit()
#         winsound.Beep(2*freq,int(duration))
#         time.sleep(sleep_time)
#         for _ in range(beat-1):
#             winsound.Beep(beep,int(duration))
#             time.sleep(sleep_time)
