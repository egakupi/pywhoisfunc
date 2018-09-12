import whois

"""
Реализовать функцию, которая запускает штатную linux-утилиту "whois" для переданного доменного имени, разбирает вывод и возвращает:
- дату создания домена в виде той или иной структуры данных (например, https://docs.python.org/3/library/time.html#time.struct_time для Python)
- список name server'ов (если получены)
- название организации (если есть)

Если произошла ошибка / дата не найдена - возвращать False.
Проверять работу на:
drweb.com
drweb.ru
drweb.net
drweb.de
"""


def pywhoisfunc(domain):
    try:
        domain_struct = whois.query(domain, ignore_returncode=1)
        if not domain_struct.__dict__['creation_date']:
            return False
        else:
            result = [domain_struct.__dict__['creation_date'].timetuple()]
            if domain_struct.__dict__['name_servers']:
                result.append(domain_struct.__dict__['name_servers'])
            if domain_struct.__dict__['registrar']:
                result.append(domain_struct.__dict__['registrar'])
            return result
    except:
        return False
