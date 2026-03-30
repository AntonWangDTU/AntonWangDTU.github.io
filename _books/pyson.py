#!/usr/bin/env python3

import sys
import requests
import re
from urllib.parse import urlparse, parse_qs, unquote
import os

# -----------------------------
# Helpers
# -----------------------------


def extract_json_url(url: str) -> str:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)

    # Case: edition param
    if "edition" in query:
        edition_raw = query["edition"][0]
        edition_decoded = unquote(edition_raw)
        match = re.search(r"/books/(OL\d+M)", edition_decoded)
        if match:
            olid = match.group(1)
            return f"https://openlibrary.org/books/{olid}.json"

    clean_path = re.sub(r"[?#].*$", "", url)
    if clean_path.endswith(".json"):
        return clean_path
    if "openlibrary.org" in clean_path:
        return clean_path.rstrip("/") + ".json"
    raise ValueError("Unsupported URL")


def fetch(url: str):
    res = requests.get(url)
    res.raise_for_status()
    return res.json()


def get_author_name(author_key: str):
    try:
        data = fetch(f"https://openlibrary.org{author_key}.json")
        return data.get("name")
    except:
        return None


def extract_book(data: dict):
    title = data.get("title")
    publish_date = data.get("publish_date")
    year = None
    if publish_date:
        match = re.search(r"\d{4}", publish_date)
        if match:
            year = match.group(0)

    isbn = None
    if "isbn_13" in data:
        isbn = data["isbn_13"][0]
    elif "isbn_10" in data:
        isbn = data["isbn_10"][0]

    olid = None
    if "key" in data:
        olid = data["key"].split("/")[-1]

    author = None
    if "authors" in data and data["authors"]:
        key = data["authors"][0].get("key")
        if key:
            author = get_author_name(key)

    # Get cover id if available
    cover_id = None
    if "covers" in data and data["covers"]:
        cover_id = data["covers"][0]

    return {
        "title": title,
        "author": author,
        "isbn": isbn,
        "olid": olid,
        "released": year,
        "cover_id": cover_id,
    }


def to_yaml(book: dict):
    slug = (book["title"] or "").lower().replace(" ", "-")
    return f"""---
layout: book-review
title: {book.get("title")}
author: {book.get("author")}
cover: assets/img/book_covers/{slug}.jpg
olid: {book.get("olid")}
isbn: {book.get("isbn")}
categories: 
tags: 
buy_link: 
date: {book.get("released")}-01-01
started: null
finished: null
released: {book.get("released")}
stars: null
goodreads_review: null
status: Finished
---
"""


def download_cover(cover_id: int, slug: str):
    url = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
    folder = "/home/aws/Documents/AntonWangDTU.github.io/assets/img/book_covers/"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{slug}.jpg")
    r = requests.get(url)
    r.raise_for_status()
    with open(path, "wb") as f:
        f.write(r.content)
    return path


def save_markdown(yaml_content: str, slug: str):
    folder = "/home/aws/Documents/AntonWangDTU.github.io/_books/"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{slug}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(yaml_content)
    return path


# -----------------------------
# Main
# -----------------------------


def main():
    if len(sys.argv) != 2:
        print("Usage: ./pyson.py <OpenLibrary URL>")
        sys.exit(1)

    input_url = sys.argv[1]

    try:
        json_url = extract_json_url(input_url)
        data = fetch(json_url)

        book = extract_book(data)
        slug = (book["title"] or "").lower().replace(" ", "-")

        # Download cover if available
        if book.get("cover_id"):
            cover_path = download_cover(book["cover_id"], slug)
            print(f"Cover saved: {cover_path}")

        # Generate YAML
        yaml_content = to_yaml(book)

        # Save .md file
        md_path = save_markdown(yaml_content, slug)
        print(f"Markdown saved: {md_path}")

        print("Done!")

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
