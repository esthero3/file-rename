import os

path = ''
start_num = 1

for x in os.listdir(path):
    if x.startswith('21'):
        print(x)
        
        # old_name = x
        # new_name = old_name.replace('21', str(start_num), 1)
        # start_num += 1

        # path_old_name = '{}/{}'.format(path, old_name)
        # path_new_name = '{}/{}'.format(path, new_name)
        # os.rename(path_old_name, path_new_name)