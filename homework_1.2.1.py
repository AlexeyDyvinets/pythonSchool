def file_opener(file):
    log = open(file)
    text = log.readlines()
    log.close()
    return text


def logs_finder(s_text, pattern):
    logs = [x for x in s_text[::-1] if pattern in x]
    if logs:
        return logs[:2]
    else:
        exit()


def logs_handler(logs):
    logs_list = []
    for log_str in logs:
        log_sep = log_str[log_str.find('eid: ') + len('eid: '):].strip().split(';')
        logs_list.append({x.split('.')[0]: x.split('.')[1] for x in log_sep})
    return set(logs_list[0].items()) ^ set(logs_list[1].items())


if __name__ == '__main__':
    open_log = file_opener('hw.log')
    desired_log = logs_finder(open_log, 'D:TUpdaterController::SetUniqueParam(429): eid:')
    print(logs_handler(desired_log))

