from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from produtos.control.produtos import Produtos 
from lista_desejos.controller.lista_desejos import Lista_desejos 
import json
@login_required(login_url='/auth/entrar/')
def lista_desejos(request):
    if request.method == 'GET':
        return JsonResponse({'status': 'status_listadesejos', 'rotas': 'rotas_listadesejos'})
    elif request.method == "POST":
        user = request.user
        data = json.loads(request.body.decode('utf-8'))
        produto=Produtos()
        produto.read_produto_id(data['produtoId'])
        lista=Lista_desejos()
        lista.add_produto_lista_desejos(user,produto)
        listaProdutos = [i.produtos_fk.to_dict() for i in lista.read_lista(user)]
        return JsonResponse({'status': 200, 'produtos': listaProdutos})
