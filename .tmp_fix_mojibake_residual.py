from pathlib import Path

files = [
    Path(r"content/complementarias/complementaria_markov_i.ipynb"),
    Path(r"content/complementarias/complementaria_markov_ii.ipynb"),
]

replacements = {
    "DimensiÃ³n": "Dimensión",
    "Ã—": "×",
    "â‰ˆ": "≈",
    "Î»â‚": "λ₁",
    "DistribuciÃ³n": "Distribución",
    "â€”": "—",
    "â†’": "→",
    "âˆž": "∞",
}

for path in files:
    text = path.read_text(encoding="utf-8")
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    path.write_text(text, encoding="utf-8")

print("ok")
