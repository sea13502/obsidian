#!/usr/bin/env python3
"""
PDF转图片和Markdown工具
将PDF文件拆分为图片，生成对应的Markdown文件和目录主页
"""

import os
import re
from pathlib import Path
from typing import List, Tuple, Dict
import fitz  # PyMuPDF
from PIL import Image
import io


class PDFToMarkdownConverter:
    """PDF转Markdown转换器"""

    def __init__(self, pdf_path: str, dpi: int = 150):
        """
        初始化转换器

        Args:
            pdf_path: PDF文件路径
            dpi: 图片分辨率，默认150
        """
        self.pdf_path = Path(pdf_path)
        self.dpi = dpi
        self.pdf_name = self.pdf_path.stem
        self.base_folder = self.pdf_path.parent / self.pdf_name
        self.images_folder = self.base_folder / "images"
        self.markdown_folder = self.base_folder / "markdown"

        # 创建文件夹
        self._create_folders()

    def _create_folders(self):
        """创建所需的文件夹结构"""
        self.base_folder.mkdir(exist_ok=True)
        self.images_folder.mkdir(exist_ok=True)
        self.markdown_folder.mkdir(exist_ok=True)
        print(f"✓ 创建文件夹结构: {self.base_folder}")

    def pdf_to_images(self) -> List[str]:
        """
        将PDF转换为图片

        Returns:
            生成的图片文件路径列表
        """
        print(f"正在转换PDF到图片: {self.pdf_path}")
        doc = fitz.open(self.pdf_path)
        image_paths = []

        total_pages = len(doc)
        for page_num in range(total_pages):
            page = doc[page_num]
            zoom = self.dpi / 72  # 72是PDF的默认DPI
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)

            # 生成图片文件名: machinelearning_concept_page_001.jpg
            image_filename = f"{self.pdf_name}_page_{page_num + 1:03d}.jpg"
            image_path = self.images_folder / image_filename

            pix.save(str(image_path))
            image_paths.append(str(image_path))

            # 显示进度
            if (page_num + 1) % 50 == 0 or page_num == 0 or page_num == total_pages - 1:
                print(f"  进度: {page_num + 1}/{total_pages} 页")

        doc.close()
        print(f"✓ 完成! 共生成 {len(image_paths)} 张图片")
        return image_paths

    def create_markdown_files(self, total_pages: int):
        """
        为每一页创建Markdown文件

        Args:
            total_pages: 总页数
        """
        print(f"正在创建Markdown文件...")

        for page_num in range(1, total_pages + 1):
            image_filename = f"{self.pdf_name}_page_{page_num:03d}.jpg"
            md_filename = f"page_{page_num:03d}.md"
            md_path = self.markdown_folder / md_filename

            # 生成导航链接
            nav_links = self._generate_nav_links(page_num, total_pages)

            # 生成Markdown内容
            md_content = f"""# 第 {page_num} 页

![第{page_num}页](../images/{image_filename})

{nav_links}
"""

            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md_content)

            # 显示进度
            if page_num % 100 == 0 or page_num == 1 or page_num == total_pages:
                print(f"  进度: {page_num}/{total_pages} 个文件")

        print(f"✓ 完成! 共生成 {total_pages} 个Markdown文件")

    def _generate_nav_links(self, current_page: int, total_pages: int) -> str:
        """
        生成导航链接（Obsidian双中括号格式）

        Args:
            current_page: 当前页码
            total_pages: 总页数

        Returns:
            Markdown格式的导航链接
        """
        links = []

        # 上一页链接
        if current_page > 1:
            links.append(f"[[page_{current_page - 1:03d}|« 上一页]]")

        # 回到主页链接
        links.append("[[../README|📖 回到书页]]")

        # 下一页链接
        if current_page < total_pages:
            links.append(f"[[page_{current_page + 1:03d}|下一页 »]]")

        return "\n\n---\n\n" + " | " + " | ".join(links)

    def extract_toc(self) -> List[Tuple[int, str, int]]:
        """
        提取PDF目录

        Returns:
            目录列表，每个元素为 (层级, 标题, 页码)
        """
        print("正在提取PDF目录...")
        doc = fitz.open(self.pdf_path)
        toc = doc.get_toc()

        if not toc:
            print("  警告: PDF没有目录信息，将创建简单的分页目录")
            # 创建简单的分页目录
            total_pages = len(doc)
            toc = [(1, f"第 {i} 页", i) for i in range(1, total_pages + 1)]

        doc.close()
        print(f"✓ 提取到 {len(toc)} 个目录项")
        return toc

    def create_index_page(self, toc: List[Tuple[int, str, int]], total_pages: int):
        """
        创建主页目录

        Args:
            toc: 目录列表
            total_pages: 总页数
        """
        print("正在创建主页目录...")

        readme_path = self.base_folder / "README.md"

        # 生成Markdown内容
        md_content = f"""# {self.pdf_name}

> 本文档由PDF自动生成，包含 {total_pages} 页

## 目录

"""

        # 按层级组织目录（Obsidian格式，纯Markdown语法）
        current_level = 0
        for level, title, page_num in toc:
            # 确保页码在有效范围内
            if page_num < 1 or page_num > total_pages:
                continue

            # 计算缩进（Markdown使用空格缩进来表示层级）
            indent = "  " * (level - 1)

            # 生成目录项（Obsidian双中括号链接）
            md_content += f'{indent}- [[markdown/page_{page_num:03d}|{title}]] (第{page_num}页)\n'

        md_content += f"""

---

## 快速导航

- [[markdown/page_001|从第1页开始阅读]]
- [[markdown|按页浏览]]

---

*生成时间: {self._get_current_time()}*
"""

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"✓ 主页目录已创建: {readme_path}")

    @staticmethod
    def _get_current_time() -> str:
        """获取当前时间字符串"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def convert(self):
        """执行完整的转换流程"""
        print(f"\n{'='*60}")
        print(f"PDF转Markdown转换工具")
        print(f"{'='*60}\n")
        print(f"PDF文件: {self.pdf_path}")
        print(f"输出文件夹: {self.base_folder}\n")

        # 1. 提取目录
        toc = self.extract_toc()

        # 2. 转换PDF为图片
        self.pdf_to_images()

        # 3. 创建Markdown文件
        total_pages = len(list(self.images_folder.glob("*.jpg")))
        self.create_markdown_files(total_pages)

        # 4. 创建主页目录
        self.create_index_page(toc, total_pages)

        print(f"\n{'='*60}")
        print(f"✓ 转换完成!")
        print(f"{'='*60}\n")
        print(f"文件结构:")
        print(f"  {self.base_folder}/")
        print(f"  ├── images/          # 图片文件")
        print(f"  ├── markdown/         # Markdown文件")
        print(f"  └── README.md         # 主页目录")
        print(f"\n请打开 {self.base_folder}/README.md 开始阅读!\n")


def main():
    """主函数"""
    import sys

    if len(sys.argv) < 2:
        print("使用方法: python pdf_to_markdown.py <PDF文件路径> [DPI]")
        print("示例: python pdf_to_markdown.py machinelearning_concept.pdf 150")
        sys.exit(1)

    pdf_path = sys.argv[1]
    dpi = int(sys.argv[2]) if len(sys.argv) > 2 else 150

    if not os.path.exists(pdf_path):
        print(f"错误: PDF文件不存在: {pdf_path}")
        sys.exit(1)

    converter = PDFToMarkdownConverter(pdf_path, dpi)
    converter.convert()


if __name__ == "__main__":
    main()
