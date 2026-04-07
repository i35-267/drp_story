#!/usr/bin/env python3
"""Render selected pages from GitClear 'Coding on Copilot' PDF to PNG (print ~220dpi).

デフォルトの PDF パスは Cursor の workspaceStorage 内。環境に合わせて
GITCLEAR_CODING_ON_COPILOT_PDF を上書きしてください。
"""
from pathlib import Path
import os

import fitz  # PyMuPDF

# 0-based indices: p.8 割合表, p.9 グラフ, p.10 YoY 表
PAGES = [
    (7, "gitclear_2024_commit_line_percentages.png"),
    (8, "gitclear_2024_commit_line_chart.png"),
    (9, "gitclear_2024_yoy_operation_changes.png"),
]

ZOOM = 220 / 72  # ~220 dpi


def main() -> None:
    pdf = os.environ.get(
        "GITCLEAR_CODING_ON_COPILOT_PDF",
        str(
            Path.home()
            / "Library/Application Support/Cursor/User/workspaceStorage/4ff3ddbf242b70ef974b2a9cf4867982/pdfs/3dca4345-5c58-444f-97e2-6a0b724cccf2/GitClear-Coding-on-Copilot-2024-Developer-Research.pdf"
        ),
    )
    out_dir = Path(__file__).resolve().parent / "assets"
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf)
    mat = fitz.Matrix(ZOOM, ZOOM)
    try:
        for page_index, filename in PAGES:
            page = doc.load_page(page_index)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            out_path = out_dir / filename
            pix.save(str(out_path))
            print(out_path)
    finally:
        doc.close()


if __name__ == "__main__":
    main()
