function verificarLogin() {
    var sessionCookie = getCookie('sessionid');
    if (sessionCookie) {
      console.log('O usuário está logado.');
      // Faça algo se o usuário estiver logado
    } else {
      console.log('O usuário não está logado.');
      // Faça algo se o usuário não estiver logado
    }
  }
  
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
  verificarLogin();
  