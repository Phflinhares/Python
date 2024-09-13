import io

def last_lines(file_path, chunk_size=io.DEFAULT_BUFFER_SIZE):

    #Ler o arquivo TXT em pedaços
    def read_in_chunks(file, chunk_size):
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk


    #Garantir a codificação 
    def safe_decode(chunk, encoding='utf-8'):
        decoded, remainder = '', b''
        try:
            decoded = chunk.decode(encoding)
        except UnicodeDecodeError as e:
            decoded = chunk[:e.start].decode(encoding)
            remainder = chunk[e.start:]
        return decoded, remainder



    lines = []
    remainder = b''

    with open(file_path, 'rb') as file:
        for chunk in read_in_chunks(file, chunk_size):
            chunk = remainder + chunk
            decoded_chunk, remainder = safe_decode(chunk)
            
            split_lines = decoded_chunk.splitlines(keepends=True)

            if split_lines:
                lines.extend(split_lines)

            #Guardando a ultima linha
            if not decoded_chunk.endswith('\n'):
                remainder = split_lines[-1].encode('utf-8') + remainder
            else:
                remainder = b''

    #Adiciona a quebra de linha
    lines = [line if line.endswith('\n') else line + '\n' for line in lines]

    #Reverte as linhas
    reversed_lines = reversed(lines)

    return iter(reversed_lines)
