from twilio.rest import Client
import twilio

account_sid = "seu_account_sid"
auth_token = "seu_auth_token"
meu_numero = "seu_numero"
numero_twilio = "seu_numero_twilio"

cliente = Client(account_sid, token)

mensagem = """
<Response>
<Say language="pt-BR">
Olá, Canal Datacoin na linha, tudo bem com você?
</Say>
</Response>
"""

ligacao = cliente.calls.create(
    to=meu_numero,
    from_=numero_twilio,
    twiml=mensagem
)