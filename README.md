# Automated File Organizer

A backend script using Python's `os` and `shutil` libraries to automatically categorize and move files into specific folders based on their extensions. Point it at any directory and it handles the rest — no manual sorting required.

---

## How It Works

The script scans a target directory, reads each file's extension, and moves it into a matching category subfolder. If the destination folder doesn't exist yet, it creates it on the fly. Files with unrecognized extensions are logged and left in place.

---

## File Categories

| Folder | Extensions |
|--------|-----------|
| `Imagens` | `.jpg` `.jpeg` `.png` `.gif` `.bmp` |
| `Documentos` | `.pdf` `.docx` `.txt` `.xlsx` `.pptx` |
| `Arquivos_Compactados` | `.zip` `.rar` `.7z` |
| `Instaladores` | `.exe` `.msi` |
| `Videos` | `.mp4` `.mkv` `.mov` |
| `Musicas` | `.mp3` `.wav` |

---

## Built With

| Technology | Role |
|------------|------|
| Python | Core scripting language |
| `os` | Directory traversal, path handling, and folder creation |
| `shutil` | File movement across the filesystem |

---

## Project Structure

```
/
└── organizer.py      # Main script with extension map and organizer logic
```

---

## Getting Started

No external dependencies — runs on the Python standard library.

**1. Set your target directory**

Open `organizer.py` and update the target path on the last line:

```python
diretorio_alvo = "./your-folder-here"
```

**2. Run the script**

```bash
python organizer.py
```

The script will print a log of every file moved and flag anything it couldn't categorize.

---

## Example Output

```
Movido: photo.jpg -> Imagens
Movido: report.pdf -> Documentos
Movido: archive.zip -> Arquivos_Compactados
Ignorado (Sem categoria): notes.md
```

Thank you for your attention!