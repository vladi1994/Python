import openai

openai.api_key = "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"
system_rol =''' hace de cuneta que sos un analizador de sentimiento.
                yo te paso sentimientos y vos analizas lo analizas, desde los mensajes y me
                das una respuesta con al meno 1 caracter y como maximo 4.
                solo respuestas numericas: donde -1 es negatividad maxima, 0 es neutral y 1 es positividad maxima.
                1 representara negatividad maxima y 1 positividad maxima 
                (Podes responder solo con ints o floats)
                '''
                
mensajes = [{"role":"system", "content": system_rol}]

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if polaridad > -0.8 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo"
        
        if polaridad > -0.3 and polaridad < -0.1:
            return "\x1b[1;31m" + "Algo Negativo"
        
        if polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;32m" + "Neutral"
                         
        if polaridad >= 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo Positivo"
            
        if polaridad >= 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo"
                         
        if polaridad > 0.9:
            return "\x1b[1;31m" + "Muy Positivo"
        else:
            return "\x1b[1;31m" + "Muy Negativo"

analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "\n Dime algo " + "\x1b[1;37m" )
    mensajes.append({"role": "user", "content": user_prompt})
    
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8        
    )
    
    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role": "assistant", "content":respuesta })
    
    sentimiento = analizador.analizar_sentimiento(respuesta)
    print(sentimiento)