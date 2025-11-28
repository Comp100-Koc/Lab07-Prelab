paths = [
    "/home/user/docs/file1.txt",
    "/home/user/docs/file2.txt",
    "/home/user/videos/ibiza_trip.mp4",
    "/home/user/videos/christmas_party.mp4",
    "/home/user/videos/movies/isle_of_dogs.mp4",
    "/home/user/videos/movies/la_haine.mp4",
    "/home/user/downloads",
    "/home/system/system32",
    "/home/system/config.ini",
    "/dev/input/mouse",
    "/dev/input/gamepad/ps5_controller_conf.ini",
] # Do not change paths list

def reconstruct_dir(paths):
    """Recursively inserts components into the directory tree. Returns the directory tree."""
    return