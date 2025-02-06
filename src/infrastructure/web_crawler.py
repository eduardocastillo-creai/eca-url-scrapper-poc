from crawl4ai import AsyncWebCrawler, CacheMode
from src.domain.models import ScraperInput, ScraperOutput


class WebCrawler:
    @staticmethod
    async def fetch_content(input_data: ScraperInput) -> ScraperOutput:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(
                url=input_data.url,
                cache_mode=CacheMode.BYPASS,
                pdf=False,
                screenshot=False)
            
            content = result.markdown if input_data.format == "markdown" else result.cleaned_html
            return ScraperOutput(content=content, format=input_data.format)
