import google.generativeai as genai

class GeminiService:
    def __init__(self, project_number, project_name, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def send_prompt(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text