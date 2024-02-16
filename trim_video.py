import datetime
from moviepy.editor import VideoFileClip

def trim_video(video_path, start_time, end_time):
  # Ensure start time is less than end time
  if start_time >= end_time:
    raise ValueError("Start time must be less than end time.")

  # Get unique file name with timestamp
  timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
  output_path = f"trimmed_{timestamp}.mp4"

  # Parse start and end times from strings (assuming HH:MM:SS format)
  try:
    start_time_obj = datetime.datetime.strptime(start_time, "%H:%M:%S")
    start_seconds = start_time_obj.hour * 3600 + start_time_obj.minute * 60 + start_time_obj.second

    end_time_obj = datetime.datetime.strptime(end_time, "%H:%M:%S")
    end_seconds = end_time_obj.hour * 3600 + end_time_obj.minute * 60 + end_time_obj.second

  except ValueError:
    raise ValueError("Invalid start or end time format. Please use HH:MM:SS.")

  # Load the video clip
  clip = VideoFileClip(video_path)

  # Trim the clip
  trimmed_clip = clip.subclip(start_seconds, end_seconds)

  # Write the trimmed clip to a new file
  trimmed_clip.write_videofile(output_path)

  return output_path

# Example usage
video_path = "/home/horixons/Videos/shorts/I_do_code.mp4"
start_time = "00:00:12"  # Start at 10 minutes
end_time = "00:00:20"  # End at 20 minutes 30 seconds

try:
  output_path = trim_video(video_path, start_time, end_time)
  print(f"Trimmed video saved to: {output_path}")
except ValueError as e:
  print(e)
