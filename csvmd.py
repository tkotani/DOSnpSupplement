import csv

# CSVファイルを読み込む関数
def csv_to_markdown_table(csv_file):
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Markdownのヘッダー行を作成
    header = "| " + " | ".join(rows[0]) + " |"
    separator = "| " + " | ".join(["---"] * len(rows[0])) + " |"

    # データ行を作成
    data_rows = ["| " + " | ".join(row) + " |" for row in rows[1:]]

    # 全ての行を結合
    markdown_table = "\n".join([header, separator] + data_rows)
    return markdown_table

# ファイルパスを指定してMarkdownテーブルを生成
csv_file_path = 'tab_nonmag_all.csv'  # CSVファイルのパスをここに指定
markdown_table = csv_to_markdown_table(csv_file_path)

# Markdown形式のテーブルを表示
print(markdown_table)

# 必要に応じてMarkdownテーブルをファイルに書き出す
with open('output.md', mode='w', encoding='utf-8') as output_file:
    output_file.write(markdown_table)
