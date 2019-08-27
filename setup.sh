#!/bin/bash
echo "[+] Performing CloudCat setup."
echo "[+] Installing required packages..."
sudo apt install ansible
pip install botocore boto3 ansible --user
echo "[+] Creating external_vars.yml file"
ansible-vault create external_vars.yml
