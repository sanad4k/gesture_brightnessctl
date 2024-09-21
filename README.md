Project Overview

This project demonstrates the use of OpenCV and MediaPipe to adjust computer display brightness in real-time based on the distance between the index and thumb fingers.

Dependencies

    OpenCV: https://opencv.org/
    MediaPipe: https://github.com/google-ai-edge/mediapipe
    System Subprocess: For interacting with the system and executing commands.
    Brightness Control Tool: A command-line tool like brightnessctl to adjust system brightness.

Installation

    Install OpenCV and MediaPipe: Follow the official instructions for your operating system.
    Install Brightness Control Tool: If not already installed, install brightnessctl or a similar tool for your system.

Usage

    Run the script: Execute the Python script containing the project code.
    Position your hands: Place your index and thumb fingers in front of the webcam.
    Observe brightness adjustment: As you move your fingers closer or farther apart, the computer's display brightness will adjust accordingly.

Customization

    System Compatibility: The script assumes the use of brightnessctl. You may need to modify the code to interact with different brightness control tools or methods on your system.
    Distance Calibration: Adjust the distance thresholds in the code to fine-tune the sensitivity of brightness adjustment.
    Additional Features: Consider adding features like automatic brightness adjustment based on ambient light or user-defined presets.

Purpose

This project was created to gain practical experience with OpenCV and MediaPipe. It demonstrates how these libraries can be used for real-time computer vision applications and system interaction.

Note: This project serves as a learning exercise and may not be suitable for production use without further refinement and testing.
