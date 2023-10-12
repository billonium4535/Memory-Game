import pygetwindow
import pyautogui
import time

# Activate window
# 1.png - Paint
window = pygetwindow.getWindowsWithTitle("FP4")[0]
window.activate()

# Get window co-ords
window_left = window.topleft[0]
window_top = window.topleft[1]
window_width = window.bottomright[0] - window.topleft[0]
window_height = window.bottomright[1] - window.topleft[1]

# Capture a screenshot of the specified window
screen = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))

# Find occurrences of the image (allowing partial matches)
box_list = list(pyautogui.locateAllOnScreen(
    "./Icons/Hidden_Icon.png", grayscale=True, confidence=0.9,
    region=(window_left, window_top, window_width, window_height)
))

# Store pairs of identical icons
icon_pairs = []

# Set to store clicked icon positions
clicked_icons = set()

# Click on each occurrence and remember the image displayed
for i, box in enumerate(box_list):
    x, y = box.left, box.top

    # Check if this icon has already been clicked
    if any(x in range(cx, cx + 25) and y in range(cy, cy + 25) for cx, cy in clicked_icons):
        continue

    pyautogui.click(x, y)
    print(f"Clicked icon {i + 1}")
    icon_pairs.append((x, y))

    # Add this icon's position to the set of clicked icons
    clicked_icons.add((x, y))

    # Add a delay to simulate displaying the image
    time.sleep(2)

input("Waiting...")

# Click on every icon again, clicking identical icons consecutively
for x, y in icon_pairs:
    pyautogui.click(x, y)
    print(f"Clicked icon at ({x}, {y})")

    # Add a delay to simulate displaying the image
    time.sleep(2)
