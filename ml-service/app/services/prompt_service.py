import joblib
class PromptService:
    #Day 3
    def __init__(self):
        self.model = joblib.load("ml/prompt_quality_model.joblib")

    #Day2
    def process_prompt(self, prompt:str)->str:
        return f"Recieved prompt: {prompt}"

    def score_prompt(self, prompt:str)->str:
        # Day 2
        # length = len(prompt.strip())
        # if length < 20:
        #     return "Low Quality"
        # elif length < 100:
        #     return "Medium Quality"
        # else :
        #     return "High Quality"

        #Day3
        prediction = self.model.predict([prompt])
        return prediction[0]