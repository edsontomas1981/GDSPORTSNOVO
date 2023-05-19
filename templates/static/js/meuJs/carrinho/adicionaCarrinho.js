// Selecionar todos os botões "Adicionar ao carrinho"
// const btnAdicionaCarrinho = document.querySelector('.btnAdicionaCarrinho')

// Função para adicionar ao carrinho
function adicionarAoCarrinho(element) {
  let qtdeCarrinho = document.getElementById('qtdeCarrinho')
  let carrinho = localStorage.getItem('carrinho');
  let img = element.dataset.capa
  let descricao = element.dataset.descricao
  let id = element.dataset.id
  if (!carrinho) {
    carrinho = [];
  } else {
    carrinho = JSON.parse(carrinho);
  }

  carrinho.push({'id':parseInt(id),'img':img,'desc':descricao});

  localStorage.setItem('carrinho', JSON.stringify(carrinho));
}
  

  
// Limpar o carrinho
function limparCarrinho() {
  localStorage.removeItem('carrinho');
}


