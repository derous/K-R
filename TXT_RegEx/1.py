import re
delim_re = re.compile(r"[:,;]")
text = "This,is;example"
print delim_re.split(text)



