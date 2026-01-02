#!/bin/bash

# 第1章から第7章までをPDFに変換するスクリプト

# プロジェクトのルートディレクトリ
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

# CSSファイルのパス
CSS_FILE="${ROOT_DIR}/pdf-style.css"

# 出力ディレクトリ
OUTPUT_DIR="${ROOT_DIR}/output"
mkdir -p "${OUTPUT_DIR}"

echo "PDF生成を開始します..."
echo "CSSファイル: ${CSS_FILE}"
echo "出力ディレクトリ: ${OUTPUT_DIR}"
echo ""

# 各章を処理
for i in {1..7}; do
    CHAPTER_DIR="${ROOT_DIR}/chapter_${i}"
    MARKDOWN_FILE="${CHAPTER_DIR}/chapter_${i}.md"
    PDF_FILE="${OUTPUT_DIR}/chapter_${i}.pdf"
    
    if [ ! -f "${MARKDOWN_FILE}" ]; then
        echo "警告: ${MARKDOWN_FILE} が見つかりません。スキップします。"
        continue
    fi
    
    echo "処理中: 第${i}章..."
    echo "  入力: ${MARKDOWN_FILE}"
    echo "  出力: ${PDF_FILE}"
    
    # markdown-pdfでPDFを生成
    markdown-pdf \
        --css-path "${CSS_FILE}" \
        --paper-format A4 \
        --paper-orientation portrait \
        --paper-border "2cm" \
        "${MARKDOWN_FILE}" \
        -o "${PDF_FILE}"
    
    if [ $? -eq 0 ]; then
        echo "  ✓ 成功: ${PDF_FILE}"
    else
        echo "  ✗ 失敗: 第${i}章のPDF生成に失敗しました。"
    fi
    echo ""
done

echo "PDF生成が完了しました。"

