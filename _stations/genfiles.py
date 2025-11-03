import yaml
from pathlib import Path

# === Настройки ===
INPUT_FILE = "data.yml"       # входной YAML

# === Основной код ===
def main():

    # читаем YAML
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # обрабатываем каждый верхний ключ
    for name, content in data.items():
        # создаём текст frontmatter
        frontmatter_lines = ["---"]
        for key, value in content.items():
            # аккуратно форматируем строки с кавычками
            frontmatter_lines.append(f'{key}: "{value}"')
        frontmatter_lines.append("---\n")

        # соединяем в один текст
        frontmatter_text = "\n".join(frontmatter_lines)

        # путь к файлу
        output_path = f"{name}.md"

        # записываем файл
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(frontmatter_text)

        print(f"✅ Создан файл: {output_path}")

if __name__ == "__main__":
    main()