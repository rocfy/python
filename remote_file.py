#!/usr/bin/python
import paramiko 
import sys
import datetime


if len(sys.argv) < 2 :
	print '\033[41mPlease input iplist and command,like  "python remote_cmd.py iplist upload_filename"\033[0m'
	sys.exit()

iplist=sys.argv[1]
local_dir=sys.argv[2]
remote_dir='/tmp/'+local_dir
now=datetime.datetime.now()

file=open(iplist,'r')

if __name__  ==  "__main__" :
	for l in file.readlines():
		if  len(l)== 1 or  l.startswith('#'):
			continue
       		f=l.split()
		hostip=(f[0])
      		username=(f[1])
     		password=(f[2])
		port=int(f[3])
#		print type(port)
#		paramiko.util.log_to_file('sftp.log')
		try:
			t=paramiko.Transport((hostip,port))
			t.connect(username=username,password=password) 
			sftp=paramiko.SFTPClient.from_transport(t) 
			sftp.put(local_dir,remote_dir)
			print "Upload file \033[31m%s\033[0m to \033[32m%s\033[0m:\033[33m%s\033[0m : %s" %(local_dir,hostip,remote_dir,now)
			sftp.close()
			t.close()
	        except Exception,ex:
               		print "\n",hostip,":\t",ex,"\n"
                	ssh_errors=open("ssh_errors.log","a")
                	ssh_errors.write("%s\t%s:\t%s\n"%(now,hostip,ex))
                	ssh_errors.close()
                	pass

file.close()
