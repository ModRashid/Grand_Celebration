import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="The Grand Celebration | Muhammad & Areeba",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed",
)

INVITATION_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#d8ed9b">
<title>The Grand Celebration | Muhammad & Areeba</title>
<style>
:root{color-scheme:light;--leaf:#657b62;--lime:#dce6d3;--deep:#344b3b;--paper:#fffdf8;--ink:#344b3b;--muted:#788675;--line:#c5d1bd}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:Georgia,'Times New Roman',serif;background:#f1f3eb;color:var(--ink)}
button,a{font:inherit}
.canvas{min-height:100vh;width:100%;padding:clamp(18px,5vw,58px) 16px;background:#f1f3eb;display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative}
.canvas:before,.canvas:after{position:absolute;color:#a8bca3;font-size:clamp(100px,20vw,230px);opacity:.25;line-height:1;pointer-events:none;font-family:Georgia,serif}
.canvas:before{content:'❧';top:1%;left:-2%;transform:rotate(-32deg)}.canvas:after{content:'❧';bottom:0;right:-2%;transform:rotate(148deg)}
.invite{width:min(100%,720px);position:relative;background:var(--paper);border:1px solid var(--line);padding:clamp(28px,6vw,66px) clamp(22px,7vw,76px);text-align:center;box-shadow:0 24px 70px #344b3b18;isolation:isolate}
.invite:before{content:'';position:absolute;inset:10px;border:1px solid #dce4d5;pointer-events:none;z-index:-1}
.kicker{font-family:Arial,sans-serif;text-transform:uppercase;letter-spacing:.28em;font-size:11px;color:var(--leaf);font-weight:600}
.flourish{display:flex;align-items:center;justify-content:center;gap:13px;color:#849b7e;margin:19px 0 22px}.flourish span{width:54px;height:1px;background:#c5d1bd}.flourish b{font-size:21px;font-weight:400}
.intro{font-size:clamp(15px,2vw,18px);line-height:1.7;color:#52614a;margin:0 auto 22px;max-width:440px}
.names{font-size:clamp(34px,7vw,58px);line-height:1.08;font-weight:400;letter-spacing:-.035em;color:var(--deep);margin:0}
.amp{font-size:clamp(26px,5vw,40px);font-style:italic;color:#849b7e;line-height:1.4;margin:5px 0}
.family{font-size:14px;line-height:1.5;color:#68755e;margin:9px 0 17px;font-style:italic}
.date{font-size:clamp(20px,4vw,27px);letter-spacing:.06em;color:var(--deep);margin:4px 0 8px}
.venue{font-size:clamp(20px,3.6vw,25px);color:var(--deep);margin:0 0 7px}
.address{font-family:Arial,sans-serif;font-size:13px;line-height:1.7;color:#68755e;margin:0 auto;max-width:390px}
.time{display:inline-block;margin:21px 0 0;padding:9px 19px;border-top:1px solid #c5d1bd;border-bottom:1px solid #c5d1bd;font-family:Arial,sans-serif;text-transform:uppercase;letter-spacing:.14em;font-size:11px;color:var(--leaf)}
.actions{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin:27px 0 0}
.action{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:43px;padding:11px 16px;text-decoration:none;border:1px solid #aabca4;color:var(--leaf);font-family:Arial,sans-serif;font-size:12px;letter-spacing:.04em;transition:background .2s,color .2s;cursor:pointer;background:transparent}
.action.primary{background:var(--leaf);color:#fff;border-color:var(--leaf)}.action:hover{background:var(--lime);color:var(--deep);border-color:var(--lime)}
.rule{width:56px;height:1px;background:#c5d1bd;margin:28px auto 18px}
.host-title{font-size:15px;font-style:italic;color:#52614a;margin:0 0 10px}.hosts{font-family:Arial,sans-serif;font-size:12px;line-height:1.9;color:#66745c;margin:0}
.contacts{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-top:12px}.contacts a{font-family:Arial,sans-serif;font-size:12px;color:var(--leaf);text-decoration:none;border-bottom:1px solid #b5c98e;padding-bottom:2px}
.footer{font-family:Arial,sans-serif;font-size:9px;text-transform:uppercase;letter-spacing:.22em;color:#89987a;margin-top:30px}
@media(prefers-reduced-motion:no-preference){.invite{animation:arrive .8s ease-out both}@keyframes arrive{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}}
@media(max-width:420px){.actions{flex-direction:column}.action{width:100%}.invite{padding-left:23px;padding-right:23px}.kicker{letter-spacing:.2em}}
</style>
</head>
<body>
<main class="canvas">
  <article class="invite" aria-label="The grand celebration invitation">
    <div class="kicker">With the blessings of our families</div>
    <div class="flourish" aria-hidden="true"><span></span><b>❧</b><span></span></div>
    <p class="intro">Together with our families, we joyfully invite you to join us for the grand celebration of</p>
    <h1 class="names">Muhammad Abdul Rashid</h1>
    <p class="family">Son of Arshad Rashid</p>
    <div class="amp">and</div>
    <h2 class="names">Areeba Fatima</h2>
    <p class="family">Daughter of Naveed Zahir</p>
    <div class="flourish" aria-hidden="true"><span></span><b>✧</b><span></span></div>
    <p class="date">Friday, November 13, 2026</p>
    <p class="venue">Iconic Marquee</p>
    <p class="address">76, Block 14, Gulistan-e-Johar<br>Karachi, Pakistan</p>
    <div class="time">Gathering at 7:30 PM</div>
    <div class="actions">
      <a class="action primary" href="https://www.google.com/maps/search/?api=1&query=Iconic+Marquee%2C+76+Block+14%2C+Gulistan-e-Johar%2C+Karachi%2C+Pakistan" target="_blank" rel="noopener">⌖ &nbsp; View venue</a>
      <button class="action" id="calendarBtn" type="button">＋ &nbsp; Save the date</button>
      <a class="action" href="https://wa.me/923323178261?text=Assalam-o-Alaikum%2C%20I%20am%20responding%20to%20the%20grand%20celebration%20invitation%20of%20Muhammad%20Abdul%20Rashid%20and%20Areeba%20Fatima." target="_blank" rel="noopener">♡ &nbsp; RSVP on WhatsApp</a>
    </div>
    <div class="rule"></div>
    <p class="host-title">With warm regards from</p>
    <p class="hosts">Arshad Rashid &nbsp;·&nbsp; Amna Arshad &nbsp;·&nbsp; Daniyal Ayub</p>
    <div class="contacts">
      <a href="https://wa.me/923323178261" target="_blank" rel="noopener">+92 332 3178261</a>
      <a href="https://wa.me/923357227454" target="_blank" rel="noopener">+92 335 7227454</a>
      <a href="https://wa.me/923312151091" target="_blank" rel="noopener">+92 331 2151091</a>
    </div>
    <div class="footer">A beautiful beginning · A day to remember</div>
  </article>
</main>
<script>
document.getElementById('calendarBtn').addEventListener('click', function () {
  const event = [
    'BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Grand Celebration Invitation//EN','CALSCALE:GREGORIAN','BEGIN:VEVENT',
    'UID:muhammad-areeba-grand-celebration-20261113@example.invalid','DTSTAMP:20261015T000000Z','DTSTART:20261113T143000Z','DTEND:20261113T170000Z',
    'SUMMARY:The Grand Celebration of Muhammad Abdul Rashid & Areeba Fatima','LOCATION:Iconic Marquee, 76 Block 14, Gulistan-e-Johar, Karachi, Pakistan',
    'DESCRIPTION:Gathering time 7:30 PM Pakistan Standard Time.','END:VEVENT','END:VCALENDAR'
  ].join('\\r\\n');
  const blob = new Blob([event], {type:'text/calendar;charset=utf-8'});
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a'); link.href=url; link.download='Muhammad-and-Areeba-Grand-Celebration.ics';
  document.body.appendChild(link); link.click(); link.remove(); URL.revokeObjectURL(url);
});
</script>
</body>
</html>"""

st.markdown(
    "<div style='text-align:center;color:#657b62;font-size:0.9rem;margin-bottom:0.5rem'>"
    "🌿 Sage green · Ivory · Botanical invitation</div>",
    unsafe_allow_html=True,
)
components.html(INVITATION_HTML, height=1600, scrolling=True)
