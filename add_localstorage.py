import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add Save and Clear buttons to the header or somewhere appropriate
header_search = """    <div class="header header-top">
        <h1>Torn City - Forum Post Builder</h1>
        <button id="theme-toggle-btn" class="theme-toggle" onclick="toggleTheme()">🌓 Theme</button>
    </div>"""

header_replace = """    <div class="header header-top">
        <h1>Torn City - Forum Post Builder</h1>
        <div style="position: absolute; top: 15px; right: 15px; display: flex; gap: 10px;">
            <button class="theme-toggle" onclick="clearData()" style="border-color: #ff5252; color: #ff5252;" title="Clear all saved data">🗑️ Clear</button>
            <button id="theme-toggle-btn" class="theme-toggle" onclick="toggleTheme()">🌓 Theme</button>
        </div>
    </div>"""
html = html.replace(header_search, header_replace)

# Add save/load js
js_append = """
    // --- LocalStorage Logic ---
    const INPUT_IDS = [
        'w-man', 'w-int', 'w-end', 'w-merit', 'w-notes', 'w-post-theme',
        'h-eff', 'h-link', 'h-perks', 'h-post-theme'
    ]; // h-company loaded later

    function saveData() {
        INPUT_IDS.forEach(id => {
            const el = document.getElementById(id);
            if (el) {
                localStorage.setItem(id, el.value);
            }
        });

        const wStyle = document.querySelector('input[name="w-style"]:checked');
        if (wStyle) localStorage.setItem('w-style', wStyle.value);

        const hStyle = document.querySelector('input[name="h-style"]:checked');
        if (hStyle) localStorage.setItem('h-style', hStyle.value);

        const hCompany = document.getElementById('h-company');
        if (hCompany) localStorage.setItem('h-company', hCompany.value);
    }

    function loadData() {
        INPUT_IDS.forEach(id => {
            const val = localStorage.getItem(id);
            if (val !== null) {
                const el = document.getElementById(id);
                if (el) el.value = val;
            }
        });

        const wStyleVal = localStorage.getItem('w-style');
        if (wStyleVal) {
            const r = document.querySelector(`input[name="w-style"][value="${wStyleVal}"]`);
            if (r) r.checked = true;
        }

        const hStyleVal = localStorage.getItem('h-style');
        if (hStyleVal) {
            const r = document.querySelector(`input[name="h-style"][value="${hStyleVal}"]`);
            if (r) r.checked = true;
        }
    }

    function clearData() {
        if(confirm("Are you sure you want to clear all your saved inputs?")) {
            INPUT_IDS.forEach(id => localStorage.removeItem(id));
            localStorage.removeItem('w-style');
            localStorage.removeItem('h-style');
            localStorage.removeItem('h-company');
            location.reload();
        }
    }

    // Attach listeners to save on change
    function attachSaveListeners() {
        INPUT_IDS.forEach(id => {
            const el = document.getElementById(id);
            if(el) {
                el.addEventListener('input', saveData);
                el.addEventListener('change', saveData);
            }
        });
        document.querySelectorAll('input[name="w-style"], input[name="h-style"]').forEach(el => {
            el.addEventListener('change', saveData);
        });

        const hCompany = document.getElementById('h-company');
        if(hCompany) {
            hCompany.addEventListener('change', saveData);
        }
    }
"""

html = html.replace("    // Theme Toggle Functionality", js_append + "\n    // Theme Toggle Functionality")

# Modify initDropdowns to load data
init_search = """    function initDropdowns() {
        generateJobsDB();
        const companies = [...new Set(jobsDB.map(job => job.c))].sort();

        const hCompany = document.getElementById('h-company');
        if (hCompany) {
            companies.forEach(comp => {
                hCompany.add(new Option(comp, comp));
            });
            renderHiringTable();
        }

        renderWorkerTable();
    }"""

init_replace = """    function initDropdowns() {
        generateJobsDB();
        const companies = [...new Set(jobsDB.map(job => job.c))].sort();

        loadData();

        const hCompany = document.getElementById('h-company');
        if (hCompany) {
            companies.forEach(comp => {
                hCompany.add(new Option(comp, comp));
            });

            // Restore h-company specifically after options are added
            const savedComp = localStorage.getItem('h-company');
            if(savedComp && companies.includes(savedComp)) {
                hCompany.value = savedComp;
            }

            renderHiringTable();
        }

        renderWorkerTable();
        attachSaveListeners();
    }"""

html = html.replace(init_search, init_replace)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
