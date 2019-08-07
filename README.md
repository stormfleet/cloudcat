# CloudCat
## Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Thanks](#thanks)

## Introduction
A Python script to create infrastructure to crack passwords for you in the cloud. Under the hood Cloudcat uses an Ansible-base to automate the creation and deletion of AWS's GPU EC2 instances, which make for great crackstations.

Building and maintaing your own crackstation is fun, but can be seriously expensive, and time consuming. If you're penetration testing or red teaming and you've captured some NTLMv2 hashes or an SPN, sometimes you need results quick.

If you can afford your own beefy crackstation then that's no problem - but if you can't justify purchasing a proper one then AWS is a great alternative. Enhanced computing EC2 instances have really fast GPUs, which are unsurprisingly ideal for cracking hashes. Here are some stats for the 3 EC2 instances supported by CloudCat.
*table here*

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
It's still a work in progress, so this is coming!

I'm not sure at the moment if the best thing to do is to create a volume, load it with wordlists, then store it on AWS, or to create the wordlist volume each time the script is run.
The benefit of the former is the setup time is much faster, however it costs money when cracking instances are not run. Inverse is true of the latter; it's slower to start up but costs no money when not in use.
## Thanks
Obviously massive thanks to the [Hashcat team](https://github.com/hashcat/hashcat) for the work they do.
Inspired to create this by the following blog posts on AWS-based password cracking: [1](https://hackernoon.com/20-hours-18-and-11-million-passwords-cracked-c4513f61fdb1),[2](https://medium.com/@lordsaibat/cracking-passwords-with-terraform-and-aws-3685cc918721),[3](https://medium.com/@iraklis/running-hashcat-v4-0-0-in-amazons-aws-new-p3-16xlarge-instance-e8fab4541e9b).
