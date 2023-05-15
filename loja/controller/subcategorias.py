from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from loja.models.menus import Menus
from produtos.models.subcategoria import Subcategoria
from django.db.models import Count


def subcategorias_por_menu(menu_id):
    # Busca o menu especificado pelo ID
    menu = get_object_or_404(Menus, id=menu_id)
    # Busca todas as categorias relacionadas ao menu
    categorias = menu.menus_categoria.all()
    # Busca todas as subcategorias relacionadas às categorias
    subcategorias = Subcategoria.objects.filter(categoria_fk__in=categorias).distinct().annotate(total_registros=Count('id'))
    # Converte as subcategorias em uma lista de dicionários
    subcategorias_list = [{'id': subcategoria.id,
                           'descricao':subcategoria.descricao,    
                           'total_registros': subcategoria.total_registros,} for subcategoria in subcategorias]
    return subcategorias_list
