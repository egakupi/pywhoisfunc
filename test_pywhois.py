from pywhois import pywhoisfunc

domain_list = ['drweb.com', 'drweb.ru', 'drweb.net', 'drweb.de']

for domain in domain_list:
    print(pywhoisfunc(domain))
