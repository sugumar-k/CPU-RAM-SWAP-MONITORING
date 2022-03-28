#importing the module 
import logging 
import os

#now we will Create and configure logger 
logging.basicConfig(filename="logpattern.log",
                    level=logging.DEBUG, 
					format='%(name)s|%(levelname)s |%(message)s|%(asctime)s',
					filemode='w',datefmt="%d-%m-%y %H-%M-%S") 

import psutil
threshold=90.0

#cpu monitoring
logging.debug("debugging cpu information")
try:
	cpu_times= (psutil.cpu_times())
	logging.info (f'cpu time is : {cpu_times}%')
	cpu_percent= (psutil.cpu_percent())
	logging.info("cpu percent:%d",cpu_percent)
	cpu_count=(psutil.cpu_count())
	logging.info("cpu_count:%d",cpu_count)
except:
	logging.error("error occured")


#ram usage monitoring
logging .debug("debugging ram memory")
try:
	ram_usage=psutil.virtual_memory()
	logging.info(f'ram usage:{ram_usage}%')
	if ram_usage.percent >=threshold:
		logging.warning("ram space is  low %d:",ram_usage.percent)
	else:
		logging.warning("ram used space in percentage  is %d:",ram_usage.percent)
except:
	logging.error("error occured")

#swap monitoring
logging.debug("debugging swap memory")
try:
	swap__memory=psutil.swap_memory()
	logging.info(f'swap memory is  {swap__memory}%')
	if swap__memory.percent>=threshold:
		logging.warning('swap memory is low :%d',swap__memory.percent)
	else:
		logging.warning("swap memory is:%d",swap__memory.percent)
except:
	logging.error("error occured")


#COUNTING THE OCCURENCE
import os
#reading the file
file=open("logpattern.log","r")
data=file.read()

#counting the occurence
def occurence(a,b):
    occurence_a=data.count(a)
    print("no of occurenceof" ,a,occurence_a)
    occurence_b=data.count(b)
    print("no of occurenceof ",b,occurence_b)
occurence("ERROR","WARNING")

#printing the required log level

file=open("logpattern.log","r")
levelname="INFO"
for line in file:
	if levelname in line:
		print(line)






