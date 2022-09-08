# README Code samples and tools

We provide examples in MATLAB, Python and R to show the use of data exported using AK Frame Extractor. Data and images
can be uploaded with common routines in MATLAB.

| Folder                    | Description                                                                                                                                                                                                     |
|---------------------------|-----------------------------|
| tools/matlab_examples     |  test_ak_simple_data_load.m |
|                           |  test_ak_data_extracted.m   |
| tools/python_examples     |  test_ak_data_extracted.py  |
| tools/R_examples          | test_ak_simple_data_load.R  |

## Example 1) MATLAB - Load .mat file exported from a dataset created.

```
test_ak_simple_data_load.m
```

This example shows how to load infrared and depth data extracted from videos in .mkv format using KA_FRAME_EXTRACTOR and
its subsequent use in MATLABs scripts as .mat files.

DEPTH
data ![alt text](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/tools/img/DEPTH_data_exported.png?raw=true)

IR data ![alt text](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/tools/img/IR_data_exported.png?raw=true)

## Example 2) MATLAB - Load .mat file exported from a dataset created.

```
test_ak_data_extracted.m
```

This example shows how to load data extracted from videos in .mkv format using KA_FRAME_EXTRACTOR and its subsequent use
in MATLABs scripts as .mat files. Having given frames (RGB and depth data) extracted from video files, it is filtered by
depth threshold value to obtain a segmented RGB fruit image.

Original
Image ![alt text](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/tools/img/20210927_114012_k_r2_e_000_150_138_2_0_C.png?raw=true)

Segmented
image ![alt text](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/tools/img/20210927_114012_k_r2_e_000_150_138_2_0_C.png_mask1.jpg?raw=true)

## Example 3) Python - Load .mat file exported from a dataset created.

This example shows how to load data extracted from videos in .mkv format using KA_FRAME_EXTRACTOR and its subsequent use
in Python scripts as .mat files. Having given frames (RGB and depth data) extracted from video files, it is filtered by
depth threshold value to obtain a segmented RGB fruit image.

```
test_ak_data_extracted.py
```

Original
Image ![alt text](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/tools/img/20210927_114012_k_r2_e_000_150_138_2_0_C.png?raw=true)

Segmented
image ![alt text](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/tools/img/20210927_114012_k_r2_e_000_150_138_2_0_C.png_mask1_p.jpg?raw=true)

## Example 4) R - Load .mat file exported from a dataset created.

This example shows how to load infrarred and depth data extracted from videos in .mkv format using AK_FRAME_EXTRACTOR
and its subsequent use in R scripts as .mat files.

```
test_ak_simple_data_load.R
```