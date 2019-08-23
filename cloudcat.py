#!/usr/bin/python3

import subprocess
import sys
import os
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
    parser.add_argument("-t","--type",help="Size of the instance to use. From cheapest to most expensive: p3.2xlarge, p3.8xlarge and p3.16xlarge.",choices=['p3.2xlarge','p3.8xlarge','p3.16xlarge'], action="store")
    parser.add_argument("-f","--file",help="File containing hashes to crack", action="store")
    parser.add_argument("-m","--mode",help="Hashtype cracking mode you want to use", action="store")
    parser.add_argument("-i","--identity",help="SSH identity on AWS to use (only select this if you're sure you have the correct key!)", action="store")
    parser.add_argument("-r","--region",help="AWS region to create the cracking instance in.", action="store")
    parser.add_argument("-l","--length",help="Length of the hash cracking run. Short is just rockyou.txt, medium is rockyou and fav_wordlist, and long is those two and crackstation.txt.", action="store")
    parser.add_argument("-g","--single",help="Create an Amazon Security Group where only your current public IP address is allowed through the firewall. You will be unable to SSH to the server from anywhere other than here.", action="store")
    parser.add_argument("-o","--double",help="Create an Amazon Security Group where your current pulic IP address and one other public IP address is allowed through the firewall. This second location should be somewhere you always have access to (e.g. home, office).", action="store")
    parser.add_argument("-d","--destroy",help="Destroy CloudCat AWS P3.X instances.",action='store_true')
    parser.add_argument("--info",help="Print information on Hashcat cracking statistics and AWS P3 instance costs.", action="store_true")
    return parser.parse_args()

info = """
"""

def main():
    args = parse_args()
    if os.path.isfile('./external_vars.yml') is False:
        print("Please configure CloudCat with your region and AWS Access and AWS Secret Keys.")
        sys.exit(0)
    if args.info:
        print(info)
        sys.exit(0)
    if args.destroy:
        destroy = ['ansible-playbook', 'cloudcat-destroy.yml']
        subprocess.call(destroy)
        sys.exit(0)
    if args.type and (args.identity is None or args.file is None or args.mode is None or args.region is None or args.length is None):
        parser = argparse.ArgumentParser()
        parser.error("You have defined an instance type but not additional parameters to create the instance. Exiting...")
        sys.exit(0)
    if args.type:
        shutil.copyfile(args.file, 'roles/taskcat/files/hashes.txt')
        create = ['ansible-playbook', 'cloudcat-create.yml', '-e']
        ops = ["type={} hashmode={} ssh_key={} identity={} oneip={} length={} guestip={}".format(args.type,args.mode,args.identity,args.identity,args.single,args.length,args.double)]
        create.extend(ops)
        print(create)
        print("Creating CloudCat cracking instance with " + args.type + "accelerated computing instance.")
        #subprocess.call(create)

if __name__ == "__main__":
    banner()
    main()
