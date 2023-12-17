import os


log_parsed_result_string = 'at: {}\n\nstarting at: {} and\nending at: {}'


def get_formatted_address_from_raw_address(address):
    return "\n\t- {}".format(address.lstrip())


def build_address_list(address_string):
    split_addresses = address_string.split('\n')
    formatted_addresses = [get_formatted_address_from_raw_address(address) for address in split_addresses]
    return ''.join(formatted_addresses)


def print_divisor_line():
    print('-' * 80)
