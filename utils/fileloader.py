import os

def get_files_by_type(input_dir, allowed_exts):
    all_files=[]
    for f in os.listdir(input_dir):
        full=os.path.join(input_dir,f)
        if os.path.isfile(full) and os.path.splitext(f)[1] in allowed_exts:
            all_files.append(f)
    return all_files

