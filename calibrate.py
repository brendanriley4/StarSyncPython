from magCalibration import process_data, ellipsoid_fit, compute_correction_matrix, apply_calibration, plot_data


# Example data received via Bluetooth as a single long string
data_string = ("-15.3,24.7,9.1,-16.2,25.3,8.9,-15.1,24.9,9.0,-15.7,24.5,8.8,-15.8,25.0,9.2,-15.5,25.1,9.3,"
               "-15.0,24.6,9.0,-15.6,25.2,9.1,-16.1,24.8,8.7,-15.9,25.4,9.4,-16.3,24.9,8.6,-15.2,25.0,9.5,"
               "-15.4,24.8,9.3,-16.0,24.7,8.5,-15.1,24.7,9.2,-15.3,25.2,9.6,-15.9,25.1,8.9,-16.2,25.0,8.4,"
               "-15.0,24.8,9.4,-15.8,24.6,9.1,-15.7,25.3,8.8,-16.1,24.7,9.0,-15.5,24.9,9.5,-15.2,25.1,9.7,"
               "-16.0,25.2,8.6,-15.6,24.7,9.2,-15.9,24.5,9.3,-15.1,25.3,8.7,-15.8,25.0,9.4,-16.3,24.8,8.5,"
               "-15.4,24.6,9.6,-15.3,25.4,8.9,-15.7,25.1,9.0,-16.2,24.9,9.2,-15.0,25.0,8.8,-15.5,24.8,9.7,"
               "-16.1,25.2,9.1,-15.9,24.7,9.4,-15.6,25.3,8.6,-15.2,24.9,8.7,-15.8,25.4,9.5,-16.0,24.8,8.4,"
               "-15.1,25.1,9.3,-15.7,24.6,9.6,-16.3,25.0,8.5,-15.4,24.7,9.8,-15.3,25.2,9.0,-15.9,25.3,9.2,"
               "-16.1,24.5,8.9,-15.0,25.4,9.4,-15.5,24.6,8.8,-15.2,25.0,9.6,-15.8,25.1,9.1,-16.0,24.9,8.3,"
               "-15.7,25.2,8.7,-16.2,24.8,9.0,-15.6,25.3,9.5,-15.9,24.7,9.3,-15.1,25.4,8.6,-15.3,24.9,9.7,"
               "-16.3,25.0,8.4,-15.4,24.8,9.9,-15.0,25.2,9.1,-15.8,25.3,9.0,-16.1,24.6,8.8,-15.5,25.1,9.8,"
               "-15.2,24.7,9.4,-15.7,25.4,8.9,-16.0,25.2,9.3,-15.9,24.5,8.7,-15.6,25.0,9.6,-16.2,24.9,8.5,"
               "-15.1,25.3,9.2,-15.8,24.6,9.7,-15.3,25.1,8.8,-15.7,24.8,9.5,-16.3,25.2,8.6,-15.0,24.9,9.9,"
               "-15.4,25.0,9.0,-15.2,24.7,9.8")

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

plot_data(magM, calibrated_data)
