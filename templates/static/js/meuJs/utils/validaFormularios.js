const validaForm = (formulario)=>{
    if (formulario.checkValidity()) {
      return true;
    }else{
      return false;
    }
}