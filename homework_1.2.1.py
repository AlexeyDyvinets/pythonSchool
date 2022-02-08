import re


def file_opener(file):
    log = open(file)
    text = log.read()
    logs_finder(text)


def logs_finder(text):
    logs_reader = re.findall(r'eid:(.*)', text)
    log1 = logs_reader[-1]
    log2 = logs_reader[-2]
    print(log1, log2, sep='\n')


file_opener('hw.log')
