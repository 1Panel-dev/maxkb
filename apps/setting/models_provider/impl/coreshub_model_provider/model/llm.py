# coding=utf-8
"""
    @project: MaxKB
    @Author：Qingyang
    @file： llm.py
    @date：2025/2/11 11:32
    @desc:
"""
from typing import List, Dict

from common.config.tokenizer_manage_config import TokenizerManage
from setting.models_provider.base_model_provider import MaxKBBaseModel
from setting.models_provider.impl.base_chat_open_ai import BaseChatOpenAI


def custom_get_token_ids(text: str):
    tokenizer = TokenizerManage.get_tokenizer()
    return tokenizer.encode(text)


class CoresHubChatModel(MaxKBBaseModel, BaseChatOpenAI):

    @staticmethod
    def is_cache_model():
        return False

    @staticmethod
    def new_instance(model_type, model_name, model_credential: Dict[str, object], **model_kwargs):
        optional_params = MaxKBBaseModel.filter_optional_params(model_kwargs)
        return CoresHubChatModel(
            model=model_name,
            openai_api_base=model_credential.get('api_base'),
            openai_api_key=model_credential.get('api_key'),
            **optional_params
        )
