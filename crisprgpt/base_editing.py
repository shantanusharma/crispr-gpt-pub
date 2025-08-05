from .logic import BaseState, Result_ProcessUserInput, BaseUserInputState
 
from util import get_logger

logger = get_logger(__name__)

ERROR_MESSAGE="CRISPR-GPT-Lite does not support this function. "

class StateError(BaseState):
    request_user_input = False

    @classmethod
    def step(cls, user_message, **kwargs):
        return Result_ProcessUserInput(response=ERROR_MESSAGE), None