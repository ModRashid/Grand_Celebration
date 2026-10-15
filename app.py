import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Muhammad Abdul Rashid & Areeba Fatima | The Grand Celebration",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header, [data-testid="stToolbar"] {visibility:hidden; height:0;}
.stApp { background:#f4f0e7; }
.block-container { padding:0 !important; max-width:100% !important; }
iframe { border:0 !important; }
</style>
""", unsafe_allow_html=True)

INVITATION_HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#203b31">
<title>The Grand Celebration | Muhammad & Areeba</title>
<style>
:root{--forest:#203b31;--forest2:#2e4d40;--sage:#9eae91;--gold:#b99a61;--cream:#f7f2e8;--paper:#fffdf7;--ink:#24382f;--muted:#68766b;--line:#d8cfb9}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--forest);color:var(--ink);font-family:Georgia,'Times New Roman',serif}a,button{font:inherit}.site{min-height:100vh;background:var(--cream);overflow:hidden}.hero{min-height:94vh;position:relative;display:flex;align-items:center;justify-content:center;text-align:center;padding:40px 20px;color:var(--cream);background:radial-gradient(ellipse at 50% 40%,#456451 0%,#2e4d40 38%,#203b31 78%);isolation:isolate}.hero:before,.hero:after{content:'❧';position:absolute;color:#c5b27e;opacity:.24;font-size:clamp(180px,33vw,420px);line-height:1;pointer-events:none;z-index:-1}.hero:before{top:-70px;left:-75px;transform:rotate(-35deg)}.hero:after{bottom:-90px;right:-70px;transform:rotate(145deg)}.hero-inner{width:min(100%,780px);padding:clamp(32px,6vw,76px) 20px;border:1px solid #b99a6177;outline:1px solid #b99a6133;outline-offset:9px;position:relative}.eyebrow{font:600 10px/1.8 Arial,sans-serif;text-transform:uppercase;letter-spacing:.34em;color:#d9c79a}.small-flourish{color:var(--gold);font-size:25px;margin:17px 0}.hero h1{font-weight:400;font-size:clamp(43px,9vw,88px);line-height:1.02;letter-spacing:-.045em;margin:12px 0;color:#fffaf0}.hero .amp{font-size:clamp(27px,5vw,44px);font-style:italic;color:#d4bd86;margin:8px 0}.hero .sub{font-size:clamp(14px,2vw,18px);line-height:1.8;color:#e4e4d8;margin:22px auto 0;max-width:480px}.hero-date{font:11px Arial,sans-serif;text-transform:uppercase;letter-spacing:.22em;color:#d9c79a;margin-top:28px}.scroll-cue{position:absolute;bottom:24px;left:0;right:0;font:10px Arial,sans-serif;text-transform:uppercase;letter-spacing:.25em;color:#e2d6b7;opacity:.8}.section{padding:76px 20px;text-align:center}.section-inner{max-width:780px;margin:auto}.section-label{font:600 10px Arial,sans-serif;letter-spacing:.28em;text-transform:uppercase;color:#8d7746}.section h2{font-weight:400;font-size:clamp(32px,6vw,54px);line-height:1.15;color:var(--forest);margin:14px 0 18px}.ornament{color:var(--gold);font-size:23px;margin:18px 0}.familyline{font-style:italic;color:var(--muted);font-size:15px;margin:7px 0}.invitation-copy{max-width:560px;margin:0 auto;color:#59675c;font-size:16px;line-height:1.9}.details{background:#e9e8dc}.detail-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:32px auto 0;max-width:800px}.detail{border:1px solid #c9cbb9;background:#f8f5ec;padding:24px 14px;min-height:150px;display:flex;flex-direction:column;justify-content:center}.detail .symbol{font-size:24px;color:#a68b50;margin-bottom:12px}.detail .label{font:600 10px Arial,sans-serif;text-transform:uppercase;letter-spacing:.2em;color:#7a846f}.detail .value{font-size:20px;color:var(--forest);line-height:1.45;margin-top:9px}.detail .small{font:12px/1.7 Arial,sans-serif;color:#6b7769;margin-top:5px}.buttons{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-top:30px}.btn{display:inline-flex;align-items:center;justify-content:center;min-height:46px;padding:13px 19px;border:1px solid var(--forest2);text-decoration:none;color:var(--forest);background:transparent;font:600 10px Arial,sans-serif;text-transform:uppercase;letter-spacing:.12em;cursor:pointer;transition:.2s}.btn.primary{background:var(--forest);color:#fffaf0}.btn:hover{background:#d8dfd0;color:var(--forest)}.hosts{background:var(--forest);color:var(--cream)}.hosts .section-label{color:#d4bd86}.hosts h2{color:var(--cream)}.hosts .invitation-copy{color:#dce0d5}.host-names{font-size:clamp(18px,3vw,24px);line-height:1.8;color:#fff8e8}.contact-list{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-top:25px}.contact-list a{color:#dfd0a6;text-decoration:none;font:12px Arial,sans-serif;border-bottom:1px solid #a58d5a;padding:7px 3px}.footer{text-align:center;padding:24px 15px;background:#182f27;color:#b9c3b4;font:9px Arial,sans-serif;text-transform:uppercase;letter-spacing:.22em}.divider{height:1px;width:70px;background:var(--gold);margin:26px auto}.fade{animation:fadeup .9s ease both}@keyframes fadeup{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:translateY(0)}}
@media(max-width:650px){.hero{min-height:88vh;padding:28px 18px}.hero-inner{padding:44px 14px}.eyebrow{letter-spacing:.22em}.detail-grid{grid-template-columns:1fr;max-width:360px}.detail{min-height:unset;padding:21px}.section{padding:58px 20px}.buttons{flex-direction:column;max-width:340px;margin-left:auto;margin-right:auto}.btn{width:100%}.hero:before{left:-125px}.hero:after{right:-120px}}
@media(prefers-reduced-motion:reduce){.fade{animation:none}html{scroll-behavior:auto}}
</style>
</head>
<body>
<div class="site">
  <section class="hero">
    <div class="hero-inner fade">
      <div class="eyebrow">Together with their families</div>
      <div class="small-flourish">✦ &nbsp; ❧ &nbsp; ✦</div>
      <h1>Muhammad Abdul<br>Rashid</h1>
      <div class="amp">&amp;</div>
      <h1>Areeba Fatima</h1>
      <p class="sub">Request the pleasure of your company<br>at <em>The Grand Celebration</em></p>
      <div class="hero-date">Friday · November 13 · 2026</div>
    </div>
    <div class="scroll-cue">Scroll to discover &nbsp; ↓</div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-label">A celebration of two families</div>
      <div class="ornament">❧</div>
      <h2>With joy in our hearts</h2>
      <p class="invitation-copy">With the blessings of our families, we warmly invite you to join us as we celebrate the union of</p>
      <div class="divider"></div>
      <h2>Muhammad Abdul Rashid</h2>
      <p class="familyline">Son of Arshad Rashid</p>
      <div class="ornament">and</div>
      <h2>Areeba Fatima</h2>
      <p class="familyline">Daughter of Naveed Zahir</p>
    </div>
  </section>

  <section class="section details">
    <div class="section-inner">
      <div class="section-label">Please join us</div>
      <h2>The Grand Celebration</h2>
      <div class="ornament">✧</div>
      <div class="detail-grid">
        <div class="detail"><div class="symbol">◷</div><div class="label">Date &amp; Time</div><div class="value">Friday, November 13</div><div class="small">Gathering at 7:30 PM</div></div>
        <div class="detail"><div class="symbol">⌖</div><div class="label">Venue</div><div class="value">Iconic Marquee</div><div class="small">76, Block 14, Gulistan-e-Johar<br>Karachi, Pakistan</div></div>
        <div class="detail"><div class="symbol">❧</div><div class="label">With warm regards</div><div class="value">Our Families</div><div class="small">Arshad Rashid · Amna Arshad<br>Daniyal Ayub</div></div>
      </div>
      <div class="buttons">
        <a class="btn primary" href="https://www.google.com/maps/search/?api=1&amp;query=Iconic+Marquee%2C+76+Block+14%2C+Gulistan-e-Johar%2C+Karachi%2C+Pakistan" target="_blank" rel="noopener">⌖ &nbsp; Open venue map</a>
        <button class="btn" id="calendarBtn" type="button">＋ &nbsp; Save the date</button>
        <a class="btn" href="https://wa.me/923323178261?text=Assalam-o-Alaikum%2C%20I%20am%20responding%20to%20the%20invitation%20of%20Muhammad%20Abdul%20Rashid%20and%20Areeba%20Fatima." target="_blank" rel="noopener">♡ &nbsp; RSVP on WhatsApp</a>
      </div>
    </div>
  </section>

  <section class="section hosts">
    <div class="section-inner">
      <div class="section-label">Your presence will mean a lot</div>
      <div class="ornament">✦</div>
      <h2>We look forward to celebrating with you</h2>
      <p class="invitation-copy">With love and best wishes,</p>
      <p class="host-names">Arshad Rashid<br>Amna Arshad<br>Daniyal Ayub</p>
      <div class="divider"></div>
      <p class="invitation-copy">For any assistance, please contact</p>
      <div class="contact-list">
        <a href="https://wa.me/923323178261" target="_blank" rel="noopener">+92 332 3178261</a>
        <a href="https://wa.me/923357227454" target="_blank" rel="noopener">+92 335 7227454</a>
        <a href="https://wa.me/923312151091" target="_blank" rel="noopener">+92 331 2151091</a>
      </div>
    </div>
  </section>
  <div class="footer">The Grand Celebration · Muhammad &amp; Areeba · 2026</div>
</div>
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
</html>'''

components.html(INVITATION_HTML, height=3300, scrolling=True)
