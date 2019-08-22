#!/usr/bin/python3

import subprocess
import sys
import argparse
import shutil

def banner():
	print("""
 _______  ___      _______  __   __  ______   _______  _______  _______ 
|       ||   |    |       ||  | |  ||      | |       ||   _   ||       |
|       ||   |    |   _   ||  | |  ||  _    ||       ||  |_|  ||_     _|
|       ||   |    |  | |  ||  |_|  || | |   ||       ||       |  |   |  
|      _||   |___ |  |_|  ||       || |_|   ||      _||       |  |   |  
|     |_ |       ||       ||       ||       ||     |_ |   _   |  |   |  
|_______||_______||_______||_______||______| |_______||__| |__|  |___|

CloudCat - The cloud-based password cracker.
        """)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--type",help="Size of the instance to use. From cheapest to most expensive: p3.2xlarge, p3.8xlarge and p3.16xlarge.",choices=['p3.2xlarge','p3.8xlarge','p3.16xlarge'],required=True)
    parser.add_argument("-f","--file",help="File containing hashes to crack",required=True)
    parser.add_argument("-m","--mode",help="Hashtype cracking mode you want to use",required=True)
    parser.add_argument("-i","--identity",help="SSH identity on AWS to use (only select this if you're sure you have the correct key!)")
    parser.add_argument("-l","--length",help="Length of the hash cracking run. Short is just rockyou.txt, medium is rockyou and fav_wordlist, and long is those two and crackstation.txt."
    parser.add_argument("-g","--single",help="Create an Amazon Security Group where only your current public IP address is allowed through the firewall. You will be unable to SSH to the server from anywhere other than here.",action='store_true')
    parser.add_argument("-o","--double",help="Create an Amazon Security Group where your current pulic IP address and one other public IP address is allowed through the firewall. This second location should be somewhere you always have access to (e.g. home, office).")
    parser.add_argument("-d","--destroy",help="Destroy CloudCat AWS P3.X instances.",action='store_true')
    return parser.parse_args()

def main():
    args = parse_args()
    shutil.copyfile(args.file, 'roles/taskcat/files/hashes.txt')
    create = ['ansible-playbook', 'cloudcat-create.yml', '-e']
    ops = ["type={} hashmode={} ssh_key={} identity={} oneip={} length={} guestip={}".format(args.type,args.mode,args.identity,args.single,args.length,args.double)]
    if args.destroy:
        destroy = ['ansible-playbook', 'cloudcat-destroy.yml']
        subprocess.call(arrayd)
        sys.exit()
    array.extend(ops)
    subprocess.call(create)

if __name__ == "__main__":
    banner()
    main()
