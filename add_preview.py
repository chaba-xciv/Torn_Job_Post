import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

preview_css = """
        .preview-box {
            margin-top: 15px;
            padding: 20px;
            border: 1px solid var(--border);
            border-radius: 6px;
            background: var(--card-bg);
            /* To simulate Torn forum background which can be light/dark based on user setting,
               but we let it inherit the card-bg so they can see how it looks in their current theme */
        }
        .preview-title {
            font-size: 0.9rem;
            font-weight: bold;
            color: var(--text-muted);
            margin-bottom: 10px;
            text-transform: uppercase;
        }
"""

html = html.replace("        .html-box textarea { height: 200px; resize: vertical; }", "        .html-box textarea { height: 200px; resize: vertical; }\n" + preview_css)

worker_preview_html = """
        <div class="html-box">
            <textarea id="w-html" readonly placeholder="HTML Code will appear here..."></textarea>
            <button onclick="copyToClipboard('w-html')" style="background: #4caf50;">Copy HTML Code</button>
        </div>

        <div class="preview-title" style="margin-top: 20px;">Live Preview</div>
        <div id="w-preview" class="preview-box">
            <i>Preview will appear here...</i>
        </div>
"""
html = html.replace("""        <div class="html-box">
            <textarea id="w-html" readonly placeholder="HTML Code will appear here..."></textarea>
            <button onclick="copyToClipboard('w-html')" style="background: #4caf50;">Copy HTML Code</button>
        </div>""", worker_preview_html)

hiring_preview_html = """
        <div class="html-box">
            <textarea id="h-html" readonly placeholder="HTML Code will appear here..."></textarea>
            <button onclick="copyToClipboard('h-html')" style="background: #4caf50;">Copy HTML Code</button>
        </div>

        <div class="preview-title" style="margin-top: 20px;">Live Preview</div>
        <div id="h-preview" class="preview-box">
            <i>Preview will appear here...</i>
        </div>
"""
html = html.replace("""        <div class="html-box">
            <textarea id="h-html" readonly placeholder="HTML Code will appear here..."></textarea>
            <button onclick="copyToClipboard('h-html')" style="background: #4caf50;">Copy HTML Code</button>
        </div>""", hiring_preview_html)

# Add js updates to populate preview
html = html.replace("document.getElementById('w-html').value = htmlCode;", "document.getElementById('w-html').value = htmlCode;\n        document.getElementById('w-preview').innerHTML = htmlCode;")
html = html.replace("document.getElementById('h-html').value = htmlCode;", "document.getElementById('h-html').value = htmlCode;\n        document.getElementById('h-preview').innerHTML = htmlCode;")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
