### NON AI METHODS

def estimateSimpleReply(s, model):
    '''
    Estimates price of  asking simple question 
    to one of these models and tokens
    ============================================
    INPUT:
    s       -   str.
    model   -   str. name of model used
    ============================================
    OUTPUT:
    tuple.  -   (no. of tokens, estimated cost)
    '''
    tokens = int(len(s)/4)
    match model:
        case 'gpt-3.5-turbo':
            price = 0.0015/1000
        case 'gpt-4':
            price = 0.03/1000
        case 'text-davinci-003':
            price = 0.02/1000
        case 'text-ada-001':
            price = 0.0004/1000
    return (tokens, tokens*price) 

def loadData():
    '''
    Loads data about vacancy and me from local txt files
    OUTPUT:
    vacancyContent  -   str.
    meContent       -   str.
    '''
    vacancy = open('data/vacancy.txt', 'r')
    vacancyContent = vacancy.read()
    
    me = open('data/me.txt', 'r')
    meContent = me.read()
    
    return vacancyContent, meContent