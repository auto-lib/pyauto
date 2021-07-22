import glob

def filenames(_):

    return glob.glob('*.txt')

def contents(_):

    res = []
    for name in _.filenames:
        with open(name) as f: res.append(f.read())
    return res