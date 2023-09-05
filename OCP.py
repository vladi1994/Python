class Notificador():
    def __init__(self,usuario , mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por MAIL A {self.usuario.email}")
        
        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por MAIL A {self.usuario.sms}")
        

class NotificadorWhatsapp(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por MAIL A {self.usuario.whatsapp}")        
        
class NotificadorTwiter(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por MAIL A {self.usuario.tweter}")