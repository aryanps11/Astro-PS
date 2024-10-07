import numpy as np
from datetime import datetime
import math
import sys
import os
import pandas as pd
from matplotlib import pyplot as plt
from shutil import copyfile
import astropy
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings('ignore')
from astropy.convolution import convolve, Box1DKernel
import json
import astropy.io.fits

class Flare:
    def read_file(self, file):
        if file.endswith('.lc'):
            with astropy.io.fits.open(file) as iit_bhu:
                iit_bhu.verify('fix')
                temp = iit_bhu[1].data
                data_ = pd.DataFrame(temp)
            return data_  # Return the dataframe

# Example usage
flare_ = Flare()
file = "/Users/apple/Desktop/iit_bhu/xsm/data/2024/09/18/calibrated/ch2_xsm_20240918_v1_level2.lc"

data_ = flare_.read_file(file)  # Capture the returned dataframe
print(data_)
import numpy as np

def print_flare_type(df):
    # Initialize type list
    type_ = []

    # Assuming bg and peak_value are calculated
    bg = df['RATE'][0]  # Simplified assumption for bg
    peak_value = max(df['RATE'])  # Simplified assumption for peak_value

    # Calculate points_between (for classification purposes)
    points_between = np.array(df['RATE'])  # Simplified version

    # Determine flare type
    if np.max(points_between) - bg <= 1 and np.max(points_between) > bg:
        float_value = (peak_value - bg) * 10
        format_float = "{:.1f}".format(float_value)
        type_.append(str(format_float) + 'A')

    elif np.max(points_between) - bg < 1 and np.max(points_between) <= bg:
        float_value = (peak_value - df['RATE'][0]) * 10
        format_float = "{:.1f}".format(float_value)
        type_.append(str(format_float) + 'A')

    elif np.max(points_between) - bg >= 1 and np.max(points_between) - bg < 10:
        float_value = (peak_value - bg)
        format_float = "{:.1f}".format(float_value)
        type_.append(str(format_float) + 'B')

    elif np.max(points_between) - bg >= 10 and np.max(points_between) - bg < 100:
        float_value = (peak_value - bg) / 10
        format_float = "{:.1f}".format(float_value)
        type_.append(str(format_float) + 'C')

    elif np.max(points_between) - bg >= 100 and np.max(points_between) - bg < 1000:
        float_value = (peak_value - bg) / 100
        format_float = "{:.1f}".format(float_value)
        type_.append(str(format_float) + 'M')

    elif np.max(points_between) - bg >= 1000 and np.max(points_between) - bg < 100000:
        float_value = (peak_value - bg) / 1000
        format_float = "{:.1f}".format(float_value)
        type_.append(str(format_float) + 'X')

    # Print the type of flare
    print(type_)

    
import pandas as pd
import astropy.io.fits

class Flare:
    def read_file(self, file):
        if file.endswith('.lc'):
            with astropy.io.fits.open(file) as iit_bhu:
                iit_bhu.verify('fix')
                temp = iit_bhu[1].data
                data_ = pd.DataFrame(temp)
            return data_  # Return the dataframe

# Example usage
flare_ = Flare()
file = "/Users/apple/Desktop/iit_bhu/xsm/data/2024/09/18/calibrated/ch2_xsm_20240918_v1_level2.lc"

data_ = flare_.read_file(file)  # Capture the returned dataframe

print_flare_type(data_)
