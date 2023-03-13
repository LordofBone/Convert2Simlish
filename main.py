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
    integrate_chatgpt_test.set_context("you are a sim from the video game, 'the sims' - whatever i type in, please "
                                       "translate it to the simlish language")

    integrate_chatgpt_test.set_text_input(text_input)

    return integrate_chatgpt_test.get_chatgpt_response()


if __name__ == "__main__":
    while True:
        text_input = input("Enter text to translate to Simlish: ")
        print(f"Simlish translation: {main(text_input)}")
