import streamlit as st
import tiktoken
from loguru import logger
import os

from langchain.agents import AgentType, initialize_agent
from langchain.agents.agent_toolkits.steam.toolkit import SteamToolkit
from langchain.llms import OpenAI
from langchain.utilities.steam import SteamWebAPIWrapper

st.set_page_config(
    page_title="SteamGPT",
    page_icon=":game:"
)

os.environ["STEAM_KEY"] = "xyz"
os.environ["STEAM_ID"] = "123"
os.environ["OPENAI_API_KEY"] = "abc"

llm = OpenAI(temperature=0)
Steam = SteamWebAPIWrapper()
toolkit = SteamToolkit.from_steam_api_wrapper(Steam)
agent = initialize_agent(
    toolkit.get_tools(), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

out = agent("can you give the information about the game Terraria")
print(out)