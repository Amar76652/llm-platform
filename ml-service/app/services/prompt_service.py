class PromptService:
    def process_prompt(self, prompt:str)->str:
        return f"Recieved prompt: {prompt}"

    def score_prompt(self, prompt:str)->str:
        length = len(prompt.strip())
        if length < 20:
            return "Low Quality"
        elif length < 100:
            return "Medium Quality"
        else :
            return "High Quality"