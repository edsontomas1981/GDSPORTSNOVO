const confere_senha_confSenha=(senha,confSenha)=>{
  if (senha ===confSenha){
    return true
  }
  return false
}

const validarSenha = (senha) => {
  let msgResposta = { senhaValida: false, listaErros: [] };
  if (senha.length < 8) {
    msgResposta.listaErros.push("Senha precisa ter no mínimo 8 caracteres");
  }
  if (!senha.match(/[a-z]/)) {
    msgResposta.listaErros.push(
      "É necessário ter ao menos uma letra minúscula"
    );
  }
  if (!senha.match(/[A-Z]/)) {
    msgResposta.listaErros.push(
      "É necessário ter ao menos uma letra maiúscula"
    );
  }
  if (!senha.match(/[0-9]/)) {
    msgResposta.listaErros.push("É necessário ter ao menos um número");
  }
  if (!senha.match(/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/)) {
    msgResposta.listaErros.push(
      "É necessário ter ao menos um caracter especial"
    );
  }
  if (msgResposta.listaErros.length === 0) {
    msgResposta["senhaValida"] = true;
  }
  return msgResposta;
};

