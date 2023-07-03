import openai
from data.secret import OPENAI_KEY
from langchain.llms import OpenAI

class Template():
    def __init__(self, vacancy, me):
        self.vacancy = vacancy
        self.me = me
        self.essSkills = """experienced in python, SQL, Node.js and REST API, software engineering, teamwork"""
        
    def matchingTemplate(self):
        temp = f"""Return only bullet points that match between vacancy description and my information
                Information about job vacancy:
                '{self.vacancy}'
                Information about me:
                '{self.me}'"""
        return temp
    
    def entryTemplate(self, matchingSkills):
        temp = f"""Using bullet points above and additional information below, generate 50 word entry to my CV:
                {self.essSkills}
                {matchingSkills}"""
        return temp
    
def question(info, model):

  openai.api_key =  OPENAI_KEY

  response = openai.ChatCompletion.create(
    model=model,
    messages=[
      {"role": "user", "content": info}
    ],
    temperature=1,
  )

  return response.choices[0].message.content