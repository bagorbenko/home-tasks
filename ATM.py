import operator


atm_content = {
    'usd': {1: 100, 5: 100, 10: 100, 20: 100, 50: 100},
    'byn': {1: 100, 5: 100, 10: 100, 20: 100, 50: 100},
    'eur': {1: 100, 5: 100, 10: 100, 20: 100, 50: 100}}

def get_cash_from_atm(currency: str, amount):
    s = amount
    global atm_content
    currency_dict = atm_content[currency]
    sorted_entries = sorted(currency_dict.items(), key=operator.itemgetter(0))
    sorted_entries.reverse()
    delta_entries = []
    for entry in sorted_entries:
        delta = s // entry[0]
        if delta > 0:
            resulting_delta = min(delta, entry[1])
            if resulting_delta > 0:
                s -= resulting_delta * entry[0];
                delta_entries.append((entry[0], resulting_delta))
    if s == 0:
        for delta_entry in delta_entries:
            currency_dict[delta_entry[0]] -= delta_entry[1]
    return delta_entries


def atm_amount(currency: str):
    global atm_content
    currency_dict = atm_content[currency]
    res = 0
    for x in currency_dict.items():
        res += x[0] * x[1]
    return res


print(atm_amount('usd'))
print(atm_amount('byn'))
print(atm_amount('eur'))
print('------------------------')
print('ATM balance: ', atm_content)
print(get_cash_from_atm('usd', 2058))
print('ATM balance: ', atm_content)
print(get_cash_from_atm('eur', 4040))
print('ATM balance: ', atm_content)
print(get_cash_from_atm('byn', 2320))
print('------------------------')
print('ATM balance: ', atm_content)
print('------------------------')
print('USD balance ', atm_amount('usd'))
print('BYN balance ', atm_amount('byn'))
print('EUR balance ', atm_amount('eur'))