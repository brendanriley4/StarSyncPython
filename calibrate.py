from magCalibration import process_data, ellipsoid_fit, compute_correction_matrix, apply_calibration

# Example data received via Bluetooth as a single long string
data_string = ("23.5,-34.2,45.1,22.0,-33.5,44.8,21.8,-35.0,46.3,-23.7,56.2,-1.2,"
               "22.5,-45.6,10.1,-10.5,48.9,-5.3,24.1,-35.2,46.0,21.0,-34.5,43.8,"
               "20.8,-36.0,45.3,-24.7,57.2,0.2,23.5,-46.6,11.1,-11.5,49.9,-4.3,"
               "23.8,-35.1,44.9,20.9,-33.4,44.7,19.7,-34.0,47.2,-22.7,55.2,2.2,21.5,-45.6,12.1,-12.5,50.9,-6.3")

# Processing the data to transform into the correct format
magM = process_data(data_string)

# Fitting the ellipsoid to the magnetometer data
fit_params = ellipsoid_fit(magM)

# Computing the correction matrices from the ellipsoid fit parameters
translation, correction_matrix = compute_correction_matrix(fit_params)

# Applying the calibration to the magnetometer data
calibrated_data = apply_calibration(magM, translation, correction_matrix)

# Optionally, print or return the calibrated data
print("Calibrated Magnetometer Data:\n", calibrated_data)
