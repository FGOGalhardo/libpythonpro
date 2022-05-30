from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.enviador_de_email import EmailInvalido
import pytest


# Teste que verifica se um email está sendo enviado.
def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


# Teste que verifica se o endereço de remetente que está sendo passado
# é de fato o endereço do remetente.
@pytest.mark.parametrize(
    'remetente',
    ['eu@eu.com', 'ele@ele.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'voce@voce.com',
        'Cominidade DevPro',
        'Primeira turma Guido Von Rossun aberta.',
    )
    assert remetente in resultado


# Teste que verifica se o endereço de remetente que está sendo passado
# é um endereço de remetente válido.
@pytest.mark.parametrize(
    'remetente',
    ['', 'ele']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'voce@voce.com',
            'Cominidade DevPro',
            'Primeira turma Guido Von Rossun aberta.',
        )



