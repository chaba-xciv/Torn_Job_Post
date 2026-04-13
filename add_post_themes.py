import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add theme selector UI
theme_html = """
        <div class="form-grid" style="margin-top: 15px;">
            <div class="input-group">
                <label>Post Color Theme</label>
                <select id="w-post-theme" onchange="generateWorkerHTML()">
                    <option value="#333333">Default (Dark Grey)</option>
                    <option value="#3b5998">Torn Blue</option>
                    <option value="#2e7d32">Green</option>
                    <option value="#c62828">Red</option>
                    <option value="#6a1b9a">Purple</option>
                    <option value="#e65100">Orange</option>
                </select>
            </div>
        </div>
"""

# Insert before "Additional Notes" in worker tab
html = html.replace("""<div class="form-grid" style="margin-top: 15px;">
            <div class="input-group">
                <label>Additional Notes</label>""", theme_html + """<div class="form-grid" style="margin-top: 15px;">
            <div class="input-group">
                <label>Additional Notes</label>""")

# Do the same for hiring tab
hiring_theme_html = """
        <div class="form-grid" style="margin-top: 15px;">
            <div class="input-group">
                <label>Post Color Theme</label>
                <select id="h-post-theme" onchange="generateHiringHTML()">
                    <option value="#333333">Default (Dark Grey)</option>
                    <option value="#3b5998">Torn Blue</option>
                    <option value="#2e7d32">Green</option>
                    <option value="#c62828">Red</option>
                    <option value="#6a1b9a">Purple</option>
                    <option value="#e65100">Orange</option>
                </select>
            </div>
        </div>
"""
# Insert before "Perks / Pay Details" in hiring tab
html = html.replace("""<div class="form-grid">
            <div class="input-group">
                <label>Perks / Pay Details</label>""", hiring_theme_html + """<div class="form-grid">
            <div class="input-group">
                <label>Perks / Pay Details</label>""")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
