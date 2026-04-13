import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Make target positions format better for the card
search = """        if(checkedBoxes.length > 0) {
            jobListHTML = "<br><br><b>🎯 Target Positions & My Expected Eff:</b><ul>";
            checkedBoxes.forEach(cb => {
                const [comp, pos, eff] = cb.value.split('|');
                let meritStr = merit > 0 ? ` + ${merit}% merit ${merit}/10` : "";
                jobListHTML += `<li>${comp} - ${pos}: <b>with ${eff}% eff job stats${meritStr}</b></li>`;
            });
            jobListHTML += "</ul>";
        } else {
            jobListHTML = "<br><br><i>(Open to any positions matching my stats)</i><br><br>";
        }"""

replace = """        if(checkedBoxes.length > 0) {
            jobListHTML = `<strong style="color: ${document.getElementById('w-post-theme') ? document.getElementById('w-post-theme').value : '#333333'};">🎯 Target Positions & My Expected Eff:</strong><ul style="margin-top: 5px; margin-bottom: 0;">`;
            checkedBoxes.forEach(cb => {
                const [comp, pos, eff] = cb.value.split('|');
                let meritStr = merit > 0 ? ` + ${merit}% merit` : "";
                jobListHTML += `<li>${comp} - ${pos}: <b>${eff}% eff</b>${meritStr}</li>`;
            });
            jobListHTML += "</ul>";
        } else {
            jobListHTML = "<i>(Open to any positions matching my stats)</i>";
        }"""

html = html.replace(search, replace)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
