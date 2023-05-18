let btnFiltrar = document.getElementById('btnFiltrar')
btnFiltrar.addEventListener('click',()=>{
    adicionarAoCarrinho(1)
})
// Adicionar um produto ao carrinho
function adicionarAoCarrinho(produtoId) {
    let carrinho = localStorage.getItem('carrinho');
  
    if (!carrinho) {
      carrinho = {'teste':0};
    } else {
      carrinho = JSON.parse(carrinho);
    }
  
    carrinho.push(produtoId);
  
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
  