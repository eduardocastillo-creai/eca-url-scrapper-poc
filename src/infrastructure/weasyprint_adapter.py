import os
from weasyprint import HTML

class WeasyPrintAdapter:
    def convert_html_to_pdf(self, html_content: str, output_path: str) -> str:
        
        if not os.path.dirname(output_path):
            output_path = os.path.join("output", output_path)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        HTML(string=html_content).write_pdf(output_path)

        if not os.path.exists(output_path):
            raise RuntimeError(f"Failed to generate PDF: {output_path}")

        return output_path
