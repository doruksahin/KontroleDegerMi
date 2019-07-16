from tkinter import *
import sys
import json
import csv
import os


input_file = "{}".format(sys.argv[1])
output_file = "{}_output.json".format(input_file.split(".")[0])

tagged_list = []
mark_list = []


def mark_as_positive():
	global mark_list
	mark_list.append(1)
	claim_text.delete('1.0', 'end-1c')
	claim_text.insert(END, tagged_list[len(mark_list)])


def mark_as_negative():
	global mark_list
	mark_list.append(0)
	claim_text.delete('1.0', 'end-1c')
	claim_text.insert(END, tagged_list[len(mark_list)])


def save_and_quit():
	json_data = []
	for i in range(len(mark_list)):
		block = {}
		block['tweet'] = tagged_list[i]
		block['is_checkworthy'] = mark_list[i]
		json_data.append(block)

	with open(output_file, 'w') as outfile:
		json.dump(json_data, outfile, indent=4)
	root.destroy()
	'''
	with open(output_file, mode='w') as csv_file:
		writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for i in range(len(mark_list)):
			row = [tagged_list[i]] + [mark_list[i]] 
			writer.writerow(row)
	'''



def readfile():
	global tagged_list
	global mark_list

	f = open(input_file, 'r')
	json_file = json.load(f)
	tagged_list = []

	for tweet in json_file:
		char_list = [j for j in tweet if ord(j) in range(65536)]
		new_str=''
		for j in char_list:
			new_str = new_str + j
		tagged_list.append(new_str)
		


	mark_list = []
	try:
		f = open(output_file, 'r')
		json_file = json.load(f)
		for block in json_file:
			mark_list.append(block['is_checkworthy'])
	except:
		try:
			os.mknod(output_file)
		except:
			pass



if __name__ == '__main__':
	root = Tk()
	readfile()



	mark_frame = Frame(root)
	mark_frame.pack(side=TOP) 
	claim_text = Text(mark_frame, height=10, width=50, font=("Helvetica", 25))
	claim_text.pack(side=TOP)
	claim_text.insert(END, tagged_list[len(mark_list)])

	btn_frame = Frame(mark_frame)
	btn_frame.pack(side=TOP)
	save_btn_frame = Frame(root)
	save_btn_frame.pack(side=TOP)
	checkworthy_btn = Button(btn_frame, text="Checkworthy", command=mark_as_positive)
	checkworthy_btn.pack(side=LEFT)
	non_checkworthy_btn = Button(btn_frame, text="Non-Checkworthy", command=mark_as_negative)
	non_checkworthy_btn.pack(side=RIGHT)
	save_btn = Button(save_btn_frame, text="Save", command=save_and_quit)
	save_btn.pack(side=BOTTOM)




root.mainloop()