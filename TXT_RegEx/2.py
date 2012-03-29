text = r"""
hager at cs dot jhu dot edu
ada&#x40;graphics.stanford.edu
melissa&#x40;graphics.stanford.edu
serafim at cs dot stanford dot edu<
subh at stanford dot edu<
uma at cs dot stanford dot edu
vladlen at stanford dot edu

ashishg @ stanford.edu
rozm @ stanford.edu
<TT>ullman @ cs.stanford.edu</TT>

support at gradiance dt com
('stanford.edu','jurafsky'); </script>

??????
d-l-w-h-@-s-t-a-n-f-o-r-d-.-e-d-u
jks at robotics;stanford;edu
lam at cs.stanford.edu
ouster (followed by &ldquo;@cs.stanford.edu&rdquo;)
teresa.lynn (followed by "@stanford.edu")
pal at cs stanford edu
mailto:vladlen%20at%20stanford%20dot%20edu

:-1342176593 1775729915 48 0 524447 0 ids:1619043898 id:1942570626; panose-1:2 3 6 0 0 1 1 1 1 1;
mso-list-id:1018121023
ids:-695830552 -190277794 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
http://www.amazon.com/exec/obidos/ASIN/1575860368/
http://www.amazon.com/exec/obidos/ASIN/0262140926/qid=1116182714/
www.amazon.com/TinyOS-Programming-Philip-Levis/dp/0521896061/
www.awlonline.com/product/0,2627,0201441241,00.html
www.cambridge.org/us/catalogue/catalogue.asp?isbn=0521872820"
"http://www.springer.com/978-3-540-74112-1"
('ullman', 'p', '650-494-8016')'617-253-1221')'410-516-5521'), ('kosecka', 'p', '703-993-1876'),
(650) 723-4539
(650) 723-4539
"""

#text = r"""'stanford.edu','jurafsky'"""
import re


#PHONE ====>>>>>
#pattern = re.compile(r"(?:\+\d|\(\+\d)?((?:\)|-|:| |&thinsp;){0,3}\d){10}\b")
pattern = re.compile(r"(?:\)|-| |&thinsp;)?[467](?:\)|-| |&thinsp;)?[015]((?:\)|-| |&thinsp;){0,2}\d){8}\b(?! ?\d)")

#e-mail ====>>>>>
#pattern = re.compile(r"\b(?:\w|\.)+(?:@| @ |\(at\)|&#x40;|%)(?:\w|\.)+(?:\.)[a-zA-Z]{2,4}\b|\b(?:\w| dot )+(?: at )(?:\w| dot | dt )+(?: dot | dt )[a-zA-Z]{2,4}\b|(?<=\()[\'\.\w\,]+(?=\)(; )?</script>)")
#pattern = re.compile(r"\b(?:\w|\-|\.| dot )+(?:@|\(at\)| at )(?:\w|\.| dot )+(?:\.| dot )[a-zA-Z]{2,4}\b|(?<=\()[\'\.\w\,]+(?=\)</script>)")

#pattern = re.compile(r"(\b(?:\w|\.)+(?:@|\(at\))(?:\w|\.)+(?:\.)[a-zA-Z]{2,4}\b)")
#pattern = re.compile(r"\b(?:\w|\.)+(?:@|\(at\))(?:\w|\.)+(?:\.)[a-zA-Z]{2,4}\b|\b(?:\w| dot )+(?: at )(?:\w| dot )+(?: dot )[a-zA-Z]{2,4}\b|(?<=\()[\'\.\w\,]+(?=\)</script>)")

#pattern = re.compile(r"\b[\w\-\.]+(?:@|\(at\))[\w\.]+\.[a-zA-Z]{2,4}\b")
#pattern = re.compile(r"\b(?:\w+| dot ) at (?:\w+| dot )+? dot [a-zA-Z]{2,4}\b")
#pattern = re.compile(r"(?<=\()[\'\.\w\,]+(?=\)</script>)")
result = pattern.finditer(text)

for m in result:
    print m.group()

# print result

#result = re.sub(r"[\w|-|\.]+@[\w+\.]+\.[a-zA-Z0-9]{2,4}\b", lambda st: "++", text)
#print result
#
#obj = re.search(r"((?:-| )?\d){4}", text)
#print obj.group(1)