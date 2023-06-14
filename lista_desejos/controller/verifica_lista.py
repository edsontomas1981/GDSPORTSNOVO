def verificar_produto_na_lista(produto_id, lista):
    for item in lista:
        if item['id'] == produto_id:
            return True
    return False
