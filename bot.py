from whatsapp_web import WhatsApp
import os

# Inicializando o WhatsApp Web
whatsapp = WhatsApp()

# Evento de QR Code
def on_qr(qr):
    print("Escaneie o QR Code abaixo para conectar seu bot ao WhatsApp:")
    print(qr)

whatsapp.on("qr", on_qr)

# Evento de conexão
def on_ready():
    print("Bot conectado ao WhatsApp!")

whatsapp.on("ready", on_ready)

# Evento de mensagem recebida
def on_message(message):
    print(f"Mensagem recebida de {message.sender_name}: {message.text}")

    # Responder ao "Oi"
    if message.text.lower() == "oi":
        whatsapp.reply(message, "Olá! Estou online no Railway!")

whatsapp.on("message", on_message)

# Inicializa o bot
whatsapp.run()
