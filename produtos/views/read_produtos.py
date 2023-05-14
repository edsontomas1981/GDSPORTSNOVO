from django.shortcuts import render
from django.http import JsonResponse
from produtos.models import Produtos
from django.shortcuts import get_object_or_404
import json

def read_produtos (request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == "POST" :
        try:
            data = json.loads(request.body.decode('utf-8'))
            produto_id = data.get('idProduto')
            if produto_id is None:
                raise ValueError('Campo "produto_id" não encontrado no corpo da requisição')
            produto = get_object_or_404(Produtos.objects.prefetch_related('imagens_set'), id=produto_id)
            imagens_data = [{'nome': imagem.nome, 'imagem_url': imagem.imagem.url} for imagem in produto.imagens_set.all()]
            data = {'produto': produto.to_dict(), 'imagens': imagens_data}
            return JsonResponse(data)
        except (json.JSONDecodeError, ValueError) as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Produtos.DoesNotExist:
            return JsonResponse({'error': f'Produto com id={produto_id} não encontrado'}, status=404)
