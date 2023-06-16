from pedidos.models.pedidos import Pedidos as Mdl_Pedidos
from produtos.control.produtos import Produtos

class Pedidos:
    def __init__(self):
        self.obj_pedido = Mdl_Pedidos()

    def add_prod_ao_pedido(self,produto_id):
        pass
    
    def del_prod_ao_pedido(self,produto_id):
        pass

    
