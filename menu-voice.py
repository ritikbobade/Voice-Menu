import os
import speech_recognition as sr
os.system("tput setaf 3")
print("                                       Welcome to my menu              ")
os.system("tput setaf 7")
print("											-----------------				")		
r=sr.Recognizer()

with sr.Microphone() as source:
	print("Tell the password")
	passw=r.listen(source)
	print("Checking the password")
	ps=r.recognize_google(passw)
	
	if(("Red" in ps)and("Hat")in ps):
		print("Access Granted")
	else:
		print("Acces Denied")	
		exit()

print("""
	\n
	 1:Big Data Hadoop
	 2:AWS Cloud
	 3:Machine Learning
	 4:Docker
	 5.Python
	""")		
	

with sr.Microphone() as source:
	print('Start speaking I am listening')
	audio=r.listen(source)
	print('Done listening')
ch = r.recognize_google(audio)
if (("Big " in ch )or ("data" in ch))and (("open" in ch)or("execute"in ch)):
	print("""
		 Open hdfs-site.xml file
		 Open core-site.xml file
		 Start namenode
		 Start datanode
		 Run jps 
		""")
	with sr.Microphone() as source:	
		print('what you want me to do')
		voice=r.listen(source)
		print('Done listening')
		bg=r.recognize_google(voice)
		if ("hdfs"in bg)and("open" in bg):
			os.system("cd /etc/hadoop; vi hdfs-site.xml")
		elif ("core" in bg) and ("open" in bg):
			os.system("cd /etc/hadoop; vi core-site.xml")
		elif ("namenode" in bg) and (("open" in bg)or ("start"in bg)):
			os.system("hadoop-daemon.sh start namenode")
		elif ("datanode" in bg)and (("open" in bg)or("start" in bg)):
			os.system("hadoop-daemon.sh start datanode")
		elif ("jps" in bg)and (("start"in bg)or("run")in bg):
			os.system("jps")
		else:	
			os.system("exit()")
elif (("aws" in ch)or ("cloud" in ch))and (("start" in ch)or("open" in ch)):
	print("""
			configure
      		generate key-pair
      		create security group
      		Create subnet id
      		Launch a ec2 instance
      		create a EBS storage
      		create a S3 bucket
      		""")
	with sr.Microphone() as source:
		print("What you want me to do")
		awaz=r.listen(source)
		print("Done listening")
		aw=r.recognize_google(awaz)
		if ("configure" in aw):
			os.system("aws configure; enter access key: ; enter security key:")
		elif(("key"in aw)or("pair"in aw))and(("generate"in aw)or("open" in aw)):
			x=input("Enter the key name")
			os.system("aws ec2 create-key-pair --key-name {}".format(x))
		elif(("security" in aw)or ("group"in aw))and(("create"in aw)or("open")in aw):
			x=input("Entr the name of the security group")
			y=input("Enter the description of the security group")
			os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count 1 --subnet-id {} --security-group-ids {} --key-name hadoopkey".format(x,y))	
		elif(("ebs"in aw)or("storage"in aw)and(("create")in aw)or("open"in aw)):
			x=input("Enter the size(in GB)")
			os.system("aws ec2 create-volume --availability-zone ap-south-1a --size  {}".format(x))
		elif (("ec2"in aw)or("instance"in aw))and(("launch"in aw)or("start"in aw)):
			x=input("Enter the name of the subnet id")
			y=input("Enter the description of the security group")
			os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count 1 --subnet-id {} --security-group-ids {} --key-name hadoopkey".format(x,y))
		elif(("s3"in aw)or("bucket"in aw))and (("create"in aw)or("open"in aw)):
			os.system("aws s3 help")
elif(("machine"in ch)or("learning"in ch))and(("open"in ch)or("start"in ch)):
	print("""
		 Launch jupyter notebook
		 Install numpy
		 Install pandas
		""")
	with sr.Microphone() as source:
		print("What you want to do")
		audion=r.listen(source)
		print("Done listening")
		ml=r.recognize_google(audion)
		if (("jupyter"in ml)or("notebook "in ml))and(("open"in ml)or("launch")in ml):
			os.system("jupyter notebook --allow-root")
		elif("numpy"in ml)and("install"in ml):
			os.system("pip3 install numpy")
		elif("pandas"in ml)and("install"in ml):
			os.system("pip3 install pandas")
elif("docker"in ch)and(("open"in ch)or("start"in ch)):
	print("""
		See running docker containers
		Run Ubuntu:18.10
		Run ubuntu:14.04
		Run ubuntu:20.10
		Exit		
		""")			
	with sr.Microphone() as source:
		print("What do you want me to do")
		audio1=r.listen(source)
		print("Done listening")			
		dc=r.recognize_google(audio1)
		if(("Ubuntu"in dc)or("18"in dc)or("start"in dc)or("launch"in dc)):
			os.system("docker run -it ubuntu:18.10")
		elif(("Ubuntu"in dc)or("14"in dc)or("start"in dc)or("launch"in dc)):
			os.system("docker run -it ubuntu:14.04")
		elif(("Ubuntu"in dc)or("20"in dc)or("start"in dc)or("launch"in dc)):
			os.system("docker run -it ubuntu:20.10")
		elif(("docker"in dc)or("container"in dc)and(("open"in dc)or("open"in dc))):
			os.system("docker ps")
elif(("python"in ch)and("open"in ch)or("start")in ch):
	print("""
		Check python version
		Run python interpreter
		Exit
		""")
	with sr.Microphone() as source:
		print("What you want me to do")
		audio2=r.listen(source)
		print("Done listening")
		py=r.recognize_google(audio2)
		if(("python" in py)or("version"in py))and(("check"in py)or("open"in py)):
			os.system("python3 --version")
		elif(("python"in py)and("start"in py)or("run"in py)):
			os.system("python3")

else:
	print("Unable to recognize what you said")
