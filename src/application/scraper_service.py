from src.infrastructure.web_crawler import WebCrawler
from src.infrastructure.langchain_reformatter import LangchainReformatter
from src.domain.models import ScraperInput, ScraperOutput


class ScraperService:
    def __init__(self):
        self.web_scrapper = WebCrawler()
        self.reformatter = LangchainReformatter()
    
    async def scrape(self, input_data: ScraperInput) -> ScraperOutput:
        raw_content = await self.web_scrapper.fetch_content(input_data)
        # enhanced_content = await self.reformatter.reformat_content(raw_content)
        return raw_content
