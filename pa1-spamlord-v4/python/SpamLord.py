import sys
import os
import re
import pprint

expr_phone = (r"(?:\)|-| |&thinsp;)?[467](?:\)|-| |&thinsp;)?"
              r"[015]((?:\)|-| |&thinsp;){0,2}\d){8}\b(?! ?\d)")

def get_email1(line):
    value = line
    if "Server at " in line:
        return ""
    value = re.sub(r"@| @ |\(at\)| at |&#x40;", lambda s: "@", value)
    return value

def get_email2(line):
    value = line
    value = re.sub(r" at ", lambda s: "@", value)
    value = re.sub(r" dot | dt |;", lambda s: ".", value)
    return value

def get_email3(line):
    #'teresa.lynn (followed by "@stanford.edu"'
    value = line
    value = re.sub(r' \(followed by ("|&ldquo;)@', lambda s: "@", value)
    value = re.sub("\"'", lambda s: "", value)
    return value

def get_email4(line):
    value = line
    if "Server at " in line:
        return ""
    value = re.sub(r" at ", lambda s: "@", value)
    value = re.sub(r" ", lambda s: ".", value)
    return value

def get_email5(line):
    value = line

    part1 = re.search(r"(?<=',')[\.\w]+", value).group();
    part2 = re.search(r"[\.\w]+(?=',')", value).group();

    value = part1+"@"+part2

    return value


def get_email6(line):
    value = line
    #engler WHERE stanford DOM edu
    value = re.sub(r" WHERE ", lambda s: "@", value)
    value = re.sub(r" DOM ", lambda s: ".", value)
    return value


def get_email7(line):
    value = line
    # email: pal at cs stanford edu, but
    value = re.sub(r" at ", lambda s: "@", value)
    value = re.sub(r" ", lambda s: ".", value)
    return value

def get_email8(line):
    value = line
    # d-l-w-h-@-s-t-a-n-f-o-r-d-.-e-d-u
    value = re.sub(r"-", lambda s: "", value)
    return value

email_patterns = {
    r"\b(?:\w|\.)+(?:@| @ |\(at\)| at |&#x40;)(?:\w|\.)+(?:\.)[a-zA-Z]{2,4}\b": get_email1,
    r"\b(?:\w| dot | dt |;)+(?: at )(?:\w| dot | dt |;)+(?: dot | dt |;)[a-zA-Z]{2,4}\b": get_email2,
    r'\b(?:\w|\.)+ \(followed by ("|\&ldquo;)@(?:\w|\.)+(?:\.)[a-zA-Z]{2,4}(?=("|\&rdquo;))': get_email3,
    r"\b(?:\w|\.)+ at (?:\w|\.)+ edu\b": get_email4,
    r"(?<=\(')[\'\.\w\,]+(?='\); </script>)": get_email5,
    r"\w+ WHERE \w+ DOM \w{2,4}\b": get_email6,
    r"(?<=email: )[ \w]+ edu": get_email7,
    r"[-\w]+@[-\w]+\.-e-d-u": get_email8
}

def get_phone_substrings(text):
    subs = []
    pattern = re.compile(expr_phone)
    subsi = pattern.finditer(text)
    for i in subsi:
        subs.append(i.group())
    return subs

def restore_phone(substring):
    value = re.sub("[^0-9]", lambda s: "", substring)
    result = value[-10:-7] + "-" + value[-7:-4] + "-" + value[-4:]#value[-10:-8] + "-" + value[-7:-5] + "-" + value[-4:]
    return result

def find_phones(text):
    phones = []

    substrings = get_phone_substrings(text)

    for substring in substrings:
        phone = restore_phone(substring)
        phones.append(phone)

    return phones

def find_emails(text):
    emails = []
    for expr in email_patterns:
        substrings_match = re.finditer(expr, text)
        for substring_match in substrings_match:
            email = email_patterns[expr](substring_match.group())
            if len(email)>0:
                emails.append(email)

    return emails

"""
TODO
This function takes in a filename along with the file object (actually
a StringIO object at submission time) and
scans its contents against regex patterns. It returns a list of
(filename, type, value) tuples where type is either an 'e' or a 'p'
for e-mail or phone, and value is the formatted phone number or e-mail.
The canonical formats are:
     (name, 'p', '###-###-#####')
     (name, 'e', 'someone@something')
If the numbers you submit are formatted differently they will not
match the gold answers

NOTE: ***don't change this interface***, as it will be called directly by
the submit script

NOTE: You shouldn't need to worry about this, but just so you know, the
'f' parameter below will be of type StringIO at submission time. So, make
sure you check the StringIO interface if you do anything really tricky,
though StringIO should support most everything.
"""
def process_file(name, f):
    # note that debug info should be printed to stderr
    # sys.stderr.write('[process_file]\tprocessing file: %s\n' % (path))
    res = []
    for line in f:
        emails = find_emails(line)
        phones = find_phones(line)
        for email in emails:
            res.append((name,'e',email))
        for phone in phones:
            res.append((name,'p',phone))
    return res

"""
You should not need to edit this function, nor should you alter
its interface as it will be called directly by the submit script
"""
def process_dir(data_path):
    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path,fname)
        f = open(path,'r')
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)
    return guess_list

"""
You should not need to edit this function.
Given a path to a tsv file of gold e-mails and phone numbers
this function returns a list of tuples of the canonical form:
(filename, type, value)
"""
def get_gold(gold_path):
    # get gold answers
    gold_list = []
    f_gold = open(gold_path,'r')
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list

"""
You should not need to edit this function.
Given a list of guessed contacts and gold contacts, this function
computes the intersection and set differences, to compute the true
positives, false positives and false negatives.  Importantly, it
converts all of the values to lower case before comparing
"""
def score(guess_list, gold_list):
    guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    #print 'Guesses (%d): ' % len(guess_set)
    #pp.pprint(guess_set)
    #print 'Gold (%d): ' % len(gold_set)
    #pp.pprint(gold_set)
    print 'True Positives (%d): ' % len(tp)
    pp.pprint(tp)
    print 'False Positives (%d): ' % len(fp)
    pp.pprint(fp)
    print 'False Negatives (%d): ' % len(fn)
    pp.pprint(fn)
    print 'Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn))

"""
You should not need to edit this function.
It takes in the string path to the data directory and the
gold file
"""
def main(data_path, gold_path):
    guess_list = process_dir(data_path)
    gold_list =  get_gold(gold_path)
    score(guess_list, gold_list)

"""
commandline interface takes a directory name and gold file.
It then processes each file within that directory and extracts any
matching e-mails or phone numbers and compares them to the gold file
"""
if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print 'usage:\tSpamLord.py <data_dir> <gold_file>'
        sys.exit(0)
    main(sys.argv[1],sys.argv[2])
