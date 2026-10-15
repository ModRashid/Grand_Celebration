import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Valima Invitation | Muhammad Abdul Rashid & Areeba Fatima",
    page_icon="❀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header, [data-testid="stToolbar"], [data-testid="stHeader"] {display:none !important;}
.stApp { background:#f3f6ef; }
.block-container { padding:0 !important; max-width:100% !important; }
div[data-testid="stHtml"] { padding:0 !important; }
iframe { border:0 !important; width:100% !important; display:block; }
</style>
""", unsafe_allow_html=True)

INVITATION_HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#eaf0e6">
<title>Valima Invitation | Muhammad Abdul Rashid &amp; Areeba Fatima</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,500&display=swap" rel="stylesheet">
<style>
:root{--sage:#879b7d;--sage-dark:#405742;--sage-deep:#263e30;--pale:#f1f5ed;--paper:#fffefa;--gold:#b49a61;--gold-light:#dfcf9f;--ink:#304535;--muted:#68766a;--line:#d5dfd0}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#eaf0e6;color:var(--ink);font-family:'DM Sans',sans-serif;-webkit-text-size-adjust:100%}a,button{font:inherit}.wrap{width:100%;padding:10px;background:linear-gradient(145deg,#e8efe3,#f9faf6 48%,#e5eddf)}
.card{position:relative;isolation:isolate;max-width:800px;margin:0 auto;background:var(--paper);border:1px solid #c4d2bd;overflow:hidden;box-shadow:0 12px 38px #2f4b3212}.card:before{content:'';position:absolute;inset:7px;border:1px solid #d9c99a;pointer-events:none;z-index:-1}
.floral{position:absolute;pointer-events:none;z-index:-1;color:#a5b99b;opacity:.65;font-family:Georgia,serif;font-size:clamp(36px,8vw,72px);line-height:1.05}.floral.tl{top:10px;left:12px;transform:rotate(-22deg)}.floral.tr{top:10px;right:12px;transform:scaleX(-1) rotate(-22deg)}.floral.bl{bottom:10px;left:12px;transform:scaleY(-1) rotate(-22deg)}.floral.br{bottom:10px;right:12px;transform:scale(-1) rotate(-22deg)}
.bismillah{text-align:center;padding:23px 18px 7px;position:relative}.arabic{font-family:'Times New Roman',serif;font-size:clamp(25px,5.5vw,37px);line-height:1.55;direction:rtl;color:var(--sage-deep)}.translation{font:italic 11px/1.55 'Playfair Display',serif;color:var(--muted);margin-top:1px}.divider-ornament{display:flex;align-items:center;justify-content:center;gap:10px;color:var(--gold);font-size:17px;margin:8px auto}.divider-ornament:before,.divider-ornament:after{content:'';height:1px;width:52px;background:linear-gradient(90deg,transparent,var(--gold))}.divider-ornament:after{transform:scaleX(-1)}
.intro{text-align:center;position:relative;padding:4px 28px 0}.eyebrow{font:700 9px/1.7 'DM Sans',sans-serif;letter-spacing:.23em;text-transform:uppercase;color:var(--sage)}.intro-copy{max-width:590px;margin:8px auto 3px;font-family:'Playfair Display',serif;font-size:clamp(16px,2.8vw,19px);line-height:1.55;color:#536654}.intro-copy strong{font-weight:600;color:var(--sage-deep)}
.couple{text-align:center;padding:3px 15px 2px}.couple-name{font-family:'Cormorant Garamond',serif;font-size:clamp(47px,10vw,79px);font-weight:500;line-height:.91;letter-spacing:-.025em;color:var(--sage-deep);margin:8px auto 0;overflow-wrap:anywhere}.ampersand{font-family:'Playfair Display',serif;font-size:clamp(25px,5vw,36px);font-style:italic;line-height:1.15;color:var(--gold);margin:3px 0}
.date-panel{max-width:580px;margin:16px auto 15px;padding:14px 12px 13px;text-align:center;position:relative;background:linear-gradient(115deg,#f2f6ef,#fffefa 48%,#f2f6ef);border-top:1px solid var(--gold);border-bottom:1px solid var(--gold)}.date-panel:before,.date-panel:after{content:'✦';position:absolute;top:50%;transform:translateY(-50%);color:var(--gold);font-size:12px}.date-panel:before{left:12px}.date-panel:after{right:12px}.date-label{font:700 9px 'DM Sans',sans-serif;letter-spacing:.22em;text-transform:uppercase;color:var(--sage)}.date-day{font:500 clamp(27px,5.5vw,41px)/1.12 'Cormorant Garamond',serif;color:var(--sage-deep);margin:4px 0}.date-time{font:600 11px 'DM Sans',sans-serif;letter-spacing:.14em;color:var(--sage-dark)}
.countdown{max-width:470px;margin:0 auto 17px;text-align:center}.countdown-label{font:700 9px 'DM Sans',sans-serif;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}.countdown-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:7px}.count-unit{padding:8px 3px 7px;border:1px solid var(--line);background:#fbfcf8;border-radius:4px}.count-number{font:600 clamp(22px,4vw,29px)/1 'Cormorant Garamond',serif;color:var(--sage-deep);font-variant-numeric:tabular-nums}.count-name{font:700 8px 'DM Sans',sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--sage);margin-top:5px}.count-note{font:italic 12px 'Playfair Display',serif;color:var(--sage-dark);margin-top:7px}
.venue-section{text-align:center;padding:0 22px 17px}.section-kicker{font:700 9px 'DM Sans',sans-serif;letter-spacing:.22em;text-transform:uppercase;color:var(--sage)}.section-heading{font:500 clamp(29px,5.5vw,39px)/1.1 'Cormorant Garamond',serif;color:var(--sage-deep);margin:4px 0}.section-subtitle{font:italic 12px/1.5 'Playfair Display',serif;color:var(--muted)}.venue-card{max-width:580px;margin:11px auto 0;position:relative;text-align:center;padding:17px 15px 15px;background:linear-gradient(135deg,#f0f5ed,#fffefa 55%,#edf3e9);border:1px solid #c9d7c3;border-radius:7px;box-shadow:inset 0 0 0 4px #fffefa,inset 0 0 0 5px #e0d3ab}.venue-top{font:700 8px 'DM Sans',sans-serif;letter-spacing:.22em;color:var(--sage);text-transform:uppercase}.venue-name{font:500 clamp(32px,6vw,43px)/1.08 'Cormorant Garamond',serif;color:var(--sage-deep);margin:4px 0}.pin{display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:50%;background:var(--sage-dark);color:white;font-size:16px;margin:5px 0 7px}.address{font:500 12px/1.65 'DM Sans',sans-serif;color:#566759}.map-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;text-decoration:none;margin-top:12px;min-height:42px;padding:11px 17px;background:var(--sage-deep);color:#fff;border:1px solid var(--gold);border-radius:3px;font:600 10px 'DM Sans',sans-serif;letter-spacing:.035em;box-shadow:0 3px 0 #d7c89d}.map-btn:active,.contact:active{transform:translateY(1px)}.timing-pill{display:inline-flex;align-items:center;gap:10px;margin:12px auto 0;padding:9px 16px;border:1px solid var(--line);border-radius:40px;background:#fbfcf8}.clock-icon{font-size:19px;color:var(--sage)}.time-label{font:700 8px 'DM Sans',sans-serif;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);text-align:left}.time-value{font:500 21px/1.05 'Cormorant Garamond',serif;color:var(--sage-deep);text-align:left;margin-top:2px}
.rsvp{margin:0 14px 12px;padding:14px 13px 15px;background:#f1f5ed;border-top:1px solid var(--line);border-bottom:1px solid var(--line);text-align:center}.rsvp-title{font:500 31px/1.05 'Cormorant Garamond',serif;color:var(--sage-deep);margin:0 0 3px}.rsvp-intro{font:11px/1.5 'DM Sans',sans-serif;color:var(--muted);margin:0 0 10px}.contacts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;max-width:650px;margin:auto}.contact{min-width:0;text-decoration:none;border:1px solid #d3dfcd;background:#fffefa;padding:10px 7px;border-radius:4px;color:var(--sage-deep);transition:transform .15s}.contact-name{font:600 14px/1.3 'Cormorant Garamond',serif;display:block;overflow-wrap:anywhere}.contact-number{display:block;font:10px/1.5 'DM Sans',sans-serif;color:var(--muted);margin-top:3px;overflow-wrap:anywhere}.contact-action{display:inline-block;font:700 8px 'DM Sans',sans-serif;color:var(--sage-dark);margin-top:5px;letter-spacing:.12em;text-transform:uppercase}
.dua{text-align:center;padding:11px 18px 23px;position:relative}.dua-arabic{font-family:'Times New Roman',serif;direction:rtl;font-size:clamp(25px,5.2vw,34px);line-height:1.5;color:var(--sage-deep)}.dua-translation{font:italic 13px/1.55 'Playfair Display',serif;color:var(--muted);margin-top:2px}.footerline{font:700 8px 'DM Sans',sans-serif;letter-spacing:.18em;text-transform:uppercase;color:var(--sage);margin-top:9px}
@media(max-width:560px){.wrap{padding:5px}.card:before{inset:5px}.floral{font-size:36px;opacity:.42}.floral.tl{top:7px;left:7px}.floral.tr{top:7px;right:7px}.bismillah{padding:21px 13px 5px}.intro{padding:3px 18px 0}.intro-copy{font-size:16px;line-height:1.48;margin-top:7px}.couple{padding:2px 9px}.couple-name{font-size:clamp(45px,11vw,62px);margin-top:7px}.date-panel{margin:12px 11px 13px;padding:12px 18px}.date-day{font-size:clamp(27px,7vw,35px)}.countdown{margin:0 15px 14px}.countdown-grid{gap:5px}.count-unit{padding:8px 1px 6px}.count-name{font-size:7px;letter-spacing:.08em}.venue-section{padding:0 13px 14px}.venue-card{padding:15px 12px 14px}.address{font-size:11px}.map-btn{width:100%;max-width:300px}.rsvp{margin:0 8px 9px;padding:13px 8px 12px}.contacts{grid-template-columns:1fr;gap:6px;max-width:340px}.contact{display:grid;grid-template-columns:1fr auto;align-items:center;text-align:left;padding:8px 11px}.contact-name{font-size:15px}.contact-number{grid-column:1;grid-row:2;margin-top:1px}.contact-action{grid-column:2;grid-row:1/3;margin:0;font-size:8px}.dua{padding:10px 12px 20px}.footerline{font-size:7px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
</style>
</head>
<body><div class="wrap"><main class="card">
<span class="floral tl" aria-hidden="true">❀ ❧</span><span class="floral tr" aria-hidden="true">❀ ❧</span>
<header class="bismillah"><div class="arabic" lang="ar">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div><div class="translation">In the name of Allah, the Most Gracious, the Most Merciful</div><div class="divider-ornament">❧ ❀ ❧</div></header>
<section class="intro"><div class="eyebrow">With the blessings of Allah and our families</div><p class="intro-copy"><strong>Mr. &amp; Mrs. Arshad Rashid</strong> cordially invite you to join them in celebrating the Valima of their beloved son, with <strong>Areeba Fatima</strong>. Your gracious presence and prayers will make this joyous occasion even more memorable.</p></section>
<section class="couple" aria-label="The couple"><h1 class="couple-name">Muhammad Abdul Rashid</h1><div class="ampersand">&amp;</div><h2 class="couple-name">Areeba Fatima</h2><div class="divider-ornament">✧ ❀ ✧</div></section>
<section class="date-panel"><div class="date-label">Please save the date</div><div class="date-day">Friday, 13 November 2026</div><div class="date-time">7:30 PM · KARACHI, PAKISTAN</div></section>
<section class="countdown" aria-label="Countdown to the Valima"><div class="countdown-label">The celebration begins in</div><div class="countdown-grid"><div class="count-unit"><div class="count-number" id="days">--</div><div class="count-name">Days</div></div><div class="count-unit"><div class="count-number" id="hours">--</div><div class="count-name">Hours</div></div><div class="count-unit"><div class="count-number" id="minutes">--</div><div class="count-name">Minutes</div></div><div class="count-unit"><div class="count-number" id="seconds">--</div><div class="count-name">Seconds</div></div></div><div class="count-note" id="count-note">We look forward to celebrating with you</div></section>
<section class="venue-section"><div class="section-kicker">A place to gather · A memory to cherish</div><h2 class="section-heading">The Venue</h2><div class="section-subtitle">We would be delighted by your presence</div><div class="venue-card"><div class="venue-top">Join us at</div><div class="venue-name">Iconic Marquee</div><div class="pin" aria-hidden="true">⌖</div><div class="address">76, Block 14, Gulistan-e-Johar<br>Karachi, Pakistan</div><a class="map-btn" href="https://www.google.com/maps/search/?api=1&amp;query=Iconic+Marquee%2C+76%2C+Block+14%2C+Gulistan-e-Johar%2C+Karachi%2C+Pakistan" target="_blank" rel="noopener"><span aria-hidden="true">📍</span> Open venue in Google Maps ↗</a></div><div class="timing-pill"><span class="clock-icon" aria-hidden="true">◷</span><div><div class="time-label">Reception time</div><div class="time-value">7:30 in the evening</div></div></div></section>
<section class="rsvp"><h2 class="rsvp-title">Kindly RSVP</h2><p class="rsvp-intro">For any assistance, please contact one of our family hosts.</p><div class="contacts">
<a class="contact" href="https://wa.me/923323178261" target="_blank" rel="noopener"><span class="contact-name">Arshad Rashid</span><span class="contact-number">+92 332 3178261</span><span class="contact-action">WhatsApp ↗</span></a>
<a class="contact" href="https://wa.me/923357227454" target="_blank" rel="noopener"><span class="contact-name">Amna Arshad</span><span class="contact-number">+92 335 7227454</span><span class="contact-action">WhatsApp ↗</span></a>
<a class="contact" href="https://wa.me/923312151091" target="_blank" rel="noopener"><span class="contact-name">Daniyal Ayub</span><span class="contact-number">+92 331 2151091</span><span class="contact-action">WhatsApp ↗</span></a>
</div></section>
<footer class="dua"><div class="divider-ornament">❧ ❀ ❧</div><div class="dua-arabic" lang="ar">وَبَارَكَ اللَّهُ لَكُمَا</div><div class="dua-translation">May Allah bless this union with love, mercy and joy.</div><div class="footerline">With love and blessings · The Rashid Family</div></footer>
<span class="floral bl" aria-hidden="true">❀ ❧</span><span class="floral br" aria-hidden="true">❀ ❧</span>
</main></div>
<script>
(function(){
 const target = new Date('2026-11-13T19:30:00+05:00').getTime();
 const ids = {days:document.getElementById('days'),hours:document.getElementById('hours'),minutes:document.getElementById('minutes'),seconds:document.getElementById('seconds')};
 const note = document.getElementById('count-note');
 function update(){
  const remaining = target - Date.now();
  if(remaining <= 0){Object.values(ids).forEach(el=>el.textContent='00');note.textContent='Today is the day — we look forward to seeing you!';return;}
  const d=Math.floor(remaining/86400000),h=Math.floor((remaining%86400000)/3600000),m=Math.floor((remaining%3600000)/60000),s=Math.floor((remaining%60000)/1000);
  ids.days.textContent=String(d).padStart(2,'0');ids.hours.textContent=String(h).padStart(2,'0');ids.minutes.textContent=String(m).padStart(2,'0');ids.seconds.textContent=String(s).padStart(2,'0');
 }
 update();setInterval(update,1000);
})();
</script></body></html>'''

# A compact iframe height prevents a large blank area below the invitation.
components.html(INVITATION_HTML, height=2020, scrolling=True)
