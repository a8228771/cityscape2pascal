import os

def image_id(rootdir):
    a = []
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            index = filename.rfind('_')
            filename = filename[:index]
            dirname = parent[len(rootdir)+1:]
            # filename = filename.strip('_leftImg8bit.png')
            filename = dirname + '/' + filename
            a.append(filename)
    return a