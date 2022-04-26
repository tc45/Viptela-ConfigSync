import tabulate


def count_tlocs(tloc_list):
    unique_devices = []
    device_list = []

    for tlocs in tloc_list:
        if tlocs['system-ip'] not in unique_devices:
            unique_devices.append(tlocs['system-ip'])

    for device in unique_devices:
        public_internet = 0
        default = 0
        mpls = 0
        other = 0
        for tlocs in tloc_list:
            if tlocs['system-ip'] == device:
                if tlocs['color'] == 'default':
                    default += 1
                elif tlocs['color'] == 'public-internet':
                    public_internet += 1
                elif tlocs['color'] == 'mpls':
                    mpls += 1
                else:
                    other += 1
        row = [
            device,
            default,
            mpls,
            public_internet,
            other,
        ]
        device_list.append(row)
    return device_list


def parse_tlocs(tloc_list):

    headers = [
        'hostname',
        'default',
        'mpls',
        'public-Internet',
        'other',
    ]

    try:
        print(tabulate.tabulate(tloc_list, headers, tablefmt="fancy_grid"))
    except UnicodeEncodeError:
        print(tabulate.tabulate(tloc_list, headers, tablefmt="grid"))