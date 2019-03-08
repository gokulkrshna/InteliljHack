#!/usr/bin/python3.5
import os
import sys
import logging
import shutil
from datetime import datetime
from pathlib import Path
import re
base_path = str(Path.home())
LOG_FILENAME = base_path+'/intellij_file_delete.log'
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename=LOG_FILENAME,level=logging.INFO)
os.chdir(base_path)
files = os.listdir(base_path)
intelli_pat = re.compile("\.IntelliJIdea[0-9]{4}\.[0-9]*")
dir_needed = list(filter(intelli_pat.match,files))
if len(dir_needed) != 1:
	logging.info("Found 0 or multiple directories with pattern")
	dir_needed.sort(key=lambda x : int(''.join(re.findall(r'\d+',x))))
	[shutil.rmtree(x) for x in dir_needed[:-1]]
	del dir_needed[:-1]
if os.path.isdir(dir_needed[0]) :
	diff_time = datetime.fromtimestamp(os.path.getmtime(dir_needed[0])).date() - datetime.now().date()
	if diff_time.days <= -15:
		shutil.rmtree(dir_needed[0])
		logging.info(dir_needed[0]+" deleted")
	else :
		logging.info("Days Remaining:%d ",abs(diff_time.days + 15))
else :
	logging.info("Directory could be not found:%s ", dir_needed[0])
