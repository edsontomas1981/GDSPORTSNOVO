
const removeItemCarrinho = (idProduto) => {
    let itensCarrinho = JSON.parse(localStorage.getItem('carrinho')); // Obtém os itens do carrinho do localStorage
  
    // Verifica se itensCarrinho é uma matriz válida
    if (!Array.isArray(itensCarrinho)) {
      return;
    }
  
    // Encontra o índice do item com o ID correspondente no carrinho
    const indice = itensCarrinho.findIndex(item => item.id === idProduto);
  
    // Verifica se o item foi encontrado
    if (indice !== -1) {
      itensCarrinho.splice(indice, 1); // Remove o item do carrinho usando o índice
  
      // Atualiza o localStorage com os itens do carrinho atualizados
      localStorage.setItem('carrinho', JSON.stringify(itensCarrinho));
  
      // Atualiza o widget do carrinho
      updateWidgetCarrinho();
    }
  };