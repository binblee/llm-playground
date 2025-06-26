from smolagents import CodeAgent, OpenAIServerModel, GradioUI
import os
from tools import WeatherInfoTool, HubStatsTool, DuckDuckGoSearchTool
from retriever import load_guest_dataset


search_tool = DuckDuckGoSearchTool()
weather_tool = WeatherInfoTool()
hub_stats_tool = HubStatsTool()
guest_info_tool = load_guest_dataset()

model = OpenAIServerModel(
    model_id="qwen2.5-coder-32b-instruct",
    api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=os.environ["DASHSCOPE_API_KEY"],
)

alfred = CodeAgent(tools=[guest_info_tool, weather_tool, hub_stats_tool, search_tool],
                   model=model,
                   add_base_tools=True, # Add any additioinal base tools
                   planning_interval=3, # Enable planning every 3 steps
                   )

GradioUI(alfred).launch()