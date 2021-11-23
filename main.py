#!/usr/bin/env python3

import cv2
import os

# Max grid to be used as reference
GRID_SIZE = 5

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def lurk():
    # To capture video from webcam.
    cap = cv2.VideoCapture(0)

    # To use a video file as input
    # cap = cv2.VideoCapture('filename.mp4')

    # Size of the cam
    cap_w = int(cap.get(3))
    cap_h = int(cap.get(4))

    # Array of eyes
    # Inspired from https://stackoverflow.com/a/30230738
    eyes = []
    folder = "./eyes/"
    for filename in ["{}.png".format(file) for file in
                     sorted([int(file[:-4]) for file in os.listdir(folder) if file[-4:] == ".png"])]:  # ... yea
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            eyes.append(img)

    # Mapping for the eyes in case the grid is smaller than GRID_SIZE
    eyes_map = {1: {0: 12}, 3: {0: 6, 1: 7, 2: 8, 3: 11, 4: 12, 5: 13, 6: 16, 7: 17, 8: 18}}

    def grid_pos(center, size=(cap.get(3), cap.get(4)), grid_size=GRID_SIZE):
        """
        :param center: Center to be used
        :param size: Dimensions of the camera
        :param grid_size: Grid size to be used
        :return: Position in the grid.
        """
        return int((center[0] // (size[0] // grid_size)) + grid_size * (center[1] // (size[1] // grid_size)))

    def draw_grid(img, size=(cap.get(3), cap.get(4)), grid_size=GRID_SIZE):
        """
        Helper to see the grid.
        :param img: Where to draw
        :param size: Dimensions of the camera
        :param grid_size: Grid size to be used
        """
        x_grid = int(size[0] // grid_size)
        y_grid = int(size[1] // grid_size)
        w = x_grid - 1
        h = y_grid - 1
        for i in range(grid_size):
            for j in range(grid_size):
                x = i * x_grid
                y = j * y_grid
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 128, 0), 3)

    while True:
        # Read the frame
        _, img = cap.read()

        # Reverse lol
        img = cv2.flip(img, 1)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around the first face
        grid = GRID_SIZE
        for (x, y, w, h) in faces:
            # Calculate the grid size
            # Grid size is an odd integer between 1 and GRID_SIZE
            grid = cap_w // w if min(cap_w, cap_h) == cap_w else cap_h // h
            if not grid % 2:
                grid += 1
            grid = min(grid, GRID_SIZE)

            # Actually draws the rectangle (with center)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            center = (x + w // 2, y + h // 2)
            cv2.circle(img, center, 3, (255, 0, 0))

            # Choose the correct "eye"
            pos_in_grid = grid_pos(center, grid_size=grid)
            # If we have a smaller grid, uses the mapping
            if grid < GRID_SIZE:
                pos_in_grid = eyes_map[grid][pos_in_grid]

            eye = eyes[pos_in_grid]
            break

        draw_grid(img, grid_size=grid)

        # Display both the camera and the "eye".
        cv2.imshow('img', img)
        cv2.imshow('target', eye)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    # Release the VideoCapture object
    cap.release()


if __name__ == "__main__":
    lurk()
