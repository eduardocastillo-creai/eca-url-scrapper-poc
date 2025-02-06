from src.domain.models import PdfRequest
import asyncio

class PdfService:
    def __init__(self, adapter):
        self.adapter = adapter

    async def generate_pdf(self, request: PdfRequest) -> str:
        loop = asyncio.get_running_loop()

        pdf_path = await loop.run_in_executor(None, lambda: self.adapter.convert_html_to_pdf(request.content, request.output_path))

        if not pdf_path:
            raise ValueError("PDF generation failed, received None")

        return pdf_path
