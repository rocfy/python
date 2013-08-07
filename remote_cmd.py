#!/usr/bin/python
#coding:utf-8
import paramiko
import sys
import datetime

if len(sys.argv) < 2 :
	print "\033[41mPlease input iplist and cmd,like  'python remote_cmd.py iplist ls'\033[0m"
	sys.exit()
iplist=sys.argv[1]
cmd=sys.argv[2]
now=datetime.datetime.now()
file=open(iplist)

for l in file.readlines():
    	if  len(l)==1 or  l.startswith('#'):
        	continue
#	print l,
	f=l.split()
	#print f
	hostip=f[0]
	username=f[1]
	password=f[2]
	port=f[3]
        print "\033[42m---------------------------------%s---------------------------\033[0m" %hostip
	try:
        	#paramiko.util.log_to_file('ssh.log')
        	s=paramiko.SSHClient()
       	 	s.load_system_host_keys()
        	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       		s.connect(hostname=hostip,port=port,username=username, password=password)
        	stdin,stdout,stderr=s.exec_command(cmd)
		print	 stdout.read()
        	s.close()
	except Exception,ex:
                print "\n",hostip,":\t",ex,"\n"
		ssh_errors=open("ssh_errors.log","a")
		ssh_errors.write("%s\t%s:\t%s\n"%(now,hostip,ex))
		ssh_errors.close()
                pass
file.close()
