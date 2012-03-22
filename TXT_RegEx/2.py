text = r"""
adsfasdf adsfasdfasdfsadf
[3/21/12 6:52:38 PM] denshik.ruslan: jurafsky@stanford.edurr jurafs-ky@cs.stanford.eZu urF.fsky@csli.stanford.e5ur
j3_fsky@stanford.u jurafsky@cs.stanfo_rd.edu urafsky@csli.stanford.e3u\r\n
 jurafsky(at)cs.stanford.edu    <script type="text/javascript">obfuscate('stanford.edu','jurafsky')</Script>
jurafsky at csli dot stanford dot edu
"""

text = r"""('stanford.edu','jurafsky')   w  e       wqe"""
import re

#pattern = re.compile(r"[\w|-|\.]+(?:@|\(at\))[\w+\.]+\.[a-zA-Z0-9]{2,4}\b")
#pattern = re.compile(r"(?<=<script\s+)['\w\(\),\.]+") #(?=</Script>)
pattern = re.compile(r"\s*")

result = pattern.findall(text)

print result

#result = re.sub(r"[\w|-|\.]+@[\w+\.]+\.[a-zA-Z0-9]{2,4}\b", lambda st: "++", text)
#print result
