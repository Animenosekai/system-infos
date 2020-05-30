import lifeeasy

print('System Information')
print("System: " + lifeeasy.system())
print("Node name: " + lifeeasy.node())
print("Release: " + lifeeasy.release())
print("Version: " + lifeeasy.version())
print("Machine: " + lifeeasy.machine())
print("Boot Time: " + lifeeasy.boot_time())
print('')
input('Continue...')
lifeeasy.clear()

print("Processor (CPU): " + lifeeasy.processor())
print("Number of physical cores: " + str(lifeeasy.number_of_physical_cores()))
print("Number of cores: " + str(lifeeasy.number_of_cores()))
print("CPU Max Freq.: " + str(lifeeasy.cpu_max_frequency()))
print("CPU Min Freq.: " + str(lifeeasy.cpu_min_frequency()))
print('')
input('Continue...')
lifeeasy.clear()

print('Total RAM: ' + lifeeasy.total_ram())
print('Total SWAP Mem.: ' + lifeeasy.total_swap_memory())
print('')
input('Continue...')
lifeeasy.clear()

print("Disks Infos: " + str(lifeeasy.disks_infos()))
print('')
input('Continue...')
lifeeasy.clear()

print("IP Address: " + lifeeasy.ip_address())
print("Number of network interfaces: " + str(lifeeasy.number_of_network_interfaces()))
print('')
input('Continue...')
lifeeasy.clear()

lifeeasy.display_title('Real Time System Monitoring')
time = lifeeasy.today() + ' ' + lifeeasy.current_time()
cpu_freq = "CPU Freq.: " + str(lifeeasy.cpu_current_frequency()) + "Mhz"
cpu_usage = "CPU Usage: " + str(lifeeasy.cpu_usage()) + "%"
ram_usage = "RAM Usage: " + str(lifeeasy.used_ram()) + '/' + str(lifeeasy.total_ram()) + ' (' + str(lifeeasy.used_ram_percentage()) + '%)'
swap_usage = 'SWAP Usage: ' + str(lifeeasy.used_swap_memory()) + '/' + str(lifeeasy.total_swap_memory()) + ' (' + str(lifeeasy.used_swap_memory_percentage()) + '%)'
disk_read = "Disk Total Read: " + lifeeasy.disk_total_read()
disk_write = "Disk Total Write: " + lifeeasy.disk_total_write()
net_receive = "Net. Total Received: " + lifeeasy.net_total_bytes_received()
net_sent = "Net. Total Sent: " + lifeeasy.net_total_bytes_sent()

lifeeasy.display_body([time, '', cpu_freq, cpu_usage, ram_usage, swap_usage, disk_read, disk_write, net_receive, net_sent])
lifeeasy.display(wait=0.5, delay=0.5)
try:
    while True:
        time = lifeeasy.today() + ' ' + lifeeasy.current_time()
        cpu_freq = "CPU Freq.: " + str(lifeeasy.cpu_current_frequency()) + "Mhz"
        cpu_usage = "CPU Usage: " + str(lifeeasy.cpu_usage()) + "%"
        ram_usage = "RAM Usage: " + str(lifeeasy.used_ram()) + '/' + str(lifeeasy.total_ram()) + ' (' + str(lifeeasy.used_ram_percentage()) + '%)'
        swap_usage = 'SWAP Usage: ' + str(lifeeasy.used_swap_memory()) + '/' + str(lifeeasy.total_swap_memory()) + ' (' + str(lifeeasy.used_swap_memory_percentage()) + '%)'
        disk_read = "Disk Total Read: " + lifeeasy.disk_total_read()
        disk_write = "Disk Total Write: " + lifeeasy.disk_total_write()
        net_receive = "Net. Total Received: " + lifeeasy.net_total_bytes_received()
        net_sent = "Net. Total Sent: " + lifeeasy.net_total_bytes_sent()

        lifeeasy.display_body([time, '', cpu_freq, cpu_usage, ram_usage, swap_usage, disk_read, disk_write, net_receive, net_sent])
except:
    lifeeasy.stop_display()
    lifeeasy.clear()
    lifeeasy.display_action('End')
    print('')
    print('Thank you for using my program today!')
    print('© Anime no Sekai - 2020')
