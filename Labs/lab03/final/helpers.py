import tabulate
import time


def print_route_list(route_list):

    headers = [
        'Host-Name',
        'System IP',
        'Destination Route',
        'Routing Instance',
        'Route Metric',
    ]

    table = []

    for route in route_list:
            row = [
                route['vdevice-host-name'],
                route['vdevice-name'],
                route['route-destination-prefix'],
                route['routing-instance-name'],
                route['route-metric'],
            ]
            table.append(row)

    try:
        print(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
        time.sleep(1)
    except UnicodeEncodeError:
        print(tabulate.tabulate(table, headers, tablefmt="grid"))
        time.sleep(1)

