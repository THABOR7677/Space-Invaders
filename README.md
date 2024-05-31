# Space Invaders Game

Welcome to the Space Invaders game project! This project is designed to help you practice and improve your programming skills using Python. This README file provides an overview of the project, installation instructions, a guide on how to play the game, and insights into the code structure.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Code Structure](#code-structure)
- [Contributing](#contributing)


## Project Overview

Space Invaders is a classic arcade game where the player controls a spaceship at the bottom of the screen and must shoot down waves of incoming aliens. This project recreates the game using Python and the Pygame library, providing a fun way to practice programming and game development concepts.
Credit to Bro Code and Nick for their programming lessons on youtube.
## Features

- Classic Space Invaders gameplay
- Multiple levels with increasing difficulty
- Score tracking
- Sound effects and background music
- Smooth animations and responsive controls

## Installation

To run the Space Invaders game on your local machine, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/space-invaders.git
    cd space-invaders
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the game**:
    ```sh
    python main.py
    ```

## How to Play

- **Movement**: Use the left and right arrow keys to move your spaceship.
- **Shooting**: Press the spacebar to shoot bullets at the invading aliens.
- **Objective**: Destroy all aliens before they reach the bottom of the screen. Avoid getting hit by the aliens' bullets.

As you progress through the levels, the aliens will move faster and become more challenging to defeat. Try to achieve the highest score possible!

## Code Structure

Here is an overview of the key files and directories in the project:

- `main.py`: The entry point of the game. This file initializes the game and handles the main game loop.
- `spaceship.py`: Contains the `Spaceship` class, which manages the spaceship's movement and shooting.
- `alien.py`: Contains the `Alien` class, which defines the behavior of the invading aliens.
- `laser.py`: Contains the `Laser` class, which handles the bullets fired by the player and aliens.
- `game.py`: Contains the `Game` class, which manages the overall game state, including level progression and collision detection.
- `assets/`: Directory containing game assets such as images and sounds.
- `README.md`: This file, providing documentation for the project.

## Contributing

Contributions are welcome! If you have any suggestions for improvements or new features, feel free to create an issue or submit a pull request. Please ensure that your contributions adhere to the project's coding standards and guidelines.

Thank you for checking out the Space Invaders game project. Have fun playing and happy coding!
