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
                  www.github.com/stormfleet/cloudcat
        """)

def parse_args():
    parser = argparse.ArgumentParser(description="Example usage: ./cloudcat.py -t p3.2xlarge -f /path/to/hashes.txt -m 1000 -i aws-id -k ssh-keyname -l short")
    parser.add_argument("-t","--type",help="Size of the instance to use. From cheapest to most expensive: p3.2xlarge, p3.8xlarge and p3.16xlarge.",choices=['p3.2xlarge','p3.8xlarge','p3.16xlarge'], action="store")
    parser.add_argument("-f","--file",help="File containing hashes to crack.", action="store")
    parser.add_argument("-m","--mode",help="Hashtype cracking mode you want to use. This should correspond to the modes listed on Hashcat's website.",type=int, action="store")
    parser.add_argument("-i","--identity",help="AWS identity to use (only select this if you're sure you have the correct key!).", action="store")
    parser.add_argument("-k","--ssh-key",dest="sshkey",help="SSH key-file name. Used to connect to created CloudCat instances to conduct tasks and launch Hashcat.", action="store")
    parser.add_argument("-l","--length",help="Length of the hash cracking run. Short is just rockyou.txt, medium is rockyou and fav_wordlist, and long is those two and crackstation.txt.",choices=['short','medium','long'], action="store")
    parser.add_argument("--guest-ip",dest="double",help="Create an Amazon Security Group where your current pulic IP address and one other public IP address is allowed through the firewall. This second location should be somewhere you always have access to (e.g. home, office).", action="store")
    parser.add_argument("--setup",help="Perform CloudCat setup to configure AWS API keys and region.", action="store_true")
    parser.add_argument("-d","--destroy",help="Destroy CloudCat AWS P3.X instances.", action='store_true')
    parser.add_argument("-v","--verbose",help="Add verbosity to CloudCat execution.", action="store_true")
    return parser.parse_args()

varsample = """
access: {}
secret: {}
region: {}
wordsnap: {}
"""

def configure():
    accesskey = input("[?] Enter your AWS Access key for storage in external_vars.yml (encrypted): ")
    secretkey = input("[?] Enter your AWS Secret Key for storage in external_vars.yml (encrypted): ")
    region = input("[?] Enter your AWS region for storage in external_vars.yml (encrypted): ")
    wordsnap = input("[?] Enter your AWS wordlist snapshot (if you have one), e.g. snap-fa019v0a.. for storage in external_vars.yml: ")
    ev = open("external_vars.yml","w+")
    ev.write(varsample.format(accesskey,secretkey,region,wordsnap))
    ev.close()
    print("[+] AWS keys and region written to file. Encrypting external_vars.yml with ansible-vault...")
    subprocess.call(["ansible-vault", "encrypt", "external_vars.yml"])
    print("[+] Setup complete, CloudCat can now be executed.")
    sys.exit(0)

def setup():
    if os.path.isfile('./external_vars.yml') is False:
        configure()
    if os.path.isfile('./external_vars.yml') is True:
        usrchk = input("[?] external_vars.yml file is already configured. Erase and reconfigure (y/n)? ")
        while usrchk.lower() not in {"y", "n"}:
            usrchk = input("[?] Please enter y/n: ")
        if usrchk.lower() == "y":
            configure()
        else:
            print("[!] Exiting...")
            sys.exit(0)

def main():
    args = parse_args()
    parser = argparse.ArgumentParser()
    if args.setup:
        setup()
    if os.path.isfile('./external_vars.yml') is False:
        print("[!] Please configure CloudCat with your region and AWS Access and AWS Secret Keys, './cloudcat.py --setup'.")
        sys.exit(0)
    if args.verbose:
        create = ['ansible-playbook', 'cloudcat-create.yml', '-vvv', '-e']
    else:
        create = ['ansible-playbook', 'cloudcat-create.yml', '-e']
    if args.destroy:
        if args.destroy and args.type:
            parser.error("[!] You can't destroy and create infrastructure at the same time!")
            sys.exit(0)
        destroy = ['ansible-playbook', 'cloudcat-destroy.yml']
        if args.verbose:
            destroy.extend(['-vvv'])
        print("[-] Destroying CloudCat cracking instances...")
        subprocess.call(destroy)
        sys.exit(0)
    if args.type and (args.sshkey is None or args.identity is None or args.file is None or args.mode is None or args.length is None):
        parser.error("[!] You have defined an instance type but not additional parameters to create the instance. Exiting...")
        sys.exit(0)
    if args.type:
        shutil.copyfile(args.file, 'roles/taskcat/files/hashes.txt')
        ops = ["type={} hashmode={} ssh_key={} identity={} length={}".format(args.type,args.mode,args.sshkey,args.identity,args.length)]
        if args.double:
            ops.extend(["-e guestip={}".format(args.double)])
        else:
            ops.extend(["-e oneip=True"])
        create.extend(ops)
        print("[+] Creating CloudCat cracking instance with " + args.type + " accelerated computing instance.")
        subprocess.call(create)
	
if __name__ == "__main__":
    banner()
    main()
