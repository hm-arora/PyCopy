import os
import shutil
import sys
import subprocess

def show_message(title):
	subprocess.Popen(['notify-send',title])

show_message("starts......")
path = sys.argv[0][::-1].partition('/')[2][::-1]+'/'
try:
	files = sys.argv[1:][0].strip().split("  ")
	folder_dic = {}
	files_dic = {}
	def extract_folder_name():
		global folder_dic
		f = open(path + 'folder.txt','r')
		s = f.read().split("\n")
		for i in s:
			split_text = i.partition("=")
			name = split_text[0].strip()
			ext = split_text[2].strip().replace("'",'')
			folder_dic[name] = ext
	def extract_file():
		global files_dic
		f = open(path+'exten.txt','r')
		s = f.read().split("\n")
		temp_dic = {}
		for i in s:
			split_text = i.partition("=")
			name = split_text[0].strip()
			ext = split_text[2].strip().replace("'",'').split(',')
			temp_dic[name] = ext
		for i,j in temp_dic.iteritems():
			files_dic[i] = []
			for k in j:
				for z in files:
					if k in z:
						files_dic[i].append(z)

	extract_folder_name()
	extract_file()
	ass = ""
	for i,j in files_dic.iteritems():
		if len(j) == 0:
			continue
		if os.path.exists(folder_dic[i]) == False:
			os.mkdir(folder_dic[i])
		for file in j:
			ass = ass + file
			try:
				shutil.copy(file,folder_dic[i])
			except:
				show_message('error')
	show_message("copy successfully :)")

except:
	show_message("error occurred :( ")