let widgetListaDesejos = document.getElementById('listaDesejos')

const widgetCurtidas=(produtos)=>{
    let html
    if(produtos!=0){
    html =  `<a href="#" >
            <div class="qty">${produtos}</div>
            <i class="fa fa-heart-o"></i>
            <span>Curtidas</span>
            </a>`}else{
            html =  `<a href="#" >
                <i class="fa fa-heart-o"></i>
                <span>Curtidas</span>
                </a>`          
            }
    widgetListaDesejos.innerHTML = html
}