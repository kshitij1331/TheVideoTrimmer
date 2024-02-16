## Python Video Trimmer with MoviePy

This script provides a simple tool to trim video clips using the `MoviePy` library.

### Features:

- Trim videos based on specified start and end times 
- Generates unique output filenames for trimmed videos.
- Preserves original video quality (no re-encoding).

### How to use:

- Install the `MoviePy` library: `pip install moviepy`
- Save the script as trim_video.py.
- Update the video path (video_path), start time (start_time), and end time (end_time) variables in the script with your desired values.
- Run the script: `python trim_video.py`

### Example usage:
```bash
video_path = "path/to/your/video.mp4"
start_time = "00:10:00"  # Start at 10 minutes
end_time = "00:20:30"  # End at 20 minutes 30 seconds

trim_video(video_path, start_time, end_time)
```

### Notes:

- This script assumes basic familiarity with Python scripting.
- You can modify the script to add more features like output format selection or progress bars.
- Re-encoding might be necessary depending on the video format and desired output.

### Further information:

- MoviePy documentation: https://zulko.github.io/moviepy/
- Python datetime module: https://docs.python.org/3/library/datetime.html

