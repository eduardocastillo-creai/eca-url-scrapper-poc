from pydantic import BaseModel


class ScraperInput(BaseModel):
    url: str
    format: str = "html"


class ScraperOutput(BaseModel):
    content: str
    format: str


class PdfRequest(BaseModel):
    content: str
    output_path: str = "output.pdf"


class PdfResponse(BaseModel):
    file_path: str
