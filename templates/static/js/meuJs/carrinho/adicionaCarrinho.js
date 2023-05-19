// Selecionar todos os botões "Adicionar ao carrinho"
const btnsAdicionarAoCarrinho = document.querySelectorAll('.btnAdicionaCarrinho');

// Adicionar evento de clique a cada botão
btnsAdicionarAoCarrinho.forEach(btn => {
  btn.addEventListener('click', function() {
    const capa = this.getAttribute('data-capa');
    adicionarAoCarrinho(capa);
  });
});

// Função para adicionar ao carrinho
function adicionarAoCarrinho(capa) {
  let carrinho = localStorage.getItem('carrinho');

  if (!carrinho) {
    carrinho = [];
  } else {
    carrinho = JSON.parse(carrinho);
  }

  carrinho.push(capa);

  localStorage.setItem('carrinho', JSON.stringify(carrinho));
}
  
// Visualizar o carrinho
function verCarrinho() {
  let carrinho = localStorage.getItem('carrinho');

  if (carrinho) {
    carrinho = JSON.parse(carrinho);
    // Faça o processamento necessário para exibir o carrinho
    console.log(carrinho);
  } else {
    console.log('Carrinho vazio');
  }
}
  
// Limpar o carrinho
function limparCarrinho() {
  localStorage.removeItem('carrinho');
}
