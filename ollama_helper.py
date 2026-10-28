"""
Wrapper de compatibilidade: substitui o cliente Anthropic pelo Ollama local.
Exponha exatamente as mesmas interfaces usadas nos notebooks do tutorial.
"""
import subprocess
import time
import urllib.request
import ollama as _ollama

MODEL_NAME = "llama3.2:1b"

# Objeto sentinela para manter compatibilidade com notebooks que usam `client`
class _FakeClient:
    pass

client = _FakeClient()


def _ensure_ollama_running():
    """Verifica se o servidor Ollama está rodando; se não, inicia automaticamente."""
    try:
        urllib.request.urlopen("http://localhost:11434/", timeout=2)
    except Exception:
        print("⚡ Iniciando servidor Ollama...", flush=True)
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        # Aguarda o servidor ficar disponível
        for _ in range(15):
            time.sleep(1)
            try:
                urllib.request.urlopen("http://localhost:11434/", timeout=1)
                print("✅ Ollama pronto!", flush=True)
                return
            except Exception:
                pass
        raise RuntimeError("Não foi possível iniciar o servidor Ollama. Execute 'ollama serve' no terminal.")


def get_completion(prompt: str, system_prompt: str = "") -> str:
    """
    Envia um prompt ao modelo local via Ollama e retorna o texto da resposta.
    Interface idêntica à função get_completion usada nos notebooks originais.
    """
    _ensure_ollama_running()
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
    _ensure_ollama_running()
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
