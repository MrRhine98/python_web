import re

# re.search
# re.search(r"^", xxx) => re.match
ret = re.search(r"\d+", "Thumbs up:9999, Thumbs down:100")
ret.group()	# '9999' 100 cannot be matched


# re.findall
ret = re.search(r"\d+", "Thumbs up:9999, Thumbs down:100")
print(ret)	# [9999, 100]


# re.sub(re, sub, data*)
re.sub(r"\d+", "998", "python = 997")
# python = 998
# sub could be a function

# re.split
ret = re.split(r":| ", "info:xiaozhang 30 shandong")
print(ret)
# [info, "xiaozhang", "30", "shandong"]
