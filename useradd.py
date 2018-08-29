#! /usr/bin/env python
# Add User Script
# By @Pink_P4nther <pinkp4nther@protonmail.com> :D
import argparse
import os
import sys

banner = """
<[ Add users to machine script ]>
By @Pink_P4nther <pinkp4nther@protonmail.com>
"""
print(banner)

parser = argparse.ArgumentParser()
parser.add_argument("USER",help="The username of the new user")
parser.add_argument("--keyname","-kn",help="The name of the RSA key")
parser.add_argument("--keypass","-kp",help="Password for RSA key")
args = parser.parse_args()

if args.USER:
	user = args.USER
	print("[*] Username: {}".format(user))

if args.keyname:
	keyname = args.keyname
	print("[*] KeyName: {}".format(keyname))
else:
	keyname = ""
	print("[!] You will need to enter the key name manually!")

if args.keypass:
	keypass = args.keypass
	print("[*] RSA key will be encrypted with password: {}".format(keypass))
	while True:
		kpchoice = input("[?] Are you sure? [y/n]: ")
		if kpchoice == "y":
			print("[*] Continuing!")
			break
		elif kpchoice == "n":
			sys.exit("[*] Exiting!")
		else:
			pass

else:
	keypass = ""
	print("[*] RSA key will not be encrypted!")

os.system("useradd -m -s /bin/bash {}".format(user))
print("[*] Added user: {}".format(user))
os.system("mkdir /home/{}/.ssh".format(user))
print("[*] Created '.ssh' directory for user: {}".format(user))
os.system("ssh-keygen -f /home/{}/.ssh/{} -P \"{}\"".format(user,keyname,keypass))
os.system("mv /home/{}/.ssh/{}.pub /home/{}/.ssh/authorized_keys".format(user,keyname,user))
print("[*] OpenSSH RSA key [{}] generated for user: {}".format(keyname,user))
os.system("chmod 700 /home/{}/.ssh".format(user))
os.system("chmod 600 /home/{}/.ssh/authorized_keys".format(user))
os.system("chown {}:{} /home/{}/.ssh".format(user,user,user))
os.system("chown {}:{} /home/{}/.ssh/{}".format(user,user,user,keyname))
os.system("chown {}:{} /home/{}/.ssh/authorized_keys".format(user,user,user))
print("[*] Correct permissions set for key: {} for user: {}".format(keyname,user))
print("[***] Done! :D")

