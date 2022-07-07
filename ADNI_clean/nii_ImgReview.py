import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D


example_path = 'ADNI_002_S_0816_MR_MPR____N3__Scaled_2_Br_20081001115756935_S19532_I118684.nii'

img = nib.load(example_path)

print(img)
print(img.header['db_name'])

# width, height, queue
W, H, Q = img.dataobj.shape

OrthoSlicer3D(img.dataobj).show()

num = 1

for i in range(0, Q, 10):
	img_arr = img.dataobj[:, :, i]

	plt.subplot(5, 4, num)
	plt.imshow(img_arr, cmap = 'gray')
	num += 1

plt.show()

