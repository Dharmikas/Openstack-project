Before running the programs:

1. Openstack and swift must be installed.

2. Run 'source openrc admin admin' command in the devstack folder.

3. Python's swiftclient library must be installed.

4. Run command 'swift stat -v' in the terminal and note down the token, storageURL(public accessible URL) and account.

5. Then run commands like-  'export storageURL="---storageURL you have noted down----"'
			    'export token="---token you have noted down----"'
			    'export Account="---account you have noted down----"'

6. Also edit the same things in the professorcode.py