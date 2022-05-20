import logging


def file_opener(file):
    log = open(file)
    text = log.readlines()
    log.close()
    return text


def error_finder(s_text, pattern):
    error_logs = [x for x in s_text if pattern in x or pattern.capitalize() in x or pattern.upper() in x]
    error_log_as_str = ''.join(error_logs)
    logging.basicConfig(level='ERROR', filename=' found_errors.log')
    logger = logging.getLogger()
    logger.error(error_log_as_str)


if __name__ == '__main__':
    log_file = file_opener('yupdate.log')
    error_finder(log_file, 'error')
