// Selecionar todos os botões "Adicionar ao carrinho"
// const btnAdicionaCarrinho = document.querySelector('.btnAdicionaCarrinho')

function adicionarAoCarrinho(element) {
  let carrinho = localStorage.getItem('carrinho');
  let img = element.dataset.capa;
  let descricao = element.dataset.descricao;
  let id = element.dataset.id;
  let preco = element.dataset.preco;

  if (!carrinho) {
    carrinho = [];
  } else {
    carrinho = JSON.parse(carrinho);
  }

  // Verificar se o produto já existe no carrinho
  let produtoExistente = carrinho.find((produto) => produto.id === parseInt(id));

  if (produtoExistente) {
    // Se o produto já existe, aumentar a quantidade
    produtoExistente.quantidade += 1;
  } else {
    // Caso contrário, adicionar o produto ao carrinho
    carrinho.push({
      'id': parseInt(id),
      'img': img,
      'desc': descricao,
      'preco': parseFloat(preco),
      'quantidade': 1
    });
  }

  localStorage.setItem('carrinho', JSON.stringify(carrinho));
  updateWidgetCarrinho();
}
  
// Limpar o carrinho
function limparCarrinho() {
  localStorage.removeItem('carrinho');
}



