__author__ = 'oleksandr'

import argparse
import re
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]

def get_args():
    parser = argparse.ArgumentParser(description='Genre sort')
    parser.add_argument('--folder', help='Folder with raw data')
    parser.add_argument('--dump', help='Dump file')
    
    args = parser.parse_args()
    folder =  args.folder
    dump_data = args.dump
    
    return (folder, dump_data)

def process_line(line):
    email = re.findall(r"\b(?:\w|\.)+(?:@| @ |\(at\)| at |&#x40;)(?:\w|\.)+(?:\.)[a-zA-Z]{2,4}\b", line)[0]
    genre = re.findall('(?<="genre":")\w*', line)[0]
    return email, genre

def make_movement(file_path, copy_to_path):
    #os.system('cp ' + file_path + ' ' +  copy_to_path)
    newfile = os.path.join(copy_to_path, os.path.basename(file_path))
    os.system('python html2text.py ' + file_path + ' > ' +  newfile)
    print 'new file', newfile

def prepare_folder(genre):
    genre_path = main_dir+'/outdata/'+genre
    if not os.path.exists(os.path.join(os.path.join(main_dir, 'outdata'), genre)):
        os.makedirs(genre_path)
        return genre_path
    return genre_path
        

def add_genre(data, f_list):
    for item in f_list:
        if data[0]+".editor.editor" == os.path.split(item)[1]:
            genre_folder = prepare_folder(data[1])
            make_movement(item, genre_folder)
            

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
    f_list = files_list(dataFiles_dir)
    #print(f_list)
    if os.path.isdir(dataFiles_dir) != True:
        print "Data folder does not exists!"
        return 0
    try:
        os.makedirs('outdata')
    except OSError:
        print "Can't create directory."
        #return 0
    for line in open(args[1]).readlines():
        data = process_line(line)
        add_genre(data, f_list)
        
if __name__=="__main__":
    main()
    