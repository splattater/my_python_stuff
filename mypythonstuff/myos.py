def get_abs_files(dir_path):
    """Search all files in a given dir and its subdirs."""
    import os

    if not os.path.isdir(dir_path):
        return []

    found = []

    for root, subdirs, files in os.walk(dir_path, topdown=True):
        for file in files:
            found.append(os.path.join(root, file))

    return found
