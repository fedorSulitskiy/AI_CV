from data.secret import OPENAI_KEY
import methods.non_ai_methods as nm
import methods.ai_methods as am
model = 'gpt-3.5-turbo'


def main():
    # Prepare initial data
    v, m = nm.loadData()
    temp = am.Template(vacancy = v, me = m)
    
    # Get matching skills
    prompt1 = temp.matchingTemplate()
    reply1 = am.question(info = prompt1, model = model)
    print("Matching Skills:\n",reply1) # It will print the array of skills it believes you match.
    print('\n')                        # This serves as an indicator of how well the model understands the assignment.
    
    # Get the custom intro
    prompt2 = temp.entryTemplate(matchingSkills = reply1, noWords = 50)
    reply2 = am.question(info = prompt2, model = model)
    print("CV Entry:\n",reply2) # This outputs the final result.
    
if __name__ == '__main__':
    main()