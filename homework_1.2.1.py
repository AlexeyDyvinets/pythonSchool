import re


def file_opener(file):
    log = open(file)
    text = log.read()
    logs_finder(text)


def logs_finder(text):
    logs_reader = re.findall(r'eid:(.*)', text)
    log1 = logs_reader[-1].replace(';', '\n').split()
    log2 = logs_reader[-2].replace(';', '\n').split()
    # print(f'Предпоследние eid:{log2}\nПоследние eid:{log1}')
    logs_handler(log1,log2)


def logs_handler(log1, log2):
    log1 = ''.join(log1)
    log2 = ''.join(log2)
    log1_names = re.findall(r'[^.0-9]\w*[^.0-9]', log1)
    log2_names = re.findall(r'[^.0-9]\w*[^.0-9]', log2)
    log1_val = re.findall(r'\d+', log1)
    log2_val = re.findall(r'\d+', log2)

    log1 = dict(zip(log1_names, log1_val))
    log2 = dict(zip(log2_names, log2_val))

    print(log1, log2, sep='\n')


file_opener('hw.log')
