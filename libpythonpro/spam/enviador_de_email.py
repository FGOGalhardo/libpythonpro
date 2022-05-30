class Enviador:
    '''
    Esta classe é uma instância que engloba as funções de uma pessoa que esteja enviando uma mensagem via email.
    '''

    def enviar(self, remetente, destinatario, assunto, corpo):
        '''
        Método que recebe como entrada um remetente, um destinatario, um assunto e um corpo/mensagem/conteúdo
        referentes à um email. Ele verifica se o endereço de email passado como "remetente" é ou não um
        endereço de emial válido. Se o endereço de emial contiver um "@" será um email válido, caso contrário,
        o email será inválido, sendo um email válido, a mensagem será enviada, caso contrário não.

        param: remetente - string - endereço de email
        param: destinatário - string - endereço de email
        param: assunto - string - frase do título do email
        param: corpo - string - mensagem/conteúdo do corpo do email

        Por exemplo:
        remetente: email1@gmail.com
        Como possui o "@", o método retornará o endereço do remetente, identificando o endereço passado como um email
        e portanto a mensagem será enviada.

        remetente: email2.com
        Como não há um "@" o método retornará a seguinte mensagem: "Email de remetente inválido: email2.com",
        identificando o endereço passado como um email inválido e portanto a mensagem não será enviada.
        '''
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente inválido: {remetente}')
        return remetente


class EmailInvalido(Exception):
    '''
    Método que recebe como entrada uma exception referentes à um email inválido. Sendo um email inválido,
    a classe retornará a seguinte mensagem: "Email de remetente inválido: email2.com", referente ao método
    "enviar()" da classe "Enviador()" identificando o endereço passado como um email inválido e portanto a
    mensagem não será enviada.
    '''
    pass