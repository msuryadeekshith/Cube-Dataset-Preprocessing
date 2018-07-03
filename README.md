# Cube-Dataset-Preprocessing

Python script for preprocessing [**Cube dataset**](http://ipg.fer.hr/ipg/resources/color_constancy#)

## Getting Started

Download the CubeDataset from [**here**](https://ferhr.sharepoint.com/:f:/s/imageprocessinggroup/Eq7zIi8T3o5Jj677YE_PIAgBTvxd0eQNTMLxCQ9ynLckog?e=a1688f96d4374a798560db3f5739d16b) and extract the png files into a directory named images.
Folder structure should look similar to the following:
```
- Cube-Dataset-Preprocessing/
                            data/
                                Cube/
                                    images/
                                          | 1.png
                                          | 2.png
                                          ...
                                    cube_gt.txt
                            CubeDataset.py
                            README.md
                            datasets.py
```

Run the following command:

  To process a single image
  ```
  python CubeDataset.py (index of image)
  ex: python CubeDataset.py 143
  ```
  To process multiple images ranging from n1 to n2
  ```
  python CubeDataset.py 15 245
  ```
  To dump processed images to pkl files
  ```
  python datasets.py
  ```
