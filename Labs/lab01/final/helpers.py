import tabulate
import time


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
            table.append(row)

    try:
        print(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
        time.sleep(1)
    except UnicodeEncodeError:
        print(tabulate.tabulate(table, headers, tablefmt="grid"))
        time.sleep(1)


