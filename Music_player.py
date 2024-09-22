import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Desktop Music Player")
        master.geometry("500x300")
        master.config(bg="#282c34")

        pygame.mixer.init()

        self.songs = []
        self.current_song_index = 0

        # Title label
        self.title_label = tk.Label(master, text="Desktop Music Player", bg="#282c34", fg="white", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Song display area
        self.song_display = tk.Label(master, text="No song loaded", bg="#282c34", fg="white", font=("Helvetica", 12))
        self.song_display.pack(pady=10)

        # Load button
        self.load_button = tk.Button(master, text="Load Folder", command=self.load_songs, bg="#61afef", fg="white", font=("Helvetica", 12))
        self.load_button.pack(pady=5)

        # Control buttons
        button_frame = tk.Frame(master, bg="#282c34")
        button_frame.pack(pady=10)

        self.play_button = tk.Button(button_frame, text="Play", command=self.play_song, bg="#61afef", fg="white", font=("Helvetica", 12), width=8)
        self.play_button.grid(row=0, column=0, padx=5)

        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause_song, bg="#61afef", fg="white", font=("Helvetica", 12), width=8)
        self.pause_button.grid(row=0, column=1, padx=5)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_song, bg="#61afef", fg="white", font=("Helvetica", 12), width=8)
        self.stop_button.grid(row=0, column=2, padx=5)

        self.next_button = tk.Button(button_frame, text="Next", command=self.next_song, bg="#61afef", fg="white", font=("Helvetica", 12), width=8)
        self.next_button.grid(row=0, column=3, padx=5)

        self.prev_button = tk.Button(button_frame, text="Previous", command=self.previous_song, bg="#61afef", fg="white", font=("Helvetica", 12), width=8)
        self.prev_button.grid(row=0, column=4, padx=5)

        # Set up a volume slider
        self.volume_label = tk.Label(master, text="Volume", bg="#282c34", fg="white", font=("Helvetica", 12))
        self.volume_label.pack(pady=10)

        self.volume_scale = tk.Scale(master, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=self.set_volume, bg="#61afef")
        self.volume_scale.set(0.5)
        self.volume_scale.pack(pady=10)

    def load_songs(self):
        folder = filedialog.askdirectory()
        if folder:
            self.songs = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith(('.mp3', '.wav'))]
            if self.songs:
                self.song_display.config(text=f"Loaded: {os.path.basename(self.songs[0])}")
            else:
                messagebox.showwarning("Warning", "No audio files found in the selected folder.")

    def play_song(self):
        if self.songs:
            pygame.mixer.music.load(self.songs[self.current_song_index])
            pygame.mixer.music.play()
            self.song_display.config(text=f"Playing: {os.path.basename(self.songs[self.current_song_index])}")

    def pause_song(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def stop_song(self):
        pygame.mixer.music.stop()
        self.song_display.config(text="No song loaded")

    def next_song(self):
        if self.songs:
            self.current_song_index = (self.current_song_index + 1) % len(self.songs)
            self.play_song()

    def previous_song(self):
        if self.songs:
            self.current_song_index = (self.current_song_index - 1) % len(self.songs)
            self.play_song()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
