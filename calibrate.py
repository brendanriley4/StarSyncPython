from magCalibrationMk2 import Magnetometer, plot_magnetometer_data
import numpy as np


def file_to_string(filepath):
    with open(filepath, 'r') as file:
        data_string = file.read().replace('\n', ',')
    return data_string


data_string = file_to_string('mag_out.txt')

magnetometer = Magnetometer()
calibrated_data = magnetometer.calibrate(data_string)
print("Calibrated data:\n", calibrated_data)

data_list = data_string.split(',')

data_floats = list(map(float, data_list))

# Group the list into sublist of three (since each point is represented by three values: X, Y, Z)
grouped_data = [data_floats[i:i+3] for i in range(0, len(data_floats), 3)]

# Convert to a NumPy array
original_data = np.array(grouped_data)

# Call the plotting function
plot_magnetometer_data(original_data, calibrated_data)
