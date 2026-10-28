"""
Wrapper de compatibilidade: substitui o cliente Anthropic pelo Ollama local.
Exponha exatamente as mesmas interfaces usadas nos notebooks do tutorial.
"""
import ollama as _ollama

MODEL_NAME = "phi3:mini"

# Objeto sentinela para manter compatibilidade com notebooks que usam `client`
class _FakeClient:
    pass

client = _FakeClient()


def get_completion(prompt: str, system_prompt: str = "") -> str:
    """
    Envia um prompt ao modelo local via Ollama e retorna o texto da resposta.
    Interface idêntica à função get_completion usada nos notebooks originais.
    """
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    response = _ollama.chat(
        model=MODEL_NAME,
        messages=messages,
        options={"temperature": 0.0, "num_ctx": 2048},
    )
    return response.message.content


def get_completion_with_prefill(prompt: str, prefill: str, system_prompt: str = "") -> str:
    """
    Versão com prefill do assistente (usada no Capítulo 5 e 6).
    Inclui uma mensagem inicial do assistente para 'falar pelo Claude'.
    """
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    messages.append({"role": "assistant", "content": prefill})

    response = _ollama.chat(
        model=MODEL_NAME,
        messages=messages,
        options={"temperature": 0.0, "num_ctx": 2048},
    )
    return prefill + response.message.content
