from correios_utils import (
    Cotacao,
    FormatoEncomenda,
    SimNao,
    Servico,
    realizar_cotacao,
    get_descricao_servico,
)


class Calcula_frete():
    def realiza_cotacao(self,dados):
        self.servicos = realizar_cotacao(
            cep_origem=dados['cep_origem'],
            cep_destino=dados['cep_destino'],
            codigos_servicos=[Servico.PAC, Servico.SEDEX, Servico.SEDEX_10],
            peso=dados['peso'],
            comprimento=dados['comprimento'],
            altura=dados['altura'],
            largura=dados['largura'],
            diametro=dados['diametro'],
            formato_encomenda=FormatoEncomenda.CAIXA_PACOTE,
            valor_declarado=dados['valor_produtos'],
            mao_propria=SimNao.NAO,
            aviso_recebimento=SimNao.NAO,
            codigo_empresa="08082650",
            senha_empresa="564321",
        )
        lista_fretes = []
        for servico in self.servicos:
            if not servico.erro:
                lista_fretes.append({'tipo_servico':get_descricao_servico(servico.codigo),
                                     'valor':servico.valor,
                                     'prazo':servico.prazo_entrega})

        return lista_fretes                