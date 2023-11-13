
def calculate_interest_rate(account_type):
    if account_type == 'saving':
        return 0.02
    elif account_type == 'current':
        return 0.01
    else:
        return 0.005

def calculate_interest(account_type, balance):
    rate = calculate_interest_rate(account_type)
    return balance * rate
