from pynput.mouse import Listener, Button

# -----------------------------------------------------------
# Gets the cursor position when the left mouse button is clicked
#
# Author: Tyler McGuire (tjm8975)
# -----------------------------------------------------------

def on_click(x, y, button, pressed):
    """Print the cursor position when the left mouse button is clicked"""
    if pressed and button == Button.left:
        print("Mouse Clicked: (%d, %d)" %(x, y))
        listener.stop()

# Create the Listener
with Listener(on_click=on_click) as listener:
    listener.join()