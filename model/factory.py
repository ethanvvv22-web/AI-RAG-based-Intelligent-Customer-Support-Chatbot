# from abc import ABC, abstractmethod
# from typing import Optional
# from langchain_core.embeddings import Embeddings
# from langchain_community.chat_models.tongyi import BaseChatModel
# from langchain_community.embeddings import DashScopeEmbeddings
# from langchain_community.chat_models.tongyi import ChatTongyi
# from utils.config_handler import rag_conf
#
#
# class BaseModelFactory(ABC):
#     @abstractmethod
#     def generator(self) -> Optional[Embeddings | BaseChatModel]:
#         pass
#
#
# class ChatModelFactory(BaseModelFactory):
#     def generator(self) -> Optional[Embeddings | BaseChatModel]:
#         return ChatTongyi(model=rag_conf["chat_model_name"])
#
#
# class EmbeddingsFactory(BaseModelFactory):
#     def generator(self) -> Optional[Embeddings | BaseChatModel]:
#         return DashScopeEmbeddings(model=rag_conf["embedding_model_name"])
#
#
# chat_model = ChatModelFactory().generator()
# embed_model = EmbeddingsFactory().generator()
# from abc import ABC,abstractmethod
# from typing import Optional
#
# from langchain_community.chat_models import ChatOpenAI
# from langchain_community.embeddings import OpenAIEmbeddings
#
# from langchain_ollama import ChatOllama, OllamaEmbeddings
#
# from langchain_core.embeddings import Embeddings
# from langchain_core.language_models import BaseChatModel
# from langchain_openai import OpenAI
#
# from utils.config_handler import rag_conf
#
#
# class BaseModelFactory(ABC):
#     @abstractmethod
#     def generator(self):
#         pass
#
#
# # -------------------------
# # 聊天模型：第三方 aihubmix
# # -------------------------
# from openai import OpenAI
#
# class ChatModelFactory(BaseModelFactory):
#     def generator(self):
#         return OpenAI(
#             api_key="sk-PitMTBNUeDTfTWLL6b36Ab12Ad0f44A4A26858D5F1B547E4",
#             base_url="https://aihubmix.com/v1"
#         )
#
# # -------------------------
# # Embedding：本地 nomic-embed-text
# # -------------------------
# class EmbeddingsModelFactory(BaseModelFactory):
#     def generator(self):
#         return OllamaEmbeddings(model="nomic-embed-text")
#
#
# # -------------------------
# # 实例化模型
# # -------------------------
# chat_client = ChatModelFactory().generator()
# embed_model = EmbeddingsModelFactory().generator()
#
#
# # -------------------------
# # 发送聊天请求（正确位置）
# # -------------------------
# response = chat_client.completions.create(
#     model="gpt-4o-free",   # 必须是 aihubmix 支持的模型名
#     messages=[{"role": "user", "content": "你好"}]
# )
#
# print(response.choices[0].message["content"])

# from abc import ABC, abstractmethod
# from langchain_ollama import OllamaEmbeddings
# from langchain_core.embeddings import Embeddings
# from openai import OpenAI  # 只保留官方 SDK 的 OpenAI
# from langchain_openai import ChatOpenAI
#
# class BaseModelFactory(ABC):
#     @abstractmethod
#     def generator(self):
#         pass
#
#
# # -------------------------
# # 聊天模型：第三方 aihubmix
# # -------------------------
#
# class ChatModelFactory(BaseModelFactory):
#     def generator(self):
#         return ChatOpenAI(
#             api_key="sk-PitMTBNUeDTfTWLL6b36Ab12Ad0f44A4A26858D5F1B547E4",
#             base_url="https://aihubmix.com/v1",
#             model="gpt-oss-20b"  # 换成你账号可用的模型
#         )
# # -------------------------
# # Embedding：本地 nomic-embed-text
# # -------------------------
# class EmbeddingsModelFactory(BaseModelFactory):
#     def generator(self):
#         return OllamaEmbeddings(model="nomic-embed-text")
#
#
# # -------------------------
# # 实例化模型
# # -------------------------
# chat_client = ChatModelFactory().generator()
# embed_model = EmbeddingsModelFactory().generator()
#
# chat_model = chat_client
# # -------------------------
# # 发送聊天请求
# # -------------------------
# response = chat_client.chat.completions.create(  # 注意：chat.completions
#     model="kimi-for-coding-free",
#     messages=[{"role": "user", "content": "你好"}]
# )
#
# print(response.choices[0].message.content)

# if __name__ == "__main__":
#     response = chat_client.chat.completions.create(
#         model="kimi-for-coding-free",
#         messages=[{"role": "user", "content": "你好"}]
#     )
#     print(response.choices[0].message.content)

from abc import ABC, abstractmethod
from langchain_ollama import OllamaEmbeddings
from openai import OpenAI
from langchain_openai import ChatOpenAI

API_KEY = "sk-PitMTBNUeDTfTWLL6b36Ab12Ad0f44A4A26858D5F1B547E4"
BASE_URL = "https://aihubmix.com/v1"
MODEL = "kimi-for-coding-free"


class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self):
        pass


# -------------------------
# LangChain 管道用（chain | 语法）
# -------------------------
class ChatModelFactory(BaseModelFactory):
    def generator(self):
        return ChatOpenAI(
            api_key=API_KEY,
            base_url=BASE_URL,
            model=MODEL
        )


# -------------------------
# 原生 API 调用用（.chat.completions.create）
# -------------------------
class RawChatClientFactory(BaseModelFactory):
    def generator(self):
        return OpenAI(
            api_key=API_KEY,
            base_url=BASE_URL
        )


# -------------------------
# Embedding：本地 nomic-embed-text
# -------------------------
class EmbeddingsModelFactory(BaseModelFactory):
    def generator(self):
        return OllamaEmbeddings(model="nomic-embed-text")


# -------------------------
# 实例化模型
# -------------------------
chat_model = ChatModelFactory().generator()       # LangChain 管道专用
chat_client = RawChatClientFactory().generator()  # 原生调用专用
embed_model = EmbeddingsModelFactory().generator()


# -------------------------
# 测试（仅直接运行此文件时执行）
# -------------------------
if __name__ == "__main__":
    response = chat_client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": "你好"}]
    )
    print(response.choices[0].message.content)