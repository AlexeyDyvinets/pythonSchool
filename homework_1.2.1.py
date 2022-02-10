def file_opener(file):
    log = open(file)
    s_text = log.readlines()
    # так нет метода клосе снова
    return s_text


def logs_finder(s_text, pattern):
    # что такое s_text, оно ж должно использоваться
    logs = [x for x in text[::-1] if pattern in x][:2] # обработай кейс если не найдено ни одно совпадение
    # т.е если список пуст при попытке среза будет ошибка например срез можно делать только если список не пуст например
    return logs

def logs_handler(logs): # Обращай внимание на подчеркивания ИДЕ
    # там где код повторяеться 2 раза выглядит не оч, напиши цикл тогда уже
    log1 = logs[0].strip()
    s1 = log1[log1.find('eid: ') + len('eid: '):].split(';')
    log2 = logs[1].strip()
    s2 = log2[log2.find('eid: ') + len('eid: '):].split(';')
    log1 = {x.split('.')[0]: x.split('.')[1]for x in s1}
    log2 = {x.split('.')[0]: x.split('.')[1]for x in s2}
    set1 = set(log1.items())
    set2 = set(log2.items())
    print(set1 ^ set2, sep='\n')
    return set1 ^ set2


if __name__ == '__main__':
    text = file_opener('hw.log')
    logs = logs_finder(text, 'eid: ')
    lgs = logs_handler(logs)
