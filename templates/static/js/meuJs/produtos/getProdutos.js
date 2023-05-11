let containerProduto = document.getElementById('containerProduto')

window.addEventListener('DOMContentLoaded', async ()=>{
    let url = '/produtos/read_produtos/'
    const urlParams = new URLSearchParams(window.location.search);
    const idProduto = urlParams.get('idProduto');
    let dados={'idProduto':idProduto}
    let conexao = new Conexao(url,dados)
    let htmlProduto=""
    let result= await conexao.sendPostRequest()
    console.log(result)
    htmlProduto=geraHtmlProduto(result)
    console.log(containerProduto)
    containerProduto.innerHTML = htmlProduto;
})

const geraHtmlProduto=(produto)=>{
   return `
    `
}

const carrossel = ()=>{
    `
    <!-- product -->
    <div class="product">
        <div class="product-img">
            <img src="{% static 'img/camisetasPromo/outrasLigas/boca.jpeg' %}" alt="">
        </div>
    </div>
    <!-- /product -->
    `

}