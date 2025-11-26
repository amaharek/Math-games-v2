#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Configuration file for Math Game
Contains all constants and settings
"""

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (232, 96, 86)

# Game settings
FPS = 30
FONT_SIZE_LARGE = 65
FONT_SIZE_MEDIUM = 40
FONT_SIZE_SMALL = 25
FONT_SIZE_SCORE = 20

# Asset paths
ASSETS_PATH = "src/assets"
IMAGES_PATH = f"{ASSETS_PATH}/images"
SOUNDS_PATH = f"{ASSETS_PATH}/sounds"
FONTS_PATH = f"{ASSETS_PATH}/fonts"

# Specific asset files
BACKGROUND_IMAGE = "math-game-background.png"
SYMBOLS_IMAGE = "symbols.png"
SOUND_CORRECT = "item1.ogg"
SOUND_INCORRECT = "item2.ogg"
BACKGROUND_MUSIC = "background-music.mp3"
FONT_KENVECTOR = "kenvector_future.ttf"
FONT_XPRESSIVE = "XpressiveBlack Regular.ttf"

# Game mechanics
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
BUTTON_SPACING = 50
PROBLEMS_PER_GAME = 20
POINTS_PER_CORRECT = 10
