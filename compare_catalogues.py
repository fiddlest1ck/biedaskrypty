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

path_a = '/home/fiddlest1ck/old_catalog'
path_b = '/home/fiddlest1ck/new_catalog'
path_create = '/home/fiddlest1ck/tmp_cat'
# files = []
# if True:
#     for x in ['dokumenty', 'sprawy', 'metadane']:
#         new_files_path = '{}/{}'.format(path_a, x)
#         old_files_path = '{}/{}'.format(path_b, x)
#         path_create1 = '{}/{}'.format(path_create, x)
#         if os.listdir(new_files_path):
#             dircomp = filecmp.dircmp(new_files_path, old_files_path)
#             for function in [dircomp.left_only, dircomp.diff_files, dircomp.right_list]:
#                 if function == dircomp.right_list:
#                     new_path(new_files_path, path_create1, x, files, function, dircomp.diff_files)
#                 new_path(new_files_path, path_create1, x, files, function)
#     print(set(files))
#     for z, g in set(files):
#         copyfile(z, g)

deleted_files = []
new_files = []
delete_modified_files = []
modified_files = []
for x in ['dokumenty', 'metadane']:
    old_files_path = '{}/{}'.format(path_a, x)
    new_files_path = '{}/{}'.format(path_b, x)
    dircomp = filecmp.dircmp(old_files_path, new_files_path)
    print('{}/{}'.format(new_files_path, ''.join(dircomp.right_only)))
    if dircomp.left_only:
        deleted_files.append('{}/{}'.format(old_files_path, ''.join(dircomp.left_only)))
    if dircomp.right_only:
        new_files.append('{}/{}'.format(new_files_path, ''.join(dircomp.right_only)))
    if dircomp.diff_files:
        delete_modified_files.append('{}/{}'.format(old_files_path, ''.join(dircomp.diff_files)))
        modified_files.append('{}/{}'.format(new_files_path, ''.join(dircomp.diff_files)))
print({'deleted_files': deleted_files, 'new_files': new_files, 'modified_files': modified_files})
