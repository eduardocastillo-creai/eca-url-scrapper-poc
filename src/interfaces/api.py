from fastapi import APIRouter
from src.application.scraper_service import ScraperService
from src.application.pdf_orchestrator import PdfOrchestrator
from src.domain.models import ScraperInput, ScraperOutput, PdfRequest, PdfResponse
from src.infrastructure.weasyprint_adapter import WeasyPrintAdapter


router = APIRouter()
scraper_service = ScraperService()
pdf_generator = PdfOrchestrator(adapter=WeasyPrintAdapter())


@router.post("/scrape", response_model=ScraperOutput)
async def scrape(input_data: ScraperInput):
    return await scraper_service.scrape(input_data)

@router.post("/generate-pdf", response_model=PdfResponse)
async def generate_pdf(input_data: PdfRequest):
    return await pdf_generator.generate(input_data)
