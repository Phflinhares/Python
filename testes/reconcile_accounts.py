from datetime import datetime, timedelta

def reconcile_accounts(list1, list2):
    def parse_date(date_str):
        return datetime.strptime(date_str, "%Y-%m-%d")
    
    def format_date(date_obj):
        return date_obj.strftime("%Y-%m-%d")
    
    def find_matching_transaction(transaction, other_list):
        trans_date = parse_date(transaction[0])
        for i, other in enumerate(other_list):
            other_date = parse_date(other[0])
            if (trans_date == other_date or
                trans_date == other_date - timedelta(days=1) or
                trans_date == other_date + timedelta(days=1)):
                if transaction[1:] == other[1:]:
                    return i
        return -1
    
    def add_status_column(transactions, found_status):
        return [transaction + [found_status] for transaction in transactions]
    
    list1_with_status = []
    list2_with_status = []
    
    # Make copies of the lists for modification
    list1_copy = [transaction[:] for transaction in list1]
    list2_copy = [transaction[:] for transaction in list2]
    
    # Reconcile list1 against list2
    for i, transaction in enumerate(list1_copy):
        match_index = find_matching_transaction(transaction, list2_copy)
        if match_index != -1:
            list2_copy[match_index].append('FOUND')
            list1_with_status.append(transaction + ['FOUND'])
        else:
            list1_with_status.append(transaction + ['MISSING'])
    
    # For the remaining items in list2 that were not matched
    for transaction in list2_copy:
        if len(transaction) == 4:  # If it doesn't have status, it's missing
            list2_with_status.append(transaction + ['MISSING'])
        else:
            list2_with_status.append(transaction)
    
    return list1_with_status, list2_with_status