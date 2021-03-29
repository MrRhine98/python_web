import urllib.request

def downloader(save_name, img_url):
	req = urllib.request.urlopen(img_url)
	img_content = req.read()

	with open(save_name, "wb") as f:
		f.write(img_content)

def main():
	url1 = ""	# image url
	url2 = ""
	gevent.joinall([
		gevent.spawn(downloader, "1.jpg", url1),
		gevent.spawn(downloader, "2.jpg", url2)
	])

if __name__ == "__main__":
	main()

