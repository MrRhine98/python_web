import os
import multiprocessing

def copy_file(file_name, target_folder, des_folder):
	print(f"copying {file_name}")
	dir_source = os.path.join(target_folder, file_name)
	f_source = open(dir_source, "rb")
	content = f_source.read()
	f_source.close()

	dir_des = os.path.join(des_folder, file_name)
	new_f = open(dir_des, "wb")
	new_f.write(content)
	new_f.close()


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
	print(f"{target_folder} ---> {des_folder}")
	for file_name in file_names:
		po.apply_async(copy_file, args=(file_name, target_folder, des_folder))
	po.close()
	po.join()
	# copy files to the new folder 


if __name__ == "__main__":
	main()