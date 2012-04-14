
text = """
[assembly: sdfgdfgdfg("3.9.0.1")]
[assembly: AssemblyVersion("3.9.0.1")]
[assembly: AssemblyFileVersion("3.9.0.1")]
[assembly: AssemblyCopyright("Copyright 2011-2012")]
"""


import re


def method1():
    pattern = "\[assembly: AssemblyFileVersion\(\"(\d\.\d\.\d\.\d)\"\)\]"
        #\[assembly: AssemblyFileVersion
    matches = re.finditer(pattern, text)

    for match in matchesх\
    :
        print match.group(1)

def method2():
    pattern = "(?<=\[assembly: AssemblyFileVersion\(\")(\d\.\d\.\d\.\d)(?=\"\)\])"
    #\[assembly: AssemblyFileVersion
    matches = re.finditer(pattern, text)

    for match in matches:
        print match.group(0)

def method3():
    prefix_pattern = r"\[assembly: \w+\(\""
    pattern = "(?<=(\[assembly: \w+\(\"))((\d\.)+\d)(?=\"\)\])"
    #\[assembly: AssemblyFileVersion
    matches = re.finditer(pattern, text)

    for match in matches:
        print match.group(0)

method3()