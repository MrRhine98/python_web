import os
import multiprocessing

def copy_file(q, file_name, target_folder, des_folder):
	dir_source = os.path.join(target_folder, file_name)
	f_source = open(dir_source, "rb")
	content = f_source.read()
	f_source.close()

	dir_des = os.path.join(des_folder, file_name)
	new_f = open(dir_des, "wb")
	new_f.write(content)
	new_f.close()
	# send a message when compelete
	q.put(file_name)


def main():
	# acquire name of the required file folder
	target_folder = input("The folder you want to copy:")

	# create a new folder
	try:
		des_folder = target_folder + "-backup"
		os.mkdir(des_folder)
	except:
		pass

	# acquire names of all the files
	file_names = os.listdir(target_folder)
	print(file_names)

	# create a process pool
	po = multiprocessing.Pool(5)

	# create a queue
	q = multiprocessing.Manager().Queue()

	print(f"{target_folder} ---> {des_folder}")
	for file_name in file_names:
		po.apply_async(copy_file, args=(q, file_name, target_folder, des_folder))
	po.close()
	# po.join()
	# copy files to the new folder 
	num_files = len(file_names)
	i = 0
	while True:
		file_n = q.get()
		i += 1 
		print("\rcompelete %.2f %%" % (i*100 / num_files), end='')

		if i >= num_files:
			break
	print()


if __name__ == "__main__":
	main()