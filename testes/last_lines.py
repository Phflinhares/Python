import io

def last_lines(file_path, tamanho=io.DEFAULT_BUFFER_SIZE):

    #Ler o arquivo TXT em pedaços
    def ler_pedacos(file, tamanho):
        while True:
            pedaco = file.read(tamanho)
            if not pedaco:
                break
            yield pedaco


    #Garantir a codificação 
    def safe_code(pedaco, encoding='utf-8'):
        decoded, lembrar = '', b''
        try:
            decoded = pedaco.decode(encoding)
        except UnicodeDecodeError as e:
            decoded = pedaco[:e.start].decode(encoding)
            lembrar = pedaco[e.start:]
        return decoded, lembrar



    linhas = []
    lembrar = b''

    with open(file_path, 'rb') as file:
        for pedaco in ler_pedacos(file, tamanho):
            pedaco = lembrar + pedaco
            pedaco_certo, lembrar = safe_code(pedaco)
            
            linhas_separadas = pedaco_certo.splitlines(keepends=True)

            if linhas_separadas:
                linhas.extend(linhas_separadas)

            #Guardando a ultima linha
            if not pedaco_certo.endswith('\n'):
                lembrar = linhas_separadas[-1].encode('utf-8') + lembrar
            else:
                lembrar = b''

    #Adiciona a quebra de linha
    linhas = [linha if linha.endswith('\n') else linha + '\n' for linha in linhas]

    #Reverte as linhas
    linhas_reversas = reversed(linhas)

    return iter(linhas_reversas)
