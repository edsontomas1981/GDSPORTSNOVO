def checa_campos_vazios(dict_request:dict,require_items:list):
    campos_vazios = []
    for chave, valor in dict_request.items():
        if valor == "" or valor is None:
            if chave in require_items:
                campos_vazios.append(chave)
    return campos_vazios
