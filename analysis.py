import numpy as np 
import matplotlib.pyplot as plt
import h5py     
from scipy.signal import find_peaks 
from scipy import stats
import os 
from tara_analysis import Nanopore


Control = Nanopore(file="C:/Users/tm763/Documents/Nano_MRes/Mini_1/nanopore_analysis/TM_1_A_111_control_1")
Control.filter_noise(level=0.04)


for event in Control.event_list_ln[0:10]:
    Control.plot_one_event(event, peaks=True)

cas = [109,130,153,161,184,217,225,265,279,282,289,291,310,313,330,342,334,356,359,365,372,382,389,393,397,401,435,436,443,473,474,503]
control1 = [6, 44, 98, 112, 135, 206, 225, 246]
control2 = [39, 50, 56, 57, 66, 69, 89, 113, 114,118,143,147,154,156,159,187,192,214,220,235,236,248]