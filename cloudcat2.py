#!/usr/bin/python3

import ansible_runner
import os

cwd = os.getcwd()
ansible_runner.run(playbook=cwd + '/test-yaml.yml', cmdline='--vault-id @prompt', extravars={'foo':'one','bar':'two','baz':'three'})
