__author__ = 'oleksandr'

import argparse
import re
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]

folder = None
dump_data = None

def get_args():
    global folder
    global dump_data

    parser = argparse.ArgumentParser(description='Genre sort')
    parser.add_argument('--folder', help='Folder with raw data')
    parser.add_argument('--dump', help='Dump file')
    
    args = parser.parse_args()
    folder =  args.folder
    dump_data = args.dump
    
    return folder, dump_data

def process_line(line):
    try:
        email = re.findall(r"\b(?:\w|\.)+(?:@| @ |\(at\)| at |&#x40;)(?:\w|\.)+(?:\.)[a-zA-Z]{2,4}\b", line)[0]
        genre = re.findall('(?<="genre":")\w*', line)[0]
        return email, genre
    except:
        return None

def make_movement(file_path, copy_to_path):
    newfile = os.path.join(copy_to_path, os.path.basename(file_path))
    os.system('pypy html2text.py ' + file_path + ' > ' +  newfile)
    #os.system('perl html2txt.pl  ' + file_path + ' > ' +  newfile)
    #perl html2txt.pl
    #os.system('cp ' + file_path + ' ' +  newfile)
    print 'new file', newfile

def prepare_folder(genre):
    genre_path = main_dir+'/outdata/'+genre
    if not os.path.exists(os.path.join(os.path.join(main_dir, 'outdata'), genre)):
        os.makedirs(genre_path)
        return genre_path
    return genre_path

def retrieve_file(name):
    prefix = (name[0:1], name[0:2], name[0:3])
    #try:
    raw_path = os.path.join(main_dir, folder)
    #print raw_path
    #except:
    #    print main_dir, folder

    for p in prefix:
        raw_path = os.path.join(raw_path, p)

    if os.path.exists(raw_path):
        bottom_files = os.listdir(raw_path)

        match_file = filter(lambda n: name in n and 'editor' in n, bottom_files)

        if not match_file is None and len(match_file) > 0:
            full_name = os.path.join(raw_path, match_file[0])
            print full_name
            return full_name
    return None



def add_genre(data):
    file_name = data[0]
    genre = data[1]

    file_path = retrieve_file(file_name)

    if file_path is None:
        return

    genre_folder = prepare_folder(genre)
    make_movement(file_path, genre_folder)


def files_list(directory):
    lst = []
    for i in os.listdir(directory):
        item = os.path.join(directory, i)
        if os.path.isdir(item):
            lst.extend(files_list(item))
        else:
            lst.append(item)
    return lst

def main():
    args = get_args()
    dataFiles_dir = os.path.join(main_dir, args[0])
    print 'processing', dataFiles_dir

    #f_list = files_list(dataFiles_dir)

    #print 'files count', len(f_list)
    #print(f_list)
    if not os.path.isdir(dataFiles_dir):
        print "Data folder does not exists!"
        return 0
    try:
        if not os.path.exists('outdata'):
            os.makedirs('outdata')
    except OSError:
        print "Can't create directory."
	return 0

    entries = 0
    for line in open(args[1]).readlines():
        data = process_line(line)
        if data is None:
            continue
        add_genre(data)
        entries += 1
        print 'processed', entries
        
if __name__=="__main__":
    main()
    
