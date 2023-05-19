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