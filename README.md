# Polyp-Size-Dataset
 Instructions for preprocessing of Polyp-Size dataset
 ## Preprocess
 Run preprocess.py to convert videos into images and rename them
 ```
python preprocess.py --root YOUR_VIDEO_ROOT --output_dir YOUR_IMAGE_ROOT
 ```
## Data split
The `split` folder includes the dataset splits details for five-fold cross-validation, with file names in the format `train_{fold}.csv` and `val_{fold}.csv`. Each CSV file contains the names of the images.

## Depth estimation
We adopted [ZoeDepth] (https://github.com/isl-org/ZoeDepth) to estimate the depth of images, and we sincerely thank the authors for their outstanding contribution.

