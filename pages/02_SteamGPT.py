import streamlit as st

from langchain.agents import Agent, AgentType, initialize_agent, AgentExecutor
from langchain.agents.agent_toolkits.steam.toolkit import SteamToolkit
from langchain.chat_models import ChatOpenAI
from langchain.utilities.steam import SteamWebAPIWrapper
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools.render import format_tool_to_openai_function
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain_community.tools.steam.prompt import (
        STEAM_GET_GAMES_DETAILS,
        STEAM_GET_RECOMMENDED_GAMES,
    )


# Set up the page config
st.set_page_config(page_title="SteamGPT", page_icon=":game:")

# Initialize the LLM and Steam API wrapper
llm = ChatOpenAI(temperature=0.1)
Steam = SteamWebAPIWrapper()
toolkit = SteamToolkit.from_steam_api_wrapper(Steam)

agent = initialize_agent(toolkit.get_tools(), llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)



# # Streamlit input widget for game name
game_name = st.text_input("Enter the name of a game:", "Terraria")  # Default value is 'Terraria'

# # Use the user input for querying
response = agent(f"can you give information about the game {game_name}")
response



# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             STEAM_GET_RECOMMENDED_GAMES,
#         ),
#         ("user", "{input}"),
#         MessagesPlaceholder(variable_name="agent_scratchpad"),
#     ]
# )
# llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in toolkit.get_tools()])

# agent = (
#     {
#         "input": lambda x: x["input"],
#         "agent_scratchpad": lambda x: format_to_openai_function_messages(
#             x["intermediate_steps"]
#         ),
#     }
#     | prompt
#     | llm_with_tools
#     | OpenAIFunctionsAgentOutputParser()
# )
# agent.invoke({"input": "can you give information about the game Terraria", "intermediate_steps": []})


