let menu  =document.getElementById('menu')
window.addEventListener('load',()=>{
    updateWidgetCarrinho();
    carregaMenu();
})

const carregaMenu = async ()=>{
    let url = '/home/menus/'
    let dados = {'login':email.value,'senha':senha.value}
    let conexao = new Conexao(url,dados)
    let html=`<li class="active"><a href="/home/" class="teste" id="0">Home</a></li>`
    let result= await conexao.sendPostRequest()
    result.status.forEach(element => {
        html+=geraMenu(element)
    });
    // Adicionando o HTML gerado na div container
    menu.innerHTML = html;
}

const geraMenu = (dados)=>{
    // Gerando o HTML a partir do resultado da requisição
    return `
        <li><a href="#" class="teste"  id="${dados.id}" onclick="carregaPageMenu(this)">${dados.descricao}</a></li>
    `;
}

const carregaPageMenu = (idMenu)=>{
    const url = `/home/categoria/?idMenu=${idMenu.id}`;
    window.location.href = url;
}
