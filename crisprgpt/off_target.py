import numpy
from util import get_logger

from llm import OpenAIChat
from .logic import BaseState, Result_ProcessUserInput, BaseUserInputState
from .off_target_constant import *
import json
import re
from .safety import (
    check_stopping_keywords,
)

logger = get_logger(__name__)


class OffTarget(BaseUserInputState):
    prompt_process = PROMPT_PROCESS_STEP1
    request_message = PROMPT_REQUEST_STEP1

    @classmethod
    def step(cls, user_message, **kwargs):
        prompt = cls.prompt_process.format(user_message=user_message)
        response = OpenAIChat.chat(prompt, use_GPT4=True)

        if response["Choice"] in ["1", "(1)", "1.", "(1)."]:
            result = "mismatch_only"
            text_response = RESPONSE_MISMATCH_ONLY
        elif response["Choice"] in ["2", "(2)", "2.", "(2)."]:
            result = "mismatch_bulges"
            text_response = RESPONSE_MISMATCH_BULGES
        return (
            Result_ProcessUserInput(
                status="success",
                thoughts=response["Thoughts"],
                result=result,
                response=text_response,
            ),
            None,
        )
