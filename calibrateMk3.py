from magCalibrationMk3 import Magnetometer
import numpy as np


def file_to_string(filepath):
    with open(filepath, 'r') as file:
        data_string = file.read().replace('\n', ',')
    return data_string


data_string = file_to_string('mag_out.txt')

magnetometer = Magnetometer()
string_output = magnetometer.calibrate(data_string)

print(string_output)
