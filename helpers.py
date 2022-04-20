import tabulate


def save_to_text(filename, payload):
    if right(filename, 4) != ".txt":
        filename = filename + ".txt"

    text_file = open(filename, 'w')
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
    except UnicodeEncodeError:
        print(tabulate.tabulate(table, headers, tablefmt="grid"))


def print_device_table(devices):
    print("Formatting device output")

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
    except UnicodeEncodeError:
        print(tabulate.tabulate(table, headers, tablefmt="grid"))
    return return_list


def left(s, amount):
    return s[:amount]


def right(s, amount):
    return s[-amount:]


def mid(s, offset, amount):
    return s[offset:offset+amount]