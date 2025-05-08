import logging
from api_client import get_users, get_posts_by_user
from processor import calcular_media_caracteres
from report_generator import gerar_relatorio_excel, gerar_relatorio_pdf
from email_simulator import simular_envio_email

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Iniciando automação...")

    usuarios = get_users()
    relatorio = []

    for usuario in usuarios:
        user_id = usuario["id"]
        nome = usuario["name"]
        posts = get_posts_by_user(user_id)
        media = calcular_media_caracteres(posts)

        relatorio.append({
            "ID do Usuário": user_id,
            "Nome do Usuário": nome,
            "Quantidade de Posts": len(posts),
            "Média de Caracteres dos Posts": round(media, 2)
        })

    # Geração do Excel
    caminho = gerar_relatorio_excel(relatorio)
    logging.info(f"Relatório gerado em: {caminho}")

    # Pergunta se deseja gerar PDF
    escolha = input("Deseja gerar o relatório em PDF também?\n1 - Sim\n2 - Não\nEscolha: ")
    if escolha.strip() == "1":
        caminho_pdf = gerar_relatorio_pdf(relatorio)
        logging.info(f"Relatório PDF gerado em: {caminho_pdf}")
    else:
        logging.info("PDF não foi gerado.")

    # Simulação de envio
    sucesso = simular_envio_email(caminho)
    if sucesso:
        logging.info("Simulação de envio realizada com sucesso.")
    else:
        logging.warning("Falha na simulação de envio.")

if __name__ == "__main__":
    main()
