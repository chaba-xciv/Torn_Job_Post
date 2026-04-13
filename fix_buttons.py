import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix CSS for the theme-toggle buttons which are overlapping
css_search = """        .theme-toggle {
            position: absolute;
            top: 20px;
            right: 20px;
            background: transparent;
            border: 1px solid white;
            color: white;
            width: auto;
            padding: 5px 10px;
            font-size: 0.9rem;
            cursor: pointer;
            border-radius: 4px;
            margin: 0;
        }"""

css_replace = """        .theme-toggle {
            background: transparent;
            border: 1px solid white;
            color: white;
            width: auto;
            padding: 5px 10px;
            font-size: 0.9rem;
            cursor: pointer;
            border-radius: 4px;
            margin: 0;
        }"""

html = html.replace(css_search, css_replace)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
