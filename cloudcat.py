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

CloudCat - The cloud-based password cracker.
        """)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--size",help="Size of the instance to use. From cheapest to most expensive: p3.2xlarge, p3.8xlarge and p3.16xlarge.",choices=['p3.2xlarge','p3.8xlarge','p3.16xlarge']required=True)
    parser.add_argument("-f","--file",help="File containing hashes to crack",required=True)
    parser.add_argument("-m","--mode",help="Hashtype cracking mode you want to use",required=True)
    parser.add_argument("-i","--identity",help="SSH identity on AWS to use (only select this if you're sure you have the correct key!)")
    parser.add_argument("-g","--group",help="Create an Amazon Security Group where only your current public IP address is allowed through the firewall. You will be unable to SSH to the server from anywhere other than here.")
    parser.add_argument("-o","--other-groups",help="Create an Amazon Security Group where your current pulic IP address and one other public IP address is allowed through the firewall. This second location should be somewhere you always have access to (e.g. home, office).")
    parser.add_argument("-d","--destroy",help="Destroy ALL AWS P3.X instances. This should only be used if you are 100% sure no other AWS P3 instances are running on your account.")
    return parser.parse_args()

def main():
    args = parse_args()
    array = ['ansible-playbook', 'creation.yml', '-e']
    ops = ["size={} file={} mode={}".format(args.size,args.file,args.mode)]
    array.extend(ops)
    subprocess.call(array)

if __name__ == "__main__":
    banner()
    main()
