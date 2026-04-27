import os
from utils.logger_handler import logger
from langchain_core.tools import tool
from rag.rag_service import RagSummarizeService
import random
from utils.config_handler import agent_conf
from utils.path_tool import get_abs_path
from langchain_ollama import OllamaEmbeddings
rag = RagSummarizeService()

user_ids = ["1001", "1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009", "1010",]
month_arr = ["2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06",
             "2025-07", "2025-08", "2025-09", "2025-10", "2025-11", "2025-12", ]

external_data = {}


@tool(description="Retrieving references from vector storage")
def rag_summarize(query: str) -> str:
    return rag.rag_summarize(query)


@tool(description="Get the weather for a specified city and return it as a message string.")
def get_weather(city: str) -> str:
    return f"{city} weather is sunny with a temperature of 26 degrees Celsius, humidity of 50%, a southerly wind of level 1, and an AQI of 21. The probability of rain in the next 6 hours is extremely low."


@tool(description="Retrieve the name of the user's city and return it as a plain string.")
def get_user_location() -> str:
    return random.choice(["Stockholm", "Paris", "Uppsala"])


@tool(description="Get the user's ID and return it as a plain string.")
def get_user_id() -> str:
    return random.choice(user_ids)


@tool(description="Get the current month and return it as a plain string")
def get_current_month() -> str:
    return random.choice(month_arr)


def generate_external_data():
    """
    {
        "user_id": {
            "month" : {"特征": xxx, "效率": xxx, ...}
            "month" : {"特征": xxx, "效率": xxx, ...}
            "month" : {"特征": xxx, "效率": xxx, ...}
            ...
        },
        "user_id": {
            "month" : {"特征": xxx, "效率": xxx, ...}
            "month" : {"特征": xxx, "效率": xxx, ...}
            "month" : {"特征": xxx, "效率": xxx, ...}
            ...
        },
        "user_id": {
            "month" : {"特征": xxx, "效率": xxx, ...}
            "month" : {"特征": xxx, "效率": xxx, ...}
            "month" : {"特征": xxx, "效率": xxx, ...}
            ...
        },
        ...
    }
    :return:
    """
    if not external_data:
        external_data_path = get_abs_path(agent_conf["external_data_path"])

        if not os.path.exists(external_data_path):
            raise FileNotFoundError(f"external data file{external_data_path}didn't exist")

        with open(external_data_path, "r", encoding="utf-8") as f:
            for line in f.readlines()[1:]:
                arr: list[str] = line.strip().split(",")

                user_id: str = arr[0].replace('"', "")
                feature: str = arr[1].replace('"', "")
                efficiency: str = arr[2].replace('"', "")
                consumables: str = arr[3].replace('"', "")
                comparison: str = arr[4].replace('"', "")
                time: str = arr[5].replace('"', "")

                if user_id not in external_data:
                    external_data[user_id] = {}

                external_data[user_id][time] = {
                    "特征": feature,
                    "效率": efficiency,
                    "耗材": consumables,
                    "对比": comparison,
                }


@tool(description="Retrieves the usage records of a specified user for a specified month from an external system and returns them as a plain string. If no records are found, an empty string is returned.")
def fetch_external_data(user_id: str, month: str) -> str:
    generate_external_data()

    try:
        return external_data[user_id][month]
    except KeyError:
        logger.warning(f"[fetch_external_data]User not found:Usage record data for {user_id}in{month}")
        return ""


@tool(description="With no input parameters and no return value, the call triggers middleware to automatically and dynamically inject context information into the scene where the report is generated, providing context information for subsequent prompt word switching.")
def fill_context_for_report():
    return "fill_context_for_report has been called."
