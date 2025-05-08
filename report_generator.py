import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def _proximo_nome_disponivel(pasta, prefixo, extensao):
    """Retorna um nome de arquivo disponível no formato prefixo (n).extensao"""
    n = 1
    while True:
        nome = f"{prefixo} ({n}).{extensao}"
        caminho = os.path.join(pasta, nome)
        if not os.path.exists(caminho):
            return caminho
        n += 1

def gerar_relatorio_excel(relatorio, pasta="relatórios", prefixo="relatorio"):
    os.makedirs(pasta, exist_ok=True)
    caminho = _proximo_nome_disponivel(pasta, prefixo, "xlsx")
    df = pd.DataFrame(relatorio)
    df.to_excel(caminho, index=False)
    return caminho

def gerar_relatorio_pdf(relatorio, pasta="relatórios", prefixo="relatorio"):
    os.makedirs(pasta, exist_ok=True)
    caminho_pdf = _proximo_nome_disponivel(pasta, prefixo, "pdf")
    c = canvas.Canvas(caminho_pdf, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 50, "Relatório de Média de Caracteres por Usuário")

    c.setFont("Helvetica", 10)
    y = height - 100

    for item in relatorio:
        linha = (
            f"Usuário: {item['Nome do Usuário']} | "
            f"Posts: {item['Quantidade de Posts']} | "
            f"Média de Caracteres: {item['Média de Caracteres dos Posts']:.2f}"
        )
        c.drawString(50, y, linha)
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    return caminho_pdf
