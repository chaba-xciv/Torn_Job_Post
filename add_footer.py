import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

footer_html = """
    <div style="text-align: center; margin-top: 30px; font-size: 0.85rem; color: var(--text-muted); padding: 15px; border-top: 1px solid var(--border);">
        This website was developed by <a href="https://jules.google/" target="_blank" style="color: var(--primary); text-decoration: none; font-weight: bold;">Jules AI</a>.
        <br>
        View source code on <a href="https://github.com/chaba-xciv/Torn_Job_Post" target="_blank" style="color: var(--primary); text-decoration: none; font-weight: bold;">GitHub</a>.
    </div>
"""

# Insert before closing container div
html = html.replace("    </div>\n</div>\n\n<script", footer_html + "    </div>\n</div>\n\n<script")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
