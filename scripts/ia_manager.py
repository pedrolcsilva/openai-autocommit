import openai

class IaManager :
    def __init__(self, config) :
        #self.url = config.ia_url()
        self.api_key = config.get_ia_api_key()
        self.messages = [{"role": "system", "content": "You are a helpful assistant. \
                You are made to generate commit for github messages based on the \
                code made that was added in the commit. \
                For that, you must use the github Conventional Commits rules. \
                You must b every clear with the user, and only print the commit message and nothing more."}]
        self.client = openai    
    def chat(self, message=""):
        chat_message = { "role": "user", "content": message}
        self.messages.append(chat_message)
    
        api_response = self.client.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=self.messages,
        api_key=self.api_key
        )

        return api_response.choices[0].message.content