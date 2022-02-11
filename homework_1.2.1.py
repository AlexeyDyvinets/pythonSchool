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
    return logs_list


def check_differences(first_element, second_element):
    return set(first_element.items()) ^ set(second_element.items())


if __name__ == '__main__':
    open_log = file_opener('hw.log')
    desired_log = logs_finder(open_log, 'D:TUpdaterController::SetUniqueParam(429): eid:')
    last_two_row = logs_handler(desired_log)
    print(f'Last row: {last_two_row[0]}\nPrevious row: {last_two_row[1]}')
    print(check_differences(*last_two_row))
