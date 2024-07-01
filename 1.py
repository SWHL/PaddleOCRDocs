from pathlib import Path

file_dir = Path("docs/algorithm/text_recognition")
md_files = list(file_dir.glob("*_en.md"))
print(md_files)

for md_path in md_files:
    new_md_path = str(md_path).replace("_en.md", ".en.md")
    print(new_md_path)
    md_path.rename(new_md_path)
