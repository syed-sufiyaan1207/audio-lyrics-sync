# Audio Lyrics Sync 🎵

A Python-based terminal application that synchronizes lyrics with an MP3 audio file and displays the lyrics character-by-character in real time.

## Features

- 🎵 Plays an MP3 audio file in the background
- ✨ Displays lyrics character-by-character
- ⏱️ Uses precise timestamps for lyric synchronization
- 🎨 Randomized terminal colors for lyric lines
- ✅ Checks for mismatches between lyrics and timestamps
- 📂 Allows the user to provide their own MP3 file

## Technologies Used

- Python
- playsound3
- time
- random
- os
- ANSI terminal formatting

## How It Works

The program takes an MP3 file path from the user and plays the audio in the background.

Each lyric line has an associated timestamp. The program waits until the appropriate timestamp and then displays the lyric character-by-character. The character delay is calculated based on the available time before the next lyric begins.

## Installation

Clone the repository:

```bash
git clone https://github.com/syed-sufiyaan1207/audio-lyrics-sync.git
