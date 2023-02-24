import openai

openai.api_key = "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"

def consultar_chatgpt(prompt):
    """
        -> Exibe o prompt e retorna o dado digitado
        :param prompt: mensagem que sera exibida para o usuario
        :return: dado digitado pelo usuario
    """
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


print("-----------chat gpt start------------")
pergunta_fixa = "Implemente no padrao docstring em portugues o seguinte codigo python, nao altere o codigo principal viu?"
while True:

    pergunta = str(input())
    resposta = consultar_chatgpt(pergunta_fixa+pergunta)
    print(resposta)
