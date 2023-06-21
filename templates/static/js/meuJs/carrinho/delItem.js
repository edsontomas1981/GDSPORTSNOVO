const delItem = (element) => {
    let id = element.dataset.id;
    let carrinho = localStorage.getItem('carrinho');
    
    if (carrinho) {
        carrinho = JSON.parse(carrinho); // Converte a string em um array
        // Verificar se o produto já existe no carrinho
        let produtoExistente = carrinho.find((produto) => produto.id === parseInt(id));

        if (produtoExistente) {
            // Se o produto já existe, diminuir a quantidade ou remover do carrinho
            if (produtoExistente.quantidade === 1) {
                const index = carrinho.indexOf(produtoExistente);
                carrinho.splice(index, 1); // Remove o item do array
            } else {
                produtoExistente.quantidade -= 1;
            }
            localStorage.setItem('carrinho', JSON.stringify(carrinho));
        }
    }
    location.reload();
}
