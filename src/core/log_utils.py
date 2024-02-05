from core.config import logging, log_parsed_result_string, headless_automation


def log(log_line, with_divisor=False):
    if logging:
        print(log_line)
        if with_divisor:
            if headless_automation:
                print_divisor_splitter()
            else:
                print_divisor_line()


def get_formatted_address_from_raw_address(address):
    return "\n\t- {}".format(address.lstrip())


def build_address_list(address_string):
    split_addresses = address_string.split('\n')
    formatted_addresses = [get_formatted_address_from_raw_address(address) for address in split_addresses]
    return ''.join(formatted_addresses)


def log_parsed_result(address, start_time, end_time):
    log(log_parsed_result_string.format(build_address_list(address), start_time, end_time), with_divisor=True)


def print_divisor_line():
    log('-' * 80)


def print_divisor_splitter():
    log('***')
