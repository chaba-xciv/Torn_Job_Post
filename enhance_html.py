import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update generateWorkerHTML
worker_html_search = """        const htmlCode = `<b>Looking for a Job</b><br><br>
<b>📊 My Base Stats:</b><br>
MAN: ${Number(man).toLocaleString()}<br>
INT: ${Number(int).toLocaleString()}<br>
END: ${Number(end).toLocaleString()}<br><br>
<b>⭐ Merits:</b> ${merit}/10 Employee Stats<br>
<b>💼 Work Style:</b> ${workStyleText}
${jobListHTML}
${notes ? `<b>💬 Notes:</b><br>${formattedNotes}` : ''}`;"""

worker_html_replace = """        const themeColor = document.getElementById('w-post-theme') ? document.getElementById('w-post-theme').value : '#333333';

        const htmlCode = `<div style="border: 2px solid ${themeColor}; border-radius: 8px; padding: 15px; max-width: 600px; font-family: Arial, sans-serif; background-color: transparent;">
    <h2 style="color: ${themeColor}; margin-top: 0; border-bottom: 2px solid ${themeColor}; padding-bottom: 5px;">Looking for a Job</h2>
    <div style="margin-bottom: 10px;">
        <strong style="color: ${themeColor};">📊 My Base Stats:</strong><br>
        • MAN: ${Number(man).toLocaleString()}<br>
        • INT: ${Number(int).toLocaleString()}<br>
        • END: ${Number(end).toLocaleString()}<br>
    </div>
    <div style="margin-bottom: 10px;">
        <strong style="color: ${themeColor};">⭐ Merits:</strong> ${merit}/10 Employee Stats<br>
    </div>
    <div style="margin-bottom: 10px;">
        <strong style="color: ${themeColor};">💼 Work Style:</strong> ${workStyleText}
    </div>
    <div style="margin-bottom: 10px;">
        ${jobListHTML}
    </div>
    ${notes ? `<div style="margin-top: 15px; padding: 10px; background-color: rgba(0,0,0,0.05); border-left: 4px solid ${themeColor};">
        <strong style="color: ${themeColor};">💬 Notes:</strong><br>${formattedNotes}
    </div>` : ''}
</div>`;"""

html = html.replace(worker_html_search, worker_html_replace)


# Update generateHiringHTML
hiring_html_search = """        const htmlCode = `<b>🏢 Hiring: ${comp} </b><br><br>
We are currently looking for dedicated workers to join our team!<br><br>
<b>🎯 Target Efficiency:</b> <b>${eff} Eff</b><br>
<b>💼 Work Style:</b> ${workStyleText}<br><br>
<b>📌 Positions Open:</b><br>
${positionsHTML}<br>
${formattedPerks ? `<b>💰 What we offer / Details:</b><br>${formattedPerks}<br><br>` : ''}
If you meet the requirements, please PM me or apply directly!
${link ? `<br><br><a href="${link}"><b>[Apply Here]</b></a>` : ''}`;"""

hiring_html_replace = """        const themeColor = document.getElementById('h-post-theme') ? document.getElementById('h-post-theme').value : '#333333';

        const htmlCode = `<div style="border: 2px solid ${themeColor}; border-radius: 8px; padding: 15px; max-width: 600px; font-family: Arial, sans-serif; background-color: transparent;">
    <h2 style="color: ${themeColor}; margin-top: 0; border-bottom: 2px solid ${themeColor}; padding-bottom: 5px;">🏢 Hiring: ${comp}</h2>
    <p>We are currently looking for dedicated workers to join our team!</p>

    <div style="margin-bottom: 10px;">
        <strong style="color: ${themeColor};">🎯 Target Efficiency:</strong> <b>${eff} Eff</b><br>
    </div>
    <div style="margin-bottom: 10px;">
        <strong style="color: ${themeColor};">💼 Work Style:</strong> ${workStyleText}<br>
    </div>
    <div style="margin-bottom: 10px;">
        <strong style="color: ${themeColor};">📌 Positions Open:</strong><br>
        ${positionsHTML}
    </div>
    ${formattedPerks ? `<div style="margin-top: 15px; padding: 10px; background-color: rgba(0,0,0,0.05); border-left: 4px solid ${themeColor};">
        <strong style="color: ${themeColor};">💰 What we offer / Details:</strong><br>${formattedPerks}
    </div>` : ''}

    <p style="margin-top: 15px;">If you meet the requirements, please PM me or apply directly!</p>
    ${link ? `<div style="text-align: center; margin-top: 20px;">
        <a href="${link}" style="background-color: ${themeColor}; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">👉 Apply Here 👈</a>
    </div>` : ''}
</div>`;"""

html = html.replace(hiring_html_search, hiring_html_replace)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
