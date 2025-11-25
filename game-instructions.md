# Game Instructions & Pygame Tutorial 🎮

## Table of Contents
1. [Introduction to Pygame](#introduction-to-pygame)
2. [Understanding the Game Architecture](#understanding-the-game-architecture)
3. [Detailed Code Explanation](#detailed-code-explanation)
4. [How Game Resources Work](#how-game-resources-work)
5. [Game Flow & Logic](#game-flow--logic)
6. [Playing the Game](#playing-the-game)
7. [Learning from This Project](#learning-from-this-project)

---

## Introduction to Pygame

### What is Pygame?

**Pygame** is a popular Python library used for creating 2D games and multimedia applications. It provides modules for handling graphics, sounds, keyboard input, mouse input, and game timing.

### Key Pygame Concepts

1. **Display Surface**: The game window where everything is drawn
2. **Game Loop**: A continuous loop that runs the game
3. **Events**: User inputs (keyboard, mouse clicks, window close)
4. **Sprites**: Game objects (images, characters, buttons)
5. **Clock**: Controls the frame rate (FPS)
6. **Blitting**: Drawing images onto the screen

### Pygame Modules Used in This Game

```python
import pygame              # Main pygame module
pygame.init()             # Initialize all pygame modules
pygame.display            # Window/screen management
pygame.font               # Text rendering
pygame.image              # Image loading
pygame.mixer              # Sound and music
pygame.time               # Time and FPS control
pygame.mouse              # Mouse input
pygame.event              # Event handling
```

---

## Understanding the Game Architecture

This game follows a **Model-View-Controller (MVC)** pattern:

### File Organization

```
main.py  ──────► Entry point & game loop
    │
    └──► game.py ────► Game logic & rendering
            │
            └──► menu.py ────► Menu system
```

### The Three-File Structure

1. **`main.py`**: Initializes Pygame and runs the main game loop
2. **`game.py`**: Contains the `Game` class (logic) and `Button` class (UI element)
3. **`menu.py`**: Contains the `Menu` class for the operation selection screen

---

## Detailed Code Explanation

### 1. main.py - The Game Loop

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from game import Game

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
```

**Explanation**:
- The shebang (`#!/usr/bin/env python`) allows the script to run directly on Unix systems
- `utf-8` encoding ensures proper character handling
- Constants define the window dimensions

#### The main() Function

```python
def main():
    pygame.init()
```
- **`pygame.init()`**: Initializes all Pygame modules (display, sound, font, etc.)

```python
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Math Games")
```
- **`set_mode()`**: Creates the game window with specified dimensions
- **`set_caption()`**: Sets the window title

```python
    done = False
    clock = pygame.time.Clock()
    game = Game()
```
- **`done`**: Boolean flag to control the main loop
- **`clock`**: Object to control frame rate
- **`game`**: Instance of the Game class

#### The Game Loop

```python
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(30)
```

This is the **heart of any game**:

1. **Process Events**: Handle user input (mouse clicks, key presses)
2. **Run Logic**: Update game state (calculations, score tracking)
3. **Display Frame**: Draw everything to the screen
4. **Tick**: Limit to 30 frames per second (FPS)

```python
    pygame.quit()
```
- **`pygame.quit()`**: Properly closes Pygame and cleans up resources

---

### 2. game.py - The Core Game Logic

This file contains two classes: `Game` and `Button`.

#### Constants

```python
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Colors (RGB format)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
```

**RGB Color System**: Each color is a tuple of (Red, Green, Blue) values from 0-255.

#### Game Class - Initialization

```python
class Game(object):
    def __init__(self):
        self.font = pygame.font.Font(None, 65)
        self.score_font = pygame.font.Font("kenvector_future.ttf", 20)
```

**Fonts**:
- `Font(None, 65)`: Uses default font, size 65 for problems
- `Font("kenvector_future.ttf", 20)`: Custom font for score display

```python
        self.problem = {"num1": 0, "num2": 0, "result": 0}
        self.operation = ""
```

**Problem Dictionary**: Stores the current math problem's numbers and answer.

```python
        self.symbols = self.get_symbols()
        self.button_list = self.get_button_list()
```

**Initialization Methods**:
- Loads operation symbols from sprite sheet
- Creates four answer buttons

```python
        self.menu = Menu(items, ttf_font="XpressiveBlack Regular.ttf", font_size=50)
        self.show_menu = True
```

**Menu System**:
- Creates a menu with four operation choices
- Starts with menu visible

```python
        self.score = 0
        self.count = 0
```

**Tracking Variables**:
- `score`: Player's points (5 per correct answer)
- `count`: Number of problems solved (max 20)

```python
        self.background_image = pygame.image.load("background.jpg").convert()
        self.sound_1 = pygame.mixer.Sound("item1.ogg")
        self.sound_2 = pygame.mixer.Sound("item2.ogg")
```

**Resource Loading**:
- **`convert()`**: Optimizes images for faster blitting
- **`Sound()`**: Loads audio files for playback

#### Loading Symbols from Sprite Sheet

```python
def get_symbols(self):
    symbols = {}
    sprite_sheet = pygame.image.load("symbols.png").convert()
    image = self.get_image(sprite_sheet, 0, 0, 64, 64)
    symbols["addition"] = image
    # ... (similar for other operations)
    return symbols
```

**Sprite Sheet Technique**:
- One image file contains multiple sprites
- `get_image()` extracts individual 64x64 pixel images
- More efficient than loading separate files

```python
def get_image(self, sprite_sheet, x, y, width, height):
    image = pygame.Surface([width, height]).convert()
    image.blit(sprite_sheet, (0, 0), (x, y, width, height))
    return image
```

**Image Extraction**:
1. Creates a blank surface
2. Blits (copies) a portion from the sprite sheet
3. Parameters: source position (x, y) and size (width, height)

#### Math Operations

```python
def addition(self):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    self.problem["num1"] = a
    self.problem["num2"] = b
    self.problem["result"] = a + b
    self.operation = "addition"
```

**Addition Logic**:
- Generates two random numbers (0-100)
- Calculates the sum
- Stores in the problem dictionary

```python
def subtraction(self):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    if a > b:
        self.problem["num1"] = a
        self.problem["num2"] = b
        self.problem["result"] = a - b
    else:
        self.problem["num1"] = b
        self.problem["num2"] = a
        self.problem["result"] = b - a
    self.operation = "subtraction"
```

**Subtraction Logic**:
- Ensures no negative results
- Larger number is always first

```python
def multiplication(self):
    a = random.randint(0, 12)
    b = random.randint(0, 12)
    # ... (simpler, uses 0-12 for easier problems)
```

**Multiplication Logic**:
- Uses smaller range (0-12) for times tables practice

```python
def division(self):
    divisor = random.randint(1, 12)
    dividend = divisor * random.randint(1, 12)
    quotient = dividend / divisor
    # ...
```

**Division Logic**:
- Ensures whole number answers
- Creates dividend from divisor to avoid remainders

#### Creating Answer Buttons

```python
def get_button_list(self):
    button_list = []
    choice = random.randint(1, 4)  # Which button has correct answer
    
    width = 100
    height = 100
    t_w = width * 2 + 50  # Total width (2 buttons + gap)
    posX = (SCREEN_WIDTH / 2) - (t_w / 2)  # Center horizontally
    posY = 150
```

**Button Layout**:
- Creates a 2x2 grid of buttons
- Centers them on screen
- One button has the correct answer, three have random numbers

#### Event Processing

```python
def process_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
```

**Event Loop**:
- Checks all events in the queue
- Returns `True` to quit if window is closed

```python
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.show_menu:
                if self.menu.state == 0:
                    self.operation = "addition"
                    self.set_problem()
                    self.show_menu = False
                # ... (similar for other operations)
```

**Menu Selection**:
- Detects which menu item was clicked
- Starts the corresponding operation
- Hides menu and shows game

```python
            else:
                self.check_result()
```

**Answer Selection**:
- If not in menu, checks if answer is correct

```python
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.show_menu = True
                self.score = 0
                self.count = 0
```

**ESC Key**:
- Returns to menu
- Resets score and count

#### Checking Answers

```python
def check_result(self):
    for button in self.button_list:
        if button.isPressed():
            if button.get_number() == self.problem["result"]:
                button.set_color(GREEN)
                self.score += 5
                self.sound_1.play()
            else:
                button.set_color(RED)
                self.sound_2.play()
            self.reset_problem = True
```

**Answer Validation**:
1. Finds which button was clicked
2. Compares button's number to correct answer
3. Changes button color (green/red)
4. Updates score if correct
5. Plays appropriate sound
6. Flags to create new problem

#### Display Frame

```python
def display_frame(self, screen):
    screen.blit(self.background_image, (0, 0))
```

**Background**:
- Draws background image first (covers previous frame)

```python
    if self.show_menu:
        self.menu.display_frame(screen)
```

**Menu Display**:
- Shows menu if `show_menu` is True

```python
    elif self.count == 20:
        msg_1 = "You answered " + str(self.score / 5) + " correctly"
        msg_2 = "Your score was " + str(self.score)
        self.display_message(screen, (msg_1, msg_2))
        # Reset and wait
        time_wait = True
```

**Game Over**:
- After 20 problems, shows results
- Waits 3 seconds before returning to menu

```python
    else:
        # Display current problem and buttons
        label_1 = self.font.render(str(self.problem["num1"]), True, BLACK)
        screen.blit(label_1, (posX, 50))
        screen.blit(self.symbols[self.operation], (...))
        # ... draw buttons and score
```

**Game Display**:
- Renders the math problem
- Displays operation symbol
- Draws all four answer buttons
- Shows current score

```python
    pygame.display.flip()
```

**Screen Update**:
- `flip()` updates the entire screen
- Makes all drawn elements visible

```python
    if self.reset_problem:
        pygame.time.wait(1000)  # Wait 1 second
        self.set_problem()
        self.count += 1
        self.reset_problem = False
```

**Problem Transition**:
- Waits 1 second to show feedback color
- Creates new problem
- Increments problem counter

---

### 3. Button Class

```python
class Button(object):
    def __init__(self, x, y, width, height, number):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render(str(number), True, BLACK)
        self.number = number
        self.background_color = WHITE
```

**Button Structure**:
- **Rect**: Defines button position and size
- **Font**: For rendering the number
- **Text**: Pre-rendered number surface
- **Color**: Changes based on correctness

```python
def draw(self, screen):
    pygame.draw.rect(screen, self.background_color, self.rect)
    pygame.draw.rect(screen, BLACK, self.rect, 3)  # Border
    # Center text in button
    width = self.text.get_width()
    height = self.text.get_height()
    posX = self.rect.centerx - (width / 2)
    posY = self.rect.centery - (height / 2)
    screen.blit(self.text, (posX, posY))
```

**Drawing**:
1. Fill button with background color
2. Draw black border (3 pixels thick)
3. Calculate centered position for text
4. Blit text onto button

```python
def isPressed(self):
    pos = pygame.mouse.get_pos()
    if self.rect.collidepoint(pos):
        return True
    else:
        return False
```

**Collision Detection**:
- Gets current mouse position
- Checks if mouse is inside button's rectangle
- Used to detect button clicks

---

### 4. menu.py - The Menu System

```python
class Menu(object):
    state = -1  # Class variable
```

**State Variable**:
- `-1`: No item hovered
- `0-3`: Index of hovered menu item

```python
def __init__(self, items, font_color=(0,0,0), select_color=(255,0,0), 
             ttf_font=None, font_size=25):
    self.font_color = font_color
    self.select_color = select_color
    self.items = items
    self.font = pygame.font.Font(ttf_font, font_size)
    self.rect_list = self.get_rect_list(items)
```

**Menu Properties**:
- **items**: Tuple of menu options
- **font_color**: Normal text color (black)
- **select_color**: Hover color (red)
- **rect_list**: Collision rectangles for each item

```python
def get_rect_list(self, items):
    rect_list = []
    for index, item in enumerate(items):
        size = self.font.size(item)
        width = size[0]
        height = size[1]
        
        posX = (SCREEN_WIDTH / 2) - (width / 2)
        t_h = len(items) * height
        posY = (SCREEN_HEIGHT / 2) - (t_h / 2) + (index * height)
        
        rect = pygame.Rect(posX, posY, width, height)
        rect_list.append(rect)
    
    return rect_list
```

**Rectangle Generation**:
1. Calculate text dimensions
2. Center horizontally
3. Stack vertically (centered as a group)
4. Create invisible rectangles for collision detection

```python
def collide_points(self):
    index = -1
    mouse_pos = pygame.mouse.get_pos()
    for i, rect in enumerate(self.rect_list):
        if rect.collidepoint(mouse_pos):
            index = i
    return index
```

**Hover Detection**:
- Returns index of hovered item
- Returns -1 if no hover

```python
def update(self):
    self.state = self.collide_points()
```

**Update Loop**:
- Called every frame
- Updates which item is hovered

```python
def display_frame(self, screen):
    for index, item in enumerate(self.items):
        if self.state == index:
            label = self.font.render(item, True, self.select_color)
        else:
            label = self.font.render(item, True, self.font_color)
        
        # Calculate position and blit
        screen.blit(label, (posX, posY))
```

**Rendering**:
- Renders each menu item
- Uses red color if hovered, black otherwise
- Centers each item on screen

---

## How Game Resources Work

### 1. Font Files (.ttf)

**TrueType Fonts** allow custom typography:

```python
font = pygame.font.Font("kenvector_future.ttf", 20)
```

- Loaded once during initialization
- Rendered to create text surfaces
- Can be any size without quality loss

**Usage in Game**:
- `kenvector_future.ttf`: Score display
- `XpressiveBlack Regular.ttf`: Menu items

### 2. Image Files

#### Background Image (background.jpg)

```python
self.background_image = pygame.image.load("background.jpg").convert()
```

- **`load()`**: Loads image from disk
- **`convert()`**: Converts to screen's pixel format (faster blitting)
- Drawn first each frame (background layer)

#### Sprite Sheet (symbols.png)

A **sprite sheet** is one image containing multiple sprites:

```
[+][−][×][÷]
```

**Advantages**:
- Fewer file loads (better performance)
- Organized asset management
- Smaller total file size

**Extraction Process**:
```python
# Load sheet
sprite_sheet = pygame.image.load("symbols.png").convert()

# Extract addition symbol (0, 0, 64, 64)
image = get_image(sprite_sheet, 0, 0, 64, 64)

# Extract subtraction symbol (64, 0, 64, 64)
image = get_image(sprite_sheet, 64, 0, 64, 64)

# And so on...
```

### 3. Sound Files (.ogg)

**OGG** is an open-source audio format:

```python
self.sound_1 = pygame.mixer.Sound("item1.ogg")
self.sound_2 = pygame.mixer.Sound("item2.ogg")
```

- **`Sound()`**: Loads audio into memory
- **`play()`**: Plays the sound

**Sound Usage**:
- `item1.ogg`: Correct answer (positive feedback)
- `item2.ogg`: Incorrect answer (negative feedback)

**Audio in Pygame**:
- `pygame.mixer.Sound`: For short sound effects
- `pygame.mixer.music`: For background music (not used here)

---

## Game Flow & Logic

### Startup Sequence

```
1. Run main.py
2. Initialize Pygame
3. Create game window (640x480)
4. Create Game object
   ├─ Load fonts
   ├─ Load images
   ├─ Load sounds
   ├─ Create menu
   └─ Initialize variables
5. Enter main game loop
```

### Menu Phase

```
Loop:
  1. Process events
     └─ Mouse click? → Select operation
  2. Update menu (detect hover)
  3. Display menu
  4. Tick clock (30 FPS)
```

### Gameplay Phase

```
For each problem (20 total):
  1. Generate random math problem
  2. Create 4 buttons (1 correct, 3 random)
  3. Loop:
     ├─ Process events
     │  ├─ Mouse click? → Check answer
     │  └─ ESC key? → Return to menu
     ├─ Display problem
     ├─ Display buttons
     ├─ Display score
     └─ Tick clock
  4. Show feedback (green/red, sound)
  5. Wait 1 second
  6. Next problem
```

### Game Over Phase

```
1. Display results
   ├─ "You answered X correctly"
   └─ "Your score was Y"
2. Wait 3 seconds
3. Return to menu
4. Reset score and count
```

### Visual Feedback System

```
Answer clicked
    ├─ Correct?
    │  ├─ YES
    │  │  ├─ Turn button GREEN
    │  │  ├─ Play item1.ogg (success sound)
    │  │  └─ Add 5 points
    │  └─ NO
    │     ├─ Turn button RED
    │     └─ Play item2.ogg (failure sound)
    ├─ Wait 1 second (show color)
    └─ Next problem
```

---

## Playing the Game

### Step-by-Step Guide

1. **Launch the Game**
   ```bash
   python main.py
   ```

2. **Main Menu**
   - You'll see four options:
     - Addition
     - Subtraction
     - Multiplication
     - Division
   - Hover over options (they turn red)
   - Click to select an operation

3. **Gameplay**
   - A math problem appears at the top
   - Four answer buttons appear below
   - Your score is shown in the top-left corner
   - Click the button with the correct answer

4. **Feedback**
   - **Correct**: Button turns green, positive sound plays, +5 points
   - **Incorrect**: Button turns red, negative sound plays, no points

5. **Game Progress**
   - After 1 second, a new problem appears
   - Complete 20 problems per session

6. **Results Screen**
   - Shows how many you answered correctly
   - Shows your total score
   - Automatically returns to menu after 3 seconds

7. **Return to Menu**
   - Press **ESC** at any time to return to the main menu
   - Your score resets when returning to menu

### Scoring System

- **5 points** per correct answer
- **0 points** for incorrect answers
- **Maximum score**: 100 points (20 correct answers)

### Difficulty Levels

**Addition & Subtraction**:
- Numbers range from 0 to 100
- Moderate difficulty

**Multiplication**:
- Numbers range from 0 to 12
- Times tables practice
- Easier than addition/subtraction

**Division**:
- Divisors from 1 to 12
- Always whole number answers
- Similar difficulty to multiplication

---

## Learning from This Project

### Python Concepts Demonstrated

1. **Object-Oriented Programming (OOP)**
   - Classes and objects
   - Encapsulation (methods and attributes)
   - Class initialization (`__init__`)

2. **Dictionaries**
   ```python
   self.problem = {"num1": 0, "num2": 0, "result": 0}
   ```

3. **Lists and Loops**
   ```python
   for button in self.button_list:
       button.draw(screen)
   ```

4. **Conditional Statements**
   ```python
   if a > b:
       # ...
   else:
       # ...
   ```

5. **Random Number Generation**
   ```python
   import random
   a = random.randint(0, 100)
   ```

6. **String Formatting**
   ```python
   "Score: " + str(self.score)
   ```

### Pygame Concepts

1. **Game Loop Pattern**
   ```python
   while not done:
       process_input()
       update_game_state()
       render_graphics()
       control_fps()
   ```

2. **Event-Driven Programming**
   - Responding to user input
   - Mouse clicks, key presses

3. **Sprite Management**
   - Loading and displaying images
   - Sprite sheets

4. **Collision Detection**
   - `rect.collidepoint(pos)`

5. **Sound Effects**
   - Loading and playing audio

6. **Text Rendering**
   - Font loading and text creation

### Design Patterns

1. **Separation of Concerns**
   - `main.py`: Game loop
   - `game.py`: Game logic
   - `menu.py`: Menu system

2. **State Management**
   - Menu state vs. gameplay state
   - Score and problem tracking

3. **Resource Management**
   - Loading assets once
   - Reusing surfaces and fonts

### Potential Enhancements

**Ideas to extend this project**:

1. **Difficulty Levels**
   - Easy, Medium, Hard modes
   - Adjustable number ranges

2. **Timed Mode**
   - Time limit per problem
   - Time bonus for quick answers

3. **High Score System**
   - Save best scores to file
   - Display leaderboard

4. **More Operations**
   - Square roots
   - Exponents
   - Mixed operations

5. **Visual Improvements**
   - Animations
   - Particle effects
   - Better graphics

6. **Sound Enhancements**
   - Background music
   - More varied sound effects

7. **Multiplayer Mode**
   - Two-player split screen
   - Turn-based gameplay

8. **Statistics**
   - Track accuracy per operation
   - Average time per problem
   - Progress graphs

---

## Pygame Best Practices Demonstrated

### 1. Resource Loading
✅ Load resources once in `__init__`, not every frame
```python
def __init__(self):
    self.background_image = pygame.image.load("background.jpg").convert()
```

### 2. Frame Rate Control
✅ Use `clock.tick()` to maintain consistent FPS
```python
clock.tick(30)  # 30 FPS
```

### 3. Event Handling
✅ Process all events in the queue
```python
for event in pygame.event.get():
    # Handle events
```

### 4. Screen Updates
✅ Draw everything, then call `flip()` once
```python
# Draw everything
pygame.display.flip()  # Update screen once
```

### 5. Quitting Properly
✅ Always call `pygame.quit()`
```python
pygame.quit()
```

### 6. Surface Conversion
✅ Use `convert()` for faster blitting
```python
image.convert()
```

### 7. Constants
✅ Define constants for reusable values
```python
SCREEN_WIDTH = 640
BLACK = (0, 0, 0)
```

---

## Common Pygame Pitfalls (Avoided in This Code)

❌ **Don't**: Load images every frame
✅ **Do**: Load once, reuse

❌ **Don't**: Forget to process events
✅ **Do**: Call `pygame.event.get()` every frame

❌ **Don't**: Skip `clock.tick()`
✅ **Do**: Control frame rate

❌ **Don't**: Forget to convert images
✅ **Do**: Use `.convert()` after loading

❌ **Don't**: Ignore `pygame.quit()`
✅ **Do**: Clean up on exit

---

## Conclusion

This math game demonstrates fundamental game development concepts:

- **Game loops** for continuous execution
- **Event handling** for user interaction
- **State management** for game flow
- **Resource management** for media assets
- **Object-oriented design** for code organization

By studying this code, you've learned:
- How Pygame works
- How to structure a game project
- How to handle user input
- How to display graphics and play sounds
- How to implement game logic

**Next Steps**:
1. Run the game and play it
2. Read through the code line by line
3. Modify values (colors, sizes, ranges) to see effects
4. Add new features or improvements
5. Build your own game using these concepts!

**Happy Learning! 🎓🎮**