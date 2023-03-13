import sys
import os

chatting_gpt_dir = os.path.join("ChattingGPT")

sys.path.append(chatting_gpt_dir)

from ChattingGPT.integrate_chatgpt import IntegrateChatGPT

integrate_chatgpt_test = IntegrateChatGPT()


def main(text_input):
    """
    Main function for running translations.
    :return:
    """
    integrate_chatgpt_test.set_context("you are a sim from the game, 'the sims' - whatever i type in in english, "
                                       "please translate to simlish")

    integrate_chatgpt_test.set_text_input(text_input)

    return integrate_chatgpt_test.get_chatgpt_response()


if __name__ == "__main__":
    print(main("hello how are you today, would you like to go into old town"))
