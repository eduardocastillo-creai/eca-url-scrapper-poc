from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from src.domain.models import ScraperOutput
import re


class LangchainReformatter:
    def __init__(self, model_name: str = "gpt-4o"):
        self.llm = ChatOpenAI(model=model_name)

    async def reformat_content(self, content: ScraperOutput) -> ScraperOutput:
        """Formats Markdown/HTML content while keeping all text unchanged."""
        format_type = "Markdown" if content.format == "markdown" else "HTML"

        prompt = f"""
        You are a **document formatting expert** specializing in structuring text, html and markdown for **professional PDF reports**.  
        Your task is to **ONLY remove special characters on text** while ensuring **ALL original text remains unchanged**.

        ---
        ### **🛠️ Formatting Output Rules**
        - **Output must be in `{format_type}` format**.
        - **Do not add prefixes.
        - **Only return the formatted cleaned content without extra comments**.

        ---
        ### **📜 Content to Format (DO NOT CHANGE THE TEXT, JUST CLEAN IT FROM SPECIAL CHARACTERS)**
        ```
        {content.content}
        ```
        ---
        """

        messages = [HumanMessage(content=prompt)]
        response = await self.llm.ainvoke(messages)
        formatted_content = response.content if isinstance(response, AIMessage) else str(response)

        return ScraperOutput(content=formatted_content.strip(), format=content.format)
