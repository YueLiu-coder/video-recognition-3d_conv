import os
import shutil

def all_path(dirname):

    result = []#所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            result.append(apath)

    return result

avi_file = all_path("./data")
for i in avi_file:
    dict_name = i[:-12]
    # 不存在文件夹，则创建
    if not os.path.exists(dict_name):
        print(dict_name)
        os.mkdir(dict_name)
    # 存在，则将文件加入到文件夹中
    else:
        shutil.move(i, dict_name)
        pass

