from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
import platform


def deepseek(model_size="1.5b"):
    port = 8000 if platform.system() == "Windows" else 11434
    return OllamaLLM(model=f"deepseek-r1:{model_size}", base_url=f"http://localhost:{port}")
