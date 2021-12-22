#!/usr/bin/env python3
"""
brief: Hlavni skript resici projekt z ISS, VUT FIT 2021/2022

file:   main.py
date:   07.01.2022
author: Hung Do
"""

import os
import numpy as np
from scipy.io import wavfile
# from scipy.signal import spectogram, lfilter, freqz, tf2zpk
import matplotlib.pyplot as plt

lof_frames = list()


def get_audio_path(filename: str) -> str:
    """
    Vygeneruje cestu ke zdroji zvuku

    Keyword arguments:

    filename: jmeno souboru
    """
    src_dir = os.path.abspath(os.path.join(os.path.join(__file__, os.pardir)))
    parent_dir = os.path.abspath(os.path.join(src_dir, os.pardir))
    return os.path.abspath(os.path.join(parent_dir, 'audio/', filename))


def task1():
    """Prvni ukol"""

    # delka signalu
    time_len = data.size / fs

    # vypis informaci
    print(f"Pocet vzorku: {data.size}")
    print(f"Delka signalu: {time_len}")
    print(f"Max: {data.max()}")
    print(f"Min: {data.min()}")

    # vykresleni grafu
    time = np.arange(data.size)
    plt.figure(figsize=(6, 3))
    plt.plot(time, data)

    # pojmenovani os
    plt.gca().set_xlabel('$t[s]$')
    plt.gca().set_title('Zvukovy signal')
    plt.tight_layout()


def task2():
    """Druhy ukol"""
    global data

    # vypocet stredni hodnoty
    mean = sum(data) / data.size

    # odecteni stredni hodnoty
    data = data - mean

    # normalizace signalu
    data = data / 2**15

    # vytvoreni ramcu o velikosti 1024 vzorku s presahem 512 vzorku
    i = 0
    while True:
        # zarovnani posledniho ramce a ukonceni cyklu
        if i + 1024 > data.size:
            lof_frames.append(data[i:data.size - 1])
            break
        lof_frames.append(data[i:i + 1024])
        i += 512

    # vytvoreni noveho grafu
    time = np.arange(1024) / fs
    plt.figure(figsize=(6, 3))
    plt.plot(time, lof_frames[0])

    # pojmenovani os
    plt.gca().set_xlabel('$t[s]$')
    plt.gca().set_title('Zvukovy signal')
    plt.tight_layout()


def task3():
    """Treti ukol"""
    # data = lof_frames[0]
    # N = 1024
    # TODO:
    pass


# absolutni cesta ke zdroji zvuku
# spojeni _parent_dir_ a audio/xlogin00.wav
PATH_TO_AUDIO = get_audio_path('xdohun00.wav')

fs, data = wavfile.read(PATH_TO_AUDIO)
task1()
# otevreni okna s grafem
task2()
plt.show()
