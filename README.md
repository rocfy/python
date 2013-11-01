remote_cmd
==========

              -h,-H,--help         帮助页面 
              -C, --cmd            执行命令模式 
              -M, --command        执行命令模式 
              -S, --sendfile       传输文件模式 
              -L, --localpath      本地文件路径 
              -R, --remotepath     远程服务器路径 

	     IP列表格式:

   	     IP地址		用户名     密码     端口
	     192.168.1.1        root	  123456    22

      	e.g.
              批量执行命令格式： -C "IP列表" -M '执行的命令'
              批量传送文件：     -S "IP列表" -L "本地文件路径" -R "远程文件路径"
	      错误日志文件：$PWD/ssh_errors.log

