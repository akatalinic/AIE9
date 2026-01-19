import os
from typing import List
import pypdf


class TextFileLoader:
    def __init__(self, path: str, encoding: str = "utf-8"):
        self.documents = []
        self.path = path
        self.encoding = encoding

    def load(self):
        if os.path.isdir(self.path):
            self.load_directory()
        elif self.path.lower().endswith(".txt"):
            self.load_file(self.path)
        elif self.path.lower().endswith(".pdf"):
            self.load_pdf(self.path)
        else:
            raise ValueError(
                f"Provided path '{self.path}' is neither a valid directory nor a .txt/.pdf file. "
                f"File exists: {os.path.isfile(self.path) if os.path.exists(self.path) else False}"
            )

    def load_file(self, path: str):
        with open(path, "r", encoding=self.encoding) as f:
            self.documents.append(f.read())

    def load_pdf(self, path: str):
        try:
            reader = pypdf.PdfReader(path)
        except Exception as e:
            print(f"Error loading PDF: {e}")
            return

        if reader.is_encrypted:
            print("Skipping encrypted PDF")
            return
        
        pdf_text = []
        for page_index, page in enumerate(reader.pages):
            try:
                text = page.extract_text()
                if text and text.strip():
                    pdf_text.append(text)
            except Exception as e:
                print(f"Skipping page {page_index}: {e}")

        if pdf_text:
            self.documents.append("\n".join(pdf_text))

            

    def load_directory(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                full_path = os.path.join(root, file)
                if file.lower().endswith(".txt"):
                   self.load_file(full_path)
                elif file.lower().endswith(".pdf"):
                   self.load_pdf(full_path)
                              
    def load_documents(self):
        self.load()
        return self.documents


class CharacterTextSplitter:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        assert (
            chunk_size > chunk_overlap
        ), "Chunk size must be greater than chunk overlap"

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str) -> List[str]:
        chunks = []
        for i in range(0, len(text), self.chunk_size - self.chunk_overlap):
            chunks.append(text[i : i + self.chunk_size])
        return chunks

    def split_texts(self, texts: List[str]) -> List[str]:
        chunks = []
        for text in texts:
            chunks.extend(self.split(text))
        return chunks


if __name__ == "__main__":
    loader = TextFileLoader("data/KingLear.txt")
    loader.load()
    splitter = CharacterTextSplitter()
    chunks = splitter.split_texts(loader.documents)
    print(len(chunks))
    print(chunks[0])
    print("--------")
    print(chunks[1])
    print("--------")
    print(chunks[-2])
    print("--------")
    print(chunks[-1])
