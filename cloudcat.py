#!/usr/bin/python3

import subprocess
import datetime
import argparse

def banner():
	print("""
 _______  ___      _______  __   __  ______   _______  _______  _______ 
|       ||   |    |       ||  | |  ||      | |       ||   _   ||       |
|       ||   |    |   _   ||  | |  ||  _    ||       ||  |_|  ||_     _|
|       ||   |    |  | |  ||  |_|  || | |   ||       ||       |  |   |  
|      _||   |___ |  |_|  ||       || |_|   ||      _||       |  |   |  
|     |_ |       ||       ||       ||       ||     |_ |   _   |  |   |  
|_______||_______||_______||_______||______| |_______||__| |__|  |___|
        """)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--size",help="Size of the instance to use",required=True)
    parser.add_argument("-f","--file",help="File containing hashes to crack",required=True)
    parser.add_argument("-m","--mode",help="Hashtype cracking mode you want to use",required=True)
    return parser.parse_args()

def main():
    args = parse_args()
    array = ['ansible-playbook', 'creation.yml']
    ops = ['--extra-vars']
    ops.append('\"size=' + args.size)
    ops.append('file=' + args.file)
    ops.append('mode=' + args.mode + '\"')
    #ops.append('\'{\"size\":\"' + args.size + '\"')
    #ops.append(',\"file\":\"' + args.file + '\"')
    #ops.append(',\"mode\":\"' + args.mode + '\"}\'')
    array.extend(ops)
    print(array)
    print(' '.join(array))
    subprocess.call(array)

if __name__ == "__main__":
    banner()
    main()
