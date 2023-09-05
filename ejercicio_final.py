# en este proyecto , podras desarrolar un chatbot en pyhton, 
# que nos pida que le digamsos algo y tome eso que le decimos, analice el sentimiento y 
# nos responda cual es el sentimiento 


#importamoos un modulo que funciona con luguage natural implementado en una IA

from textblob import TextBlob

class AnalizadorDeSentimiento:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "Negativo"
        
analizador = AnalizadorDeSentimiento()
resultado = analizador.analizar_sentimiento("hello, i'm fine?")
print(resultado)