import os
from moviepy.editor import *
import tkinter as tk
from tkinter import filedialog, simpledialog

def create_video(input_folder, duration, audio_file, output_file):
    # Lists all image files in the specified directory.
    images = [os.path.join(input_folder, img) for img in os.listdir(input_folder) if img.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff'))]
    
    # Sort the images by name
    images.sort()

    # Create video clip for each image
    clips = [ImageClip(m).set_duration(duration).set_fps(24) for m in images]

    # Concatenate all video clips into one video
    concat_clip = concatenate_videoclips(clips, method="compose")

    # Add audio to the video
    audio_background = AudioFileClip(audio_file)
    final_clip = concat_clip.set_audio(audio_background)

    # Write the result to a file
    final_clip.write_videofile(output_file, codec='libx264')

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        duration = simpledialog.askinteger("Input", "How long should each image be displayed (in seconds)?", parent=root)
        audio_file = filedialog.askopenfilename(title="Select audio file", filetypes=(("Audio files", "*.wav *.flac *.mp3 *.aac"), ("All files", "*.*")))
        output_file = filedialog.asksaveasfilename(defaultextension=".mp4", initialdir=folder, title="Select output file", filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")))
        if output_file:
            create_video(folder, duration, audio_file, output_file)

root = tk.Tk()
button = tk.Button(root, text="Browse", command=browse_folder)
button.pack()
root.mainloop()