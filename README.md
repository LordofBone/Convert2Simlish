### What this does

This is a project that integrates with ChatGPT to convert text to Simlish (the language developed for the game 'The Sims'.

You can read more about it [here](https://www.hackster.io/314reactor/simlish-o-matic-134a8e).

### Usage

Check out this project into your code:

```git clone --recurse-submodules https://github.com/LordofBone/Convert2Simlish```

Install the requirements:

```pip install -r requirements.txt```

Head to [OpenAI](https://platform.openai.com/) and sign up, you should get some free credits for a 
limited time to use the API, then create an API key.

Copy or rename 'ChattingGPT/config/api_config_template.py' to 'config/api_config.py' and add the API key in.

And now it should be ready to go. Just run the main file:
    
```python main.py```