import tabulate
import os
import time


def check_directory_exist(path):
    '''
    Check whether path exist.  Return True/False based on result.
    :param path: directory to check if it exist.
    :return: True or False
    '''

    isdir = os.path.isdir(path)
    return isdir


def create_directory(path):
    # Create directory if it doesn't exist.
    return os.makedirs(path)


def save_to_text(filename, path="", payload=""):
    if right(filename, 4) != ".txt":
        filename = filename + ".txt"
    completeFilename = filename
    if path != "":
        completeFilename = os.path.join(path, filename).replace('\\', '/')
    text_file = open(completeFilename, 'w')
    text_file.write(payload)
    text_file.close()


def print_template_table(templates):

    headers = [
        'Template Name',
        'Description',
        'Device Type',
        'Feature Templates',
    ]

    table = []

    for template in templates:
        general_templates = ''
        for subTemplate in template['generalTemplates']:
            general_templates += subTemplate['templateName'] + '\n'

        row = [
            template['templateName'],
            template['templateDescription'],
            template['deviceType'],
            general_templates,
        ]
        table.append(row)

    try:
        print(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
        return True
    except UnicodeEncodeError:
        print(tabulate.tabulate(table, headers, tablefmt="grid"))
        return True


def print_device_table(devices):

    headers = [
        'Host-Name',
        'Device Type',
        'Device ID',
        'Serial Number',
        'System IP',
        'Site ID',
        'Version',
        'Device Model',
        'Template',
    ]

    table = []
    return_list = []

    for device in devices:
        if 'host-name' in device and 'system-ip' in device:
            if not 'template' in device:
                device['template'] = ""
            row = [
                device['host-name'],
                device['deviceType'],
                device['uuid'],
                device['serialNumber'],
                device['system-ip'],
                device['site-id'],
                device['version'],
                device['deviceModel'],
                device['template'],
            ]
            return_row = [
                device['host-name'],
                device['uuid']
            ]
            # if 'template' in device:
            #     row.append(device['template'])
            table.append(row)
            return_list.append(return_row)

    try:
        print(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
        time.sleep(1)
    except UnicodeEncodeError:
        print(tabulate.tabulate(table, headers, tablefmt="grid"))
        time.sleep(1)
    return return_list


def left(s, amount):
    return s[:amount]


def right(s, amount):
    return s[-amount:]


def mid(s, offset, amount):
    return s[offset:offset+amount]