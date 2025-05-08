def calcular_media_caracteres(posts):
    if not posts:
        return 0
    total_caracteres = sum(len(post.get("body", "")) for post in posts)
    return total_caracteres / len(posts)
