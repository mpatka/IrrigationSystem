from os import listdir

from joblib import load


def load_newest(path):
    joblib_filenames = []
    for filename in listdir(path):
        if filename.endswith('.joblib'):
            joblib_filenames.append(filename)

    if not joblib_filenames:
        raise Exception('no ml model found')

    newest_model_name = joblib_filenames[-1]
    return load(path + newest_model_name)
