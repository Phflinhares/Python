from datetime import datetime, timedelta

def reconcile_accounts(lista1, lista2):
    def parse_date(date_str):
        return datetime.strptime(date_str, "%Y-%m-%d")
    
    def data_formatada(date_obj):
        return date_obj.strftime("%Y-%m-%d")
    
    def match_transacao(transacao, other_lista):
        trans_date = parse_date(transacao[0])
        for i, other in enumerate(other_lista):
            other_date = parse_date(other[0])
            if (trans_date == other_date or
                trans_date == other_date - timedelta(days=1) or
                trans_date == other_date + timedelta(days=1)):
                if transacao[1:] == other[1:]:
                    return i
        return -1
    
    def add_status(transacaos, found_status):
        return [transacao + [found_status] for transacao in transacaos]
    
    lista1_com_status = []
    lista2_com_status = []
    
    lista1_copy = [transacao[:] for transacao in lista1]
    lista2_copy = [transacao[:] for transacao in lista2]
    
    # Reconciliando as contas lista 1 com lista2
    for i, transacao in enumerate(lista1_copy):
        match_index = match_transacao(transacao, lista2_copy)
        if match_index != -1:
            lista2_copy[match_index].append('FOUND')
            lista1_com_status.append(transacao + ['FOUND'])
        else:
            lista1_com_status.append(transacao + ['MISSING'])
    
    # add missing lista 2 caso não tenha
    for transacao in lista2_copy:
        if len(transacao) == 4:
            lista2_com_status.append(transacao + ['MISSING'])
        else:
            lista2_com_status.append(transacao)
    
    return lista1_com_status, lista2_com_status