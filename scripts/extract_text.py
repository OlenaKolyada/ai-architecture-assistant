from pathlib import Path

import ebooklib
from ebooklib import epub


BOOKS_DIR = Path("books")


book_file = None

for file in BOOKS_DIR.iterdir():
    if file.suffix == ".epub":
        book_file = file
        break

if book_file is None:
    raise FileNotFoundError("No EPUB file found in books folder")

book = epub.read_epub(str(book_file))

texts = []

for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        texts.append(item.get_content().decode("utf-8"))

text = "\n".join(texts)

print(f"Book file: {book_file}")
print(f"Extracted characters: {len(text)}")
WORKSPACE_DIR = Path("workspace")
WORKSPACE_DIR.mkdir(exist_ok=True)

raw_text_file = WORKSPACE_DIR / "raw.txt"
raw_text_file.write_text(text, encoding="utf-8")

print(f"Saved to: {raw_text_file}")