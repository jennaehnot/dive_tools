# dive-tools
This repository is for converting object annotation files generated by the softwave [DIVE/VIAME toolkit](https://kitware.github.io/dive/) into YOLOv5 annotation files.


After annotating, their platform offers two methods for downloading:
1. annotations.dive.json
2. annotations.viame.csv
   
The annotation format for boundary boxes in VIAME/DIVE is x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, <sub>2</sub>, describing the upper left and bottom right corners.
YOLOv5 boundary box format follows center<sub>x</sub>, center<sub>y</sub>, width<sub>bb_box</sub>, height<sub>bb_box</sub>, all normalized by the width and height of the photo. 

Before using these scripts:
YOLO expects that images and their corresponding labels have the same name. So before creating my label files from the DIVE/VIAME file, I converted the video file into numbered frames using ffmpeg: 
```
{
ffmpeg -i video.mp4 -vf fps=10 images/frame_%d.png
}
```
In the code, the variable **name_conv** is whatever you put in front of the frame number when running ffmpeg. For example, after running the code above, I would use **name_conv = 'frame_'**. This ensures we can match the label file name and image file name to the correct frame. 
