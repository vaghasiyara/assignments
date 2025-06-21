from fpdf import FPDF
from datetime import datetime

def export_result_to_pdf(text: str, score: str, student_name: str = "Student") -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_text_color(0, 0, 128)
    pdf.cell(200, 10, txt="Assignment Evaluation Report", ln=True, align='C')
    pdf.set_text_color(0, 0, 0)

    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {student_name}", ln=True)
    pdf.cell(200, 10, txt=f"Score: {score}", ln=True)
    pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"Extracted Text:\n{text}")

    output_path = f"backend/app/static/{student_name.replace(' ', '_')}_result.pdf"
    pdf.output(output_path)
    return output_path
