import pypdf
from flask import Flask, render_template, request, redirect, url_for

def uploadFile(file):
    try:
        reader = pypdf.PdfReader(file, "rb")
        page = reader.pages[0]
        text = page.extract_text(0)
        text = text.replace('\n', ' ').replace('\r', '')
        return 0, text
    except Exception as e:
        print(e)
    return -1, None
