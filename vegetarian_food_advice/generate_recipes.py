import os
from dotenv import load_dotenv
#from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, OpenAI, LLMChain
from langchain.chains import SimpleSequentialChain

load_dotenv()

OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def generate_response(txt):
    template = """
    Suppose you're a nutritionist and I need you to give me adivice for my diet.
    I give you and ingredients I have available and you suggest a menu.
    menu: Suggest the menu for a full day. Include breakfast, lunch, and dinner.
    shopping list: List the ingredients I need to buy but don't include the ones I already have.

    If you can't generate a valid menu, just output null.

    Format the output as JSON with the following keys:
    menu
    shopping list

    text: {input}
    """

    llm = OpenAI(temperature=0)
    prompt_template = PromptTemplate.from_template(template=template)
    chain = LLMChain(llm=llm, prompt=prompt_template)
    
    response_template = """
    You are a helpful cheff that gives me the best recipes to cook the menu that the nutritionist gave me.
    You will get a menu for a full day that includes breakfast, lunch and dinner and a shopping list for ingredients that 
    I don't have. Give me the recipes for the menu.

    text:{input}
    """
    recipes_template = PromptTemplate(input_variables=['input'], template=response_template)
    recipes_chain = LLMChain(llm=llm, prompt=recipes_template)
    
    overall_chain = SimpleSequentialChain(chains=[chain, recipes_chain], verbose=True)
    #overall_chain.run(input="eggs, beef, banana, apples, garlic")
    
    return overall_chain.run(input=txt)