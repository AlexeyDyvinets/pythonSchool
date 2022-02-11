def file_opener(file):
    log = open(file)
    text = log.readlines()
    log.close()
    return text


def logs_finder(s_text, pattern):
    if s_text == 0:
        return "Ничего не найдено. Список пуст"
    else:
        if [x for x in s_text[::-1] if pattern not in x]:
            return 'Такой строчки в списке нет'
        else:
            logs = [x for x in s_text[::-1] if pattern in x][:2]
            return logs


def logs_handler(logs):
    # там где код повторяеться 2 раза выглядит не оч, напиши цикл тогда уже
    log1 = logs[0].strip()
    s1 = log1[log1.find('eid: ') + len('eid: '):].split(';')
    log2 = logs[1].strip()
    s2 = log2[log2.find('eid: ') + len('eid: '):].split(';')
    log1 = {x.split('.')[0]: x.split('.')[1] for x in s1}
    log2 = {x.split('.')[0]: x.split('.')[1] for x in s2}
    set1 = set(log1.items())
    set2 = set(log2.items())
    return set1 ^ set2


if __name__ == '__main__':
    open_log = file_opener('hw.log')
    desired_log = logs_finder(open_log, 'eid: ')
    print(desired_log)
