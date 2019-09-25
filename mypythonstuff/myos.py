def get_abs_files(dir_path):
    """Search all files in a given dir and its subdirs."""
    import os

    if not os.path.isdir(dir_path):
        return []

    found_files = []

    def get_more(top):
        for root, subdirs, files in os.walk(dir_path, topdown=True):
            for file in files:
                found_files.append(os.path.join(root, file))
            for subdir in subdirs:
                get_more(os.path.join(root, subdir))

    return found_files
