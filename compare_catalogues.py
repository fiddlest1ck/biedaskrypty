import os
import filecmp
from os.path import join
from collections import OrderedDict
from shutil import copyfile

def src_cp_tuple(new_package_path, path_for_create, a):
    return ('{}/{}'.format(new_package_path, a),'{}/{}'.format(path_for_create, a))

def new_path(new_package_path, path_for_create, x , files_list, first_item, other_items=None):
    if other_items:
        path = [files_list.append(src_cp_tuple(new_package_path, path_for_create, item)) for item in first_item if item not in other_items]
    path = [files_list.append(src_cp_tuple(new_package_path, path_for_create, item)) for item in first_item]
    return path

path_a = '/home/fiddlest1ck/cat1'
path_b = '/home/fiddlest1ck/cat2'
path_create = '/home/fiddlest1ck/tmp_cat'
files = []
if True:
    for x in ['dokumenty', 'sprawy', 'metadane']:
        new_files_path = '{}/{}'.format(path_a, x)
        old_files_path = '{}/{}'.format(path_b, x)
        path_create1 = '{}/{}'.format(path_create, x)
        if not os.path.exists(path_create):
            os.mkdir(path_create)
            os.mkdir(path_create1)
        if os.listdir(new_files_path):
            dircomp = filecmp.dircmp(new_files_path, old_files_path)
            for function in [dircomp.left_only, dircomp.diff_files, dircomp.right_list]:
                if function == dircomp.right_list:
                    new_path(new_files_path, path_create1, x, files, function, dircomp.diff_files)
                new_path(new_files_path, path_create1, x, files, function)
    print(set(files))
    for z, g in set(files):
        copyfile(z, g)
