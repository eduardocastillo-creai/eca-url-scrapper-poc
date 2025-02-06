from src.domain.models import PdfRequest, PdfResponse
from src.domain.pdf_service import PdfService
from src.infrastructure.weasyprint_adapter import WeasyPrintAdapter


class PdfOrchestrator:    
    def __init__(self, adapter=None):
        self.pdf_service = PdfService(adapter or WeasyPrintAdapter())

    async def generate(self, request: PdfRequest) -> PdfResponse:
        pdf_path = await self.pdf_service.generate_pdf(request)
        return PdfResponse(file_path=pdf_path)
