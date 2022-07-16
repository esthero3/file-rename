import os

def rename(path, indicator, start_num):
    print('path: {}'.format(path))
    print('Renaming all files that start with {} with numbers starting from {}...'
    .format(indicator, start_num))
    for file_name in os.listdir(path):
        if file_name.startswith(indicator):
            
            old_name = file_name
            new_name = old_name.replace(indicator, str(start_num), 1)
            start_num += 1

            path_old_name = '{}/{}'.format(path, old_name)
            path_new_name = '{}/{}'.format(path, new_name)
            os.rename(path_old_name, path_new_name)
    print('Renaming Completed')


def append_to_front(path, indicator, start_num):
    print('path: {}'.format(path))
    print('Starting append with the number:{} for all files starting with {}'
    .format(start_num, indicator))
    for file_name in os.listdir(path):
        if file_name.startswith(indicator):

            old_name = file_name
            new_name = '{}-{}'.format(start_num, old_name)
            start_num += 1

            path_old_name = '{}/{}'.format(path, old_name)
            path_new_name = '{}/{}'.format(path, new_name)
            os.rename(path_old_name, path_new_name)
    print('Apending Completed.')
            


def main():
    #-------------------------Change these -------------------------------#
    path = r''
    start_num = 0   # where you want to start counting from
    indicator = ''    # the repeating value in your files
    files_action = '' #either 'rename' or 'append'
    #----------------------------------------------------------------------#

    if files_action == 'rename':
        rename(path, indicator, start_num)
    elif files_action == 'append':
        append_to_front(path, indicator, start_num)


if __name__ == "__main__":
    main()


