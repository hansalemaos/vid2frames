<h2>Converts a video to frames </h2>


```python
# ffmpeg needs to be installed! 
pip install vid2frames
from vid2frames import convert_video_to_frames
allfiles = convert_video_to_frames(
    video=r"F:\newvidxx2.mp4",
    output_folder="f:\\outputvi",  # folder will be created if it doesn't exists
    fps=24,
    fileprefix="videoframe",
    zfill=8,  # videoframe_1.png -> videoframe_0000001.png
)



```



