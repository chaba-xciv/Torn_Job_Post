import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Modify CSS to support explicit dark theme
css_search = """        @media (prefers-color-scheme: dark) {
            :root {
                --bg-color: #18191a;
                --card-bg: #242526;
                --text-main: #e4e6eb;
                --text-muted: #b0b3b8;
                --primary: #4e8cff;
                --primary-hover: #3b71d6;
                --border: #3e4042;
                --highlight: #3a3b3c;
            }
        }"""

css_replace = """        body.dark-theme {
            --bg-color: #18191a;
            --card-bg: #242526;
            --text-main: #e4e6eb;
            --text-muted: #b0b3b8;
            --primary: #4e8cff;
            --primary-hover: #3b71d6;
            --border: #3e4042;
            --highlight: #3a3b3c;
        }

        /* Default dark theme if preferred by OS */
        @media (prefers-color-scheme: dark) {
            body:not(.light-theme) {
                --bg-color: #18191a;
                --card-bg: #242526;
                --text-main: #e4e6eb;
                --text-muted: #b0b3b8;
                --primary: #4e8cff;
                --primary-hover: #3b71d6;
                --border: #3e4042;
                --highlight: #3a3b3c;
            }
        }

        .theme-toggle {
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
        }
        .theme-toggle:hover {
            background: rgba(255,255,255,0.2);
        }

        .header-top {
            position: relative;
        }
"""

html = html.replace(css_search, css_replace)

# Modify HTML
html_search = """    <div class="header">
        <h1>Torn City - Forum Post Builder</h1>
    </div>"""

html_replace = """    <div class="header header-top">
        <h1>Torn City - Forum Post Builder</h1>
        <button id="theme-toggle-btn" class="theme-toggle" onclick="toggleTheme()">🌓 Theme</button>
    </div>"""

html = html.replace(html_search, html_replace)

# Modify JS
js_append = """

    // Theme Toggle Functionality
    function toggleTheme() {
        const body = document.body;
        if (body.classList.contains('dark-theme')) {
            body.classList.remove('dark-theme');
            body.classList.add('light-theme');
            localStorage.setItem('theme', 'light');
        } else if (body.classList.contains('light-theme')) {
            body.classList.remove('light-theme');
            body.classList.add('dark-theme');
            localStorage.setItem('theme', 'dark');
        } else {
            // No class means it's using OS preference
            const isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
            if (isDark) {
                body.classList.add('light-theme');
                localStorage.setItem('theme', 'light');
            } else {
                body.classList.add('dark-theme');
                localStorage.setItem('theme', 'dark');
            }
        }
    }

    function loadTheme() {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') {
            document.body.classList.add('dark-theme');
        } else if (savedTheme === 'light') {
            document.body.classList.add('light-theme');
        }
    }
"""

# add loadTheme to window.onload
html = html.replace("window.onload = initDropdowns;", "window.onload = function() { loadTheme(); initDropdowns(); };\n" + js_append)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
