# An Eye on You
Basically fncking around with OpenCV and cathode ray televisions.

## What the fnck?
> Basically, tomorrow I'm going around Romandie to collect cathode ray televisions, and I want to tinker with a thingy with an eye that follows you from the television.

The basic idea was to make a wall of televisions connected to a [undefined], and the televisions display an eye that follows your face.

![harold](./img/harold.png)

### No for real, what the fnck?
I'm not even sure where the idea came from, but as part of the preparation of an exhibition with interactive artworks, I really, really wanted to make this wall of televisions with eyes that follow you.

## How?
### Software
- Using OpenCV, I start by detecting a face, and surrounding it with a square.
- I look at where this square is located in relation to a grid.
- This grid is more or less divided according to the size of the previous square:
  - If you are close, the squares are bigger (because your face is big)
  - If you are far, the squares are smaller (because the eye must follow your face).
- Once the detection is done, I have a collection of pictures of an eye looking in different directions, and I use the right eye according to the position - the square - to look.

![demo](./img/demo.gif)

#### How to use
1. [Install OpenCV](https://docs.opencv.org/4.x/df/d65/tutorial_table_of_content_introduction.html).
1. Plug a webcam to your computer.
1. Run `main.py`.

### Hardware
To have a little creepy/vintage effect, I felt like using old TVs, because why not. So I went around the Léman to get some of them.

For each television, you can choose to split the signal, or to use it independently. You can put either [Raspberry+webcam](https://qengineering.eu/install-opencv-4.5-on-raspberry-pi-4.html), or [ESP32+ESPCAM](https://github.com/joachimBurket/esp32-opencv), and run the little script on it.

**TODO**: Photos with the tvs.

## Upgrades
- [Use a 3D model](https://medium.com/geekculture/face-detection-in-unity-using-opencv-2df17a9e8ecd) instead of crappy old screenshots.
- Calibrate the grid so that it doesn't go on holiday every other time.

## Credits
- Basis: [Face Detection in 2 Minutes using OpenCV & Python](https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81).
- More basis: [OpenCV Tutorials](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html).
- Model used in the example: [Eye free model V2 - 3d by Oscar creativo](https://sketchfab.com/3d-models/eye-free-model-v2-3d-by-oscar-creativo-f4aa47ab47af42c7a08dfc5b81e9db40).
- Other model considered: [Anatomical Eye ball](https://sketchfab.com/3d-models/anatomical-eye-ball-281784b8e6ff4713991cdee224f07b09).
- Other model considered: [Eye Free Model V.3 by Oscar creativo](https://sketchfab.com/3d-models/eye-free-model-v3-by-oscar-creativo-6042034ca1a44c05bc8044ba79434bbf).
