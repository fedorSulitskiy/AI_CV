import openai
from data.secret import OPENAI_KEY
from langchain.llms import OpenAI
import methods.non_ai_methods as nm
import methods.ai_methods as am
model = 'gpt-3.5-turbo'

# Prepare prompt
v, m = nm.loadData()
temp = am.Template(vacancy=v, me=m)
prompt1 = temp.matchingTemplate()
# Get matching skills
reply1 = am.question(prompt1,model)
print("Matching Skills:\n",reply1)
print('\n')
# Get the custom intro
prompt2 = temp.entryTemplate(reply1)
reply2 = am.question(prompt2,model)
print("Entry\n",reply2)