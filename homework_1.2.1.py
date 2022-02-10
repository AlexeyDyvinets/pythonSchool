def file_opener(file):
    log = open(file)
    s_text = log.readlines()
    return s_text


def logs_finder(s_text, pattern):
    logs = [x for x in text[::-1] if pattern in x][:2]
    return logs

def logs_handler(logs):
    log1 = logs[0].strip()
    s1 = log1[log1.find('eid: ') + len('eid: '):].split(';')
    log2 = logs[1].strip()
    s2 = log2[log2.find('eid: ') + len('eid: '):].split(';')
    log1 = {x.split('.')[0]: x.split('.')[1]for x in s1}
    log2 = {x.split('.')[0]: x.split('.')[1]for x in s2}
    set1 = set(log1.items())
    set2 = set(log2.items())
    return set1 ^ set2


if __name__ == '__main__':
    text = file_opener('hw.log')
    logs = logs_finder(text, 'eid: ')
    lgs = logs_handler(logs)
    print(lgs)
