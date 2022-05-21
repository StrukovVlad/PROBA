from check_ip_function import check_ip


def return_correct_ip(ip_s):
    rex = []
    for ip in ip_s:
        if check_ip(ip):
            rex.append(ip)
    return rex


print('Проверка списка IP-адресов')
ip_list = ['10.1.1.1', '8.8.8.8', '2.2.2']
rex = return_correct_ip(ip_list)
print(rex)

