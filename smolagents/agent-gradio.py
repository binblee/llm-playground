# Core smolagents imports
from smolagents import CodeAgent, OpenAIServerModel, DuckDuckGoSearchTool, load_tool, GradioUI

# For DASHSCOPE/OpenAI-compatible API
from openai import OpenAI

# Environment and utilities
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


model = OpenAIServerModel(
    model_id="qwen2.5-coder-32b-instruct",
    api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=os.environ["DASHSCOPE_API_KEY"],
)    


# Import tool from Hub
image_generation_tool = load_tool("m-ric/text-to-image", trust_remote_code=True)

tools = [
    DuckDuckGoSearchTool(),
    image_generation_tool
]

agent = CodeAgent(
    tools=tools,
    model=model
)


GradioUI(agent).launch()
