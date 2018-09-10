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

domain = whois.query('drweb.com')
print(domain.__dict__)
