import re

# capital stands for the opposite
# \d stands for one digit 0 to 9
ret = re.match(r"MrRhine\d", "MrRhine1")

# . stands for any character but one digit (except \n)
ret = re.match(r"MrRhine.", "MrRhine1")

# also one digit 
ret = re.match(r"MrRhine[12345]", "MrRhine1")
ret = re.match(r"MrRhine[1-5]", "MrRhine1")

ret = re.match(r"MrRhine[1235678]", "MrRhine1")
ret = re.match(r"MrRhine[1-35-8]", "MrRhine1")

ret = re.match(r"MrRhine[1-5abcde]", "MrRhine1")

ret = re.match(r"MrRhine[1-5a-eA-Z]", "MrRhine1")
	
# \w stands for a word 0-9 a-z A-z and underscore_
ret = re.match(r"MrRhine\w", "MrRhine1")
ret = re.match(r"MrRhine[0-9a-zA-Z_]", "MrRhine1")

# \s stands for a space or a tab
ret = re.match(r"MrRhine\s\d", "MrRhine\t1")

# one two and three digits are all valid
ret = re.match(r"MrRhine\d{1,3}", "MrRhine172")

# strictly restrained 11 digits
ret = re.match(r"\d{11}", "11120121510")

ret = re.match(r"021-/d{8}", "021-12345678")
# ? means the previous character is optional
ret = re.match(r"021-?/d{8}", "021-12345678")
# * means the previous character could appear for many times or 
ret = re.match(r"021-*/d{8}", "021-12345678")


string = """dsafasdf
dsafdsaf
dsaf
sdfasdf
asdfasadf
"""
# re.S make . include \n
ret = re.match(r".*", string, re.S)

# + means the previous character could appear for one or many time. must exists
ret = re.match(r".+", string)

# ^ starts $ ends
ret = re.match(r"^\d{11}$", "11120121510")

ret = re.match(r"[a-zA-Z0-9_]{4-20}@(163|126)\.com", "laowang@163.com")
ret.group(1)	# return the first data in ()

# tags at two ends need to be the same
html_str = "<h1>MrRhine17777</h1>"
ret = re.match(r"<(\w*)>.*</\1>", html_str)
