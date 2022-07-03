def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    a = "#%02x%02x%02x"
    return a % rgb


