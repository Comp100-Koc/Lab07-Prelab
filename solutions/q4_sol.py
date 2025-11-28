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
]

def insert_path(tree, components):
    """Recursively inserts components into the directory tree."""
    if not components:
        return
    current = components[0]
    for i in range(len(tree)):
        # Check if the current directory exists
        if isinstance(tree[i], str) and tree[i] == current:
            if i + 1 < len(tree) and isinstance(tree[i + 1], list):
                insert_path(tree[i + 1], components[1:])
            return
    # Add a new directory or file
    if len(components) == 1:
        if "." in current:  # It's a file
            tree.append(current)
        else:  # It's an empty directory
            tree.append(current)
            tree.append([])
    else:
        tree.append(current)
        subtree = []
        tree.append(subtree)
        insert_path(subtree, components[1:])

def reconstruct_dir(paths):
    root = []
    for path in paths:
        components = path.strip("/").split("/")
        insert_path(root, components)
    return root

result = reconstruct_dir(paths)
print(result)