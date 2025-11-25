# Math Game v2 🎮

A fun and educational math game built with Pygame that helps players practice basic arithmetic operations: addition, subtraction, multiplication, and division.

## 📋 Table of Contents
- [About the Game](#about-the-game)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Windows Installation](#windows-installation)
  - [macOS/Linux Installation](#macoslinux-installation)
- [How to Run the Game](#how-to-run-the-game)
- [Game Resources](#game-resources)
- [Project Structure](#project-structure)
- [How the Code Works](#how-the-code-works)
- [Troubleshooting](#troubleshooting)

## 🎯 About the Game

Math Game v2 is an interactive educational game designed to help players improve their mental math skills. Players select an operation type from a menu and solve 20 problems, earning points for correct answers. The game features visual feedback, sound effects, and a scoring system to make learning math fun and engaging.

**Video Demo**: https://youtu.be/R8UUBWTG0OQ

## ✨ Features

- **Four Operation Modes**: Addition, Subtraction, Multiplication, and Division
- **Multiple Choice Format**: Four answer buttons per question
- **Scoring System**: Earn 5 points for each correct answer
- **Visual Feedback**: Buttons turn green for correct answers, red for incorrect
- **Sound Effects**: Audio feedback for correct and incorrect answers
- **Beautiful UI**: Custom fonts and background image
- **Progress Tracking**: Shows current score and tracks 20 problems per session
- **Menu System**: Easy navigation with mouse hover effects

## 🔧 Prerequisites

Before running the game, you need to have Python installed on your system:

- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** (Python package installer - comes with Python)

## 💾 Installation

### Windows Installation

1. **Install Python**
   - Download Python from [python.org](https://www.python.org/downloads/)
   - During installation, **check the box** that says "Add Python to PATH"
   - Verify installation by opening Command Prompt and typing:
     ```cmd
     python --version
     ```

2. **Download the Game**
   - Download or clone this repository to your computer
   - Extract the files to a folder (e.g., `C:\Math-games-v2`)

3. **Open Command Prompt in the Game Folder**
   - Navigate to the game folder:
     ```cmd
     cd C:\Math-games-v2
     ```
   - Or right-click in the folder while holding Shift and select "Open PowerShell window here" or "Open command window here"

4. **Create a Virtual Environment (Optional but Recommended)**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

5. **Install Pygame**
   ```cmd
   pip install -r requirements.txt
   ```
   Or install Pygame directly:
   ```cmd
   pip install pygame
   ```

### macOS/Linux Installation

1. **Install Python**
   - macOS: Python 3 is often pre-installed. Check with `python3 --version`
   - Linux: Use your package manager (e.g., `sudo apt install python3 python3-pip`)

2. **Navigate to the Game Folder**
   ```bash
   cd /path/to/Math-games-v2
   ```

3. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Pygame**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 How to Run the Game

### On Windows:
```cmd
python main.py
```

### On macOS/Linux:
```bash
python3 main.py
```

### Game Controls:
- **Mouse**: Click to select menu options and answer buttons
- **ESC Key**: Return to the main menu at any time

## 📁 Game Resources

The game uses several external resources located in the project folder:

### Fonts
- **`kenvector_future.ttf`**: Used for the score display (20px)
- **`XpressiveBlack Regular.ttf`**: Used for menu items (50px)

### Images
- **`background.jpg`**: The background image displayed during gameplay
- **`symbols.png`**: A sprite sheet containing the four operation symbols (+, -, ×, ÷)
  - Each symbol is 64x64 pixels arranged horizontally

### Sound Effects
- **`background-music.ogg`**: Background music that loops continuously during gameplay
- **`item1.ogg`**: Plays when the player selects the correct answer
- **`item2.ogg`**: Plays when the player selects an incorrect answer

## 📂 Project Structure

```
Math-games-v2/
│
├── main.py                       # Entry point - initializes Pygame and game loop
├── game.py                       # Core game logic and Button class
├── menu.py                       # Menu system for operation selection
├── requirements.txt              # Python dependencies
│
├── kenvector_future.ttf          # Font for score display
├── XpressiveBlack Regular.ttf    # Font for menu items
├── background.jpg                # Game background image
├── symbols.png                   # Operation symbols sprite sheet
├── background-music.ogg          # Background music (looping)
├── item1.ogg                     # Correct answer sound
├── item2.ogg                     # Incorrect answer sound
│
└── README.md                     # This file
```

## 🔍 How the Code Works

### main.py - The Entry Point
- Initializes Pygame
- Creates the game window (640x480 pixels)
- Sets up the game loop running at 30 FPS
- Handles the main game cycle: process events → run logic → display frame

### game.py - Game Logic
**Game Class**:
- Manages game state and problem generation
- Handles four operations: addition, subtraction, multiplication, division
- Creates and manages four answer buttons (one correct, three random)
- Tracks score and problem count (20 problems per session)
- Loads and displays resources (fonts, images, sounds)
- Provides visual feedback (green for correct, red for incorrect)

**Button Class**:
- Represents clickable answer buttons
- Handles drawing buttons with text
- Detects mouse clicks
- Changes color based on answer correctness

### menu.py - Menu System
**Menu Class**:
- Creates interactive menu with operation choices
- Highlights menu items on mouse hover (red text)
- Uses custom font for styling
- Handles menu item selection

## 🛠 Troubleshooting

### "Python is not recognized" (Windows)
- Python is not in your PATH. Reinstall Python and check "Add Python to PATH"

### "pygame module not found"
- Run: `pip install pygame` or `pip install -r requirements.txt`

### "No module named tkinter" (Linux)
- Install tkinter: `sudo apt-get install python3-tk`

### Sound not playing
- Ensure your system audio is not muted
- Verify that `.ogg` files are in the game folder

### Missing font or image files
- Ensure all resource files are in the same folder as the `.py` files
- Check that file names match exactly (case-sensitive on macOS/Linux)

### Game runs too fast or slow
- The game is locked to 30 FPS. Check if your system meets minimum requirements

## 🙏 Credits

This project is a fork of the original [Math-games](https://github.com/edward344/Math-games) by [edward344](https://github.com/edward344). Thank you for the great work and foundation!

### Sound Resources

- **Background Music**: [Kids Game Gaming Background Music](https://pixabay.com/music/happy-childrens-tunes-kids-game-gaming-background-music-295075/) from Pixabay
- **Sound Effects**: [Game Sound Effects](https://mixkit.co/free-sound-effects/game/) from Mixkit

## 📝 License

This project is open source and available for educational purposes.

## 🎓 Learning Resources

For more information about Pygame and game development, check out the [Game Instructions](game-instructions.md) file.

---

**Enjoy playing and improving your math skills! 🧮✨**
