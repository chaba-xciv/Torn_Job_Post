import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Make sure we actually replace it, maybe the spacing was slightly off
css_search = """        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
        }

        .container {
            width: 100%;
            max-width: 900px;
            background: var(--card-bg);
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            overflow: hidden;
            border: 1px solid var(--border);
        }"""

css_replace = """        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0;
            padding: 10px;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
        }

        .container {
            width: 100%;
            max-width: 1000px;
            background: var(--card-bg);
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            overflow: hidden;
            border: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            margin-bottom: 20px;
        }

        /* Responsive grid adjustments */
        @media (max-width: 600px) {
            body { padding: 5px; }
            .tabs { flex-direction: column; }
            .tab { border-bottom: 1px solid var(--border); }
            .form-grid { grid-template-columns: 1fr; }
            .table-container { max-height: 300px; }
            .data-table th, .data-table td { padding: 5px; font-size: 0.85rem; }
        }"""

html = re.sub(r'        body \{.*?border: 1px solid var\(--border\);\n        \}', css_replace, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
