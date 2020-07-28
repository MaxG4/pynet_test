import yaml
from concurrent.futures import ThreadPoolExecutor
from netmiko import ConnectHandler


def netmio_show(device_dict):
    net_connect = ConnectHandler(**device_dict)
    print(net_connect.find_prompt())
    return 

if __name__ == "__main__":
    main()

    yaml_file = "devices.yml"
    with open(yaml_file) as f:
        devices = yaml.load(f)

    sros_devices = devices["sros"]
    junos_deivces = devices["juniper"]

    device_list = sros_devices + junos_deivces

# create thread pool
    pool = ThreadPoolExecutor(max_workers=WORKERS)
    futures = []

# submit work for thread pool
    for devices in device_list
        device_dict = devices[device]
        # netmiko_show(device_list)
        futures.append(pool.submit(netmiko_show, (device_dict)))

# wait till task as 
        wait(futures)
        for task_result in futures:
            print(task_result.result())
        



