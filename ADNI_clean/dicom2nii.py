import dicom2nifti
import os

dicom_path = ''
nii_save_path = ''

# obtain the DICOM file list
dicom_list = os.listdir(dicom_path)
# remove the non-DICOM file from the list



for d in dicom_list:
	dicom2nifti.convert_directory(os.path.join(dicom_path, d), nii_save_path)