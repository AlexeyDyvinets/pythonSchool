import re


def file_opener(file):
    log = open(file)
    text = log.read()
    logs_finder(text)


def logs_finder(text):
    logs_reader = re.findall(r'eid:(.*)', text)
    log1 = logs_reader[-1].replace(';', '\n').split()
    log2 = logs_reader[-2].replace(';', '\n').split()
    print(f'Предпоследние eid:{log2}\nПоследние eid:{log1}')





file_opener('hw.log')
