import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pygame
import os

pygame.mixer.init()

def load_music():
    global music_file
    music_file = filedialog.askopenfilename(title="Select a Music File", filetypes=[("Audio Files", "*.mp4 *.mp3 *.wav")])
    if music_file:
        song_label.config(text=f"Loaded: {os.path.basename(music_file)}")
        play_button.config(state=tk.NORMAL)
    else:
        messagebox.showwarning("Warning", "No file selected!")

def play_music():
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    status_label.config(text="Playing...")

def pause_music():
    pygame.mixer.music.pause()
    status_label.config(text="Paused")

def resume_music():
    pygame.mixer.music.unpause()
    status_label.config(text="Playing...")

def stop_music():
    pygame.mixer.music.stop()
    status_label.config(text="Stopped")

# Function to adjust volume
def set_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

app = tk.Tk()
app.title("Music Player")
app.geometry("500x400")
app.config(bg="#282828")

title_label = tk.Label(app, text="Music Player", font=("Arial", 24, "bold"), bg="#282828", fg="#ffffff")
title_label.pack(pady=10)

# Load button to select music file
load_button = tk.Button(app, text="Load Music", font=("Arial", 14), bg="#444444", fg="#ffffff", command=load_music)
load_button.pack(pady=20)


song_label = tk.Label(app, text="No music loaded", font=("Arial", 12), bg="#282828", fg="#ffffff")
song_label.pack(pady=10)

# Control buttons (Play, Pause, Resume, Stop)
control_frame = tk.Frame(app, bg="#282828")
control_frame.pack(pady=10)

play_button = tk.Button(control_frame, text="Play", font=("Arial", 14), bg="#4CAF50", fg="#ffffff", state=tk.DISABLED, command=play_music)
play_button.grid(row=0, column=0, padx=10)

pause_button = tk.Button(control_frame, text="Pause", font=("Arial", 14), bg="#FF9800", fg="#ffffff", command=pause_music)
pause_button.grid(row=0, column=1, padx=10)

resume_button = tk.Button(control_frame, text="Resume", font=("Arial", 14), bg="#FFC107", fg="#ffffff", command=resume_music)
resume_button.grid(row=0, column=2, padx=10)

stop_button = tk.Button(control_frame, text="Stop", font=("Arial", 14), bg="#F44336", fg="#ffffff", command=stop_music)
stop_button.grid(row=0, column=3, padx=10)

# Volume control
volume_label = tk.Label(app, text="Volume", font=("Arial", 12), bg="#282828", fg="#ffffff")
volume_label.pack(pady=10)

volume_slider = tk.Scale(app, from_=0, to=100, orient=tk.HORIZONTAL, bg="#282828", fg="#ffffff", command=set_volume)
volume_slider.set(70)  # Set initial volume
volume_slider.pack()

# Label to show the current status (Playing, Paused, Stopped)
status_label = tk.Label(app, text="No music playing", font=("Arial", 12), bg="#282828", fg="#ffffff")
status_label.pack(pady=20)

# Run the application
app.mainloop()
