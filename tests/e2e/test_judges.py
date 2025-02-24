import os
import unittest
from oumi.judges.judge_court import oumi_v1_xml_deepseek_r1_judge
from oumi.core.configs.inference_engine_type import InferenceEngineType
from oumi.core.types.conversation import Conversation, Message, Role
from oumi.judges.oumi_judge import OumiXmlJudge as OumiJudge


class TestDeepSeekR1Judge(unittest.TestCase):
    def test_deepseek_r1_judge_config(self):

        conversations = [
            Conversation(
                messages=[
                    Message(role=Role.USER, content="What is the sum of 1 and 1 in binary?"),
                    Message(role=Role.ASSISTANT, content="The sum is 11 in binary."),
                ]
            ),
            Conversation(
                messages=[
                    Message(role=Role.USER, content="What's the capital of France?"),
                    Message(role=Role.ASSISTANT, content="French people love Paris!"),
                ]
            ),
        ]

        # Get the judge configuration
        config = oumi_v1_xml_deepseek_r1_judge()
        judge = OumiJudge(config)
        judge_output = judge.judge(conversations)

        # Print the results
        print(judge_output)

if __name__ == '__main__':
    unittest.main()
