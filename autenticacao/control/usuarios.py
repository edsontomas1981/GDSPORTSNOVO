from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class Usuarios (User):
    def create_user(self,dados):
        try:
            self.user = User.objects.create_user(dados['login'],dados['login'],dados['cadastroSenha'])
            return 200
        except:
            return 300

    def entrar(self,user,passw):
        self.user = authenticate(username=user,password=passw)
        if self.user is not None:
            return 200
        else:
            return 300
    
    def usuario_dict(self):
        return {'id': self.user.id,
                'email': self.user.email,
    }

