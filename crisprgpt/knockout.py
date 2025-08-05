from .logic import BaseState, Result_ProcessUserInput, BaseUserInputState
from llm import OpenAIChat
from .knockout_constant import *
from .off_target import OffTarget
from .knockout_sgRNA_selection import SgRNASelection
import numpy
import re
import requests
import os
from util import get_logger

logger = get_logger(__name__)


class StateEntry(BaseState):
    request_user_input = False

    @classmethod
    def step(cls, user_message, **kwargs):
        return Result_ProcessUserInput(response=PROMPT_REQUEST_ENTRY), None


class StateStep1(BaseState):
    @classmethod
    def step(cls, user_message, **kwargs):
        return Result_ProcessUserInput(response=PROMPT_STEP1), StateStep1Inquiry


class StateStep1Inquiry(BaseUserInputState):
    prompt_process = PROMPT_PROCESS_STEP1_INQUIRY
    request_message = PROMPT_REQUEST_STEP1_INQUIRY

    @classmethod
    def step(cls, user_message, **kwargs):
        prompt = cls.prompt_process.format(user_message=user_message)
        response = OpenAIChat.chat(prompt, use_GPT4=True)
        text_response = str(response)
        result = response["Answer"]
        text_response += f" Final Result {result}"
        return (
            Result_ProcessUserInput(
                status="success",
                thoughts=response["Thoughts"],
                result=result,
                response=text_response,
            ),
            None,
        )



class StateStep1Easy(BaseUserInputState):
    prompt_process = PROMPT_PROCESS_EASY
    request_message = PROMPT_REQUEST_EASY

    @classmethod
    def step(cls, user_message, **kwargs):
        prompt = cls.prompt_process.format(user_message=user_message)
        response = OpenAIChat.chat(prompt)
        text_response = str(response)
        result = response["Answer"]
        text_response += f" Final Result {result}"
        return (
            Result_ProcessUserInput(
                status="success",
                thoughts=response["Thoughts"],
                result=result,
                response=text_response,
            ),
            StateStep3,
        )


class StateStep3(BaseState):
    @classmethod
    def step(cls, user_message, **kwargs):
        if kwargs["is_automation"]:
            if "StateStep1Easy" in kwargs["memory"]:
                return Result_ProcessUserInput(), SgRNASelection
            else:
                return (
                    Result_ProcessUserInput(response=PROMPT_REQUEST_STEP3),
                    StateStep1Easy,
                )
        else:
            return (
                Result_ProcessUserInput(response=PROMPT_REQUEST_STEP3),
                SgRNASelection,
            )

 