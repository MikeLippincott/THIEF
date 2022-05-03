import os
"""

"""

# Set up sub directories
def set_up_dirs(new_dir):
    """
    check if current directory + :param new_dir: is a path

    :return:
    if not a new_dir path will be created
    """
    path = os.getcwd()
    if not path.endswith('/'):
        path = path + '/'
    print(path)
    # List of relative path's to create if not present
    if_exists = os.path.exists((f'{path}{new_dir}'))
    print(if_exists)
    if not if_exists:
        os.makedirs((f'{path}{new_dir}'))


def main():
    return

if __name__ == '__main__':
    main()




