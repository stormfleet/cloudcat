# CloudCat
## Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Coming](#coming)
- [Thanks](#thanks)

## Introduction
A Python script to create infrastructure to crack passwords for you in the cloud. Under the hood Cloudcat uses an Ansible-base to automate the creation and deletion of AWS's GPU EC2 instances, which make for great crackstations.

Building and maintaing your own crackstation is fun, but can be seriously expensive, and time consuming. If you're penetration testing or red teaming and you've captured some NTLMv2 hashes or an SPN, sometimes you need results quick.

If you can afford your own beefy crackstation then that's no problem - but if you can't justify purchasing a proper one then AWS is a great alternative. Enhanced computing EC2 instances have really fast GPUs, which are unsurprisingly ideal for cracking hashes. Here are some stats for the 3 EC2 instances supported by CloudCat.


[Here](benchmark.md) is a full benchmark for all Hashcat hashtypes on a p3.2xlarge instance. p3.8x and p3.16xlarge instances use 4 and 8 of the NVIDIA V100 GPUs respectively, so the increase in cracking power is linear.

tl;dr: Don't have the money or can't be bothered to maintain your own crackstation? Have some cash to spare? Want creds quickly? Automate cracking in the cloud and free up time to continue pentesting.

## Installation
Cloudcat requires the following Python dependencies:
```
boto
botocore
boto3
ansible
```
In addition to the following linux packages:
```
awscli
ansible
```
## Usage

```
./cloudcat.py --help

CloudCat - The cloud-based password cracker.
        
usage: cloudcat.py [-h] [-t {p3.2xlarge,p3.8xlarge,p3.16xlarge}] [-f FILE]
                   [-m MODE] [-i IDENTITY] [-k SSHKEY] [-l LENGTH] [-s]
                   [--double DOUBLE] [-d] [--info]

optional arguments:
  -h, --help            show this help message and exit
  -t {p3.2xlarge,p3.8xlarge,p3.16xlarge}, --type {p3.2xlarge,p3.8xlarge,p3.16xlarge}
                        Size of the instance to use. From cheapest to most
                        expensive: p3.2xlarge, p3.8xlarge and p3.16xlarge.
  -f FILE, --file FILE  File containing hashes to crack
  -m MODE, --mode MODE  Hashtype cracking mode you want to use
  -i IDENTITY, --identity IDENTITY
                        AWS identity to use (only select this if you're sure
                        you have the correct key!)
  -k SSHKEY, --ssh-key SSHKEY
                        SSH key-file name. Used to connect to created CloudCat
                        instances to conduct tasks and launch Hashcat.
  -l LENGTH, --length LENGTH
                        Length of the hash cracking run. Short is just
                        rockyou.txt, medium is rockyou and fav_wordlist, and
                        long is those two and crackstation.txt.
  -s, --single          Create an Amazon Security Group where only your
                        current public IP address is allowed through the
                        firewall. You will be unable to SSH to the server from
                        anywhere other than here.
  --double DOUBLE       Create an Amazon Security Group where your current
                        pulic IP address and one other public IP address is
                        allowed through the firewall. This second location
                        should be somewhere you always have access to (e.g.
                        home, office).
  -d, --destroy         Destroy CloudCat AWS P3.X instances.
  --info                Print information on Hashcat cracking statistics and
                        AWS P3 instance costs.

```
Example usage: ./cloudcat.py -t p3.2xlarge -f /tmp/foo.txt -m 1000 -i awscat -k awscat -l short -s

Currently CloudCat creates an instance, creates a volume from a public snapshot containing the following wordlists. This needs to be improved, as the more wordlists included the better.
```
rockyou.txt
fav_wordlist.lst
crackstation.txt
```

## Coming
Things that will be coming to CloudCat eventually:
- Support for multiple simultaneous CloudCat instances
- Terraform support
- Robust hash detection to confirm whether hashes are correctly formatted before the instances are brought up (to save money).
- Better management of active hosts to facilitate destruction
- Dockerfile support
## Thanks
Obviously massive thanks to the [Hashcat team](https://github.com/hashcat/hashcat) for the work they do.
Inspired to create this by the following blog posts on AWS-based password cracking: [1](https://hackernoon.com/20-hours-18-and-11-million-passwords-cracked-c4513f61fdb1),[2](https://medium.com/@lordsaibat/cracking-passwords-with-terraform-and-aws-3685cc918721),[3](https://medium.com/@iraklis/running-hashcat-v4-0-0-in-amazons-aws-new-p3-16xlarge-instance-e8fab4541e9b).
./cloudcat.py -t p3.2xlarge -f /tmp/foo.txt -m 1000 -i awscat -k awscat -l short -s
