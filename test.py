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


def re_number(path, start_num):
    print('path: {}'.format(path))
    print('Renumbering all files to start from {}...'.format(start_num))

    for file_name in os.listdir(path):
        file_type = os.path.splitext(file_name)[1]

        if(file_type == '.pdf'):
            indicator = file_name.split('-')[0]
            #if file_name.startswith(indicator):
                
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
    path = r'' #copy file path and paste in between the quotes
    start_num = 1   # where you want to start counting from
    indicator = ''    # the repeating value in your files
    files_action = 're-number' #'rename' or 'append' or 're-number'
    #----------------------------------------------------------------------#

    if files_action == 'rename':
        rename(path, indicator, start_num)
    elif files_action == 'append':
        append_to_front(path, indicator, start_num)
    elif files_action == 're-number':
        re_number(path, start_num)


if __name__ == "__main__":
    main()


