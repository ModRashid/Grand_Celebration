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
.stApp { background:#edf2e9; }
.block-container { padding:0 !important; max-width:100% !important; }
iframe { border:0 !important; width:100% !important; }
</style>
""", unsafe_allow_html=True)

INVITATION_HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#e8eee5">
<title>Valima Invitation | Muhammad Abdul Rashid &amp; Areeba Fatima</title>
<style>
:root{--sage:#91a68e;--sage2:#6e886b;--deep:#344c3a;--pale:#edf2e9;--white:#fffefa;--gold:#b5a16e;--muted:#687768;--line:#cbd8c7}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--pale);color:var(--deep);font-family:Georgia,'Times New Roman',serif;-webkit-text-size-adjust:100%;}a,button{font:inherit}.wrap{width:100%;padding:12px;background:linear-gradient(135deg,#e5ede1,#f7f8f2 48%,#e3ebdf)}
.card{position:relative;max-width:850px;margin:0 auto;background:var(--white);border:1px solid #b9cbb5;outline:1px solid #d5e0d1;outline-offset:-7px;overflow:hidden;box-shadow:0 10px 35px #304b3412}
.floral{position:absolute;z-index:0;pointer-events:none;color:#91a88d;opacity:.72;font-size:clamp(30px,7vw,66px);line-height:1.2}.floral.tl{top:7px;left:10px;transform:rotate(-20deg)}.floral.tr{top:7px;right:10px;transform:scaleX(-1) rotate(-20deg)}.floral.bl{bottom:7px;left:10px;transform:scaleY(-1) rotate(-20deg)}.floral.br{bottom:7px;right:10px;transform:scale(-1) rotate(-20deg)}
.bismillah{text-align:center;padding:25px 16px 13px;position:relative;z-index:1}.arabic{font-family:'Times New Roman',serif;font-size:clamp(24px,5.8vw,36px);line-height:1.7;direction:rtl;color:var(--deep)}.translation{font:italic 11px/1.5 Arial,sans-serif;color:var(--muted);margin-top:1px}
.hero{text-align:center;position:relative;padding:10px 23px 20px;z-index:1}.kicker{font:600 10px/1.7 Arial,sans-serif;letter-spacing:.19em;text-transform:uppercase;color:var(--sage2)}.ornament{color:var(--sage2);font-size:20px;margin:7px 0}.hero h1{font-weight:400;font-size:clamp(34px,7.6vw,66px);line-height:1.02;letter-spacing:-.035em;margin:5px 0;color:var(--deep);overflow-wrap:anywhere}.amp{font-size:clamp(24px,4.5vw,36px);font-style:italic;color:var(--gold);margin:3px 0}.invite-copy{max-width:610px;margin:12px auto 0;font-size:clamp(14px,2.6vw,17px);line-height:1.72;color:#536654}.invite-copy strong{color:var(--deep);font-weight:600}.date-box{margin:19px auto 0;max-width:490px;padding:13px 12px 14px;border-top:1px solid var(--gold);border-bottom:1px solid var(--gold);color:var(--deep)}.date-small{font:600 10px Arial,sans-serif;letter-spacing:.21em;text-transform:uppercase;color:var(--sage2)}.date-main{font-size:clamp(21px,4.8vw,34px);line-height:1.25;margin:5px 0}.date-time{font:600 12px Arial,sans-serif;letter-spacing:.1em;color:var(--sage2)}
.content{position:relative;z-index:1;padding:0 22px 20px;text-align:center}.section-title{font-size:clamp(22px,4.5vw,30px);font-weight:400;margin:12px 0 6px;color:var(--deep)}.subtle{font:11px/1.6 Arial,sans-serif;color:var(--muted)}.venue{margin:12px auto 0;max-width:560px;padding:15px 12px 14px;border:1px solid var(--line);background:#f6f8f2;border-radius:5px}.venue-name{font-size:clamp(21px,4.5vw,28px);color:var(--deep);margin:3px 0 6px}.address{font:13px/1.65 Arial,sans-serif;color:#5b6b5b}.map-btn,.rsvp-btn{display:inline-flex;align-items:center;justify-content:center;text-decoration:none;border-radius:30px;min-height:43px;padding:11px 17px;font:600 11px Arial,sans-serif;letter-spacing:.035em;transition:transform .15s,background .15s}.map-btn{margin-top:12px;border:1px solid var(--sage2);color:white;background:var(--sage2)}.map-btn:active,.rsvp-btn:active{transform:scale(.98)}.timing{display:flex;justify-content:center;gap:10px;align-items:center;margin:14px auto 0;padding:10px 14px;max-width:340px;background:#edf3e9;border-radius:5px}.clock{font-size:23px;color:var(--sage2)}.time-label{font:600 9px Arial,sans-serif;text-transform:uppercase;letter-spacing:.17em;color:var(--sage2)}.time-value{font-size:19px;color:var(--deep);margin-top:3px}
.rsvp{padding:14px 18px 17px;margin:2px 12px 12px;background:#f2f6ef;border-top:1px solid var(--line);border-bottom:1px solid var(--line);text-align:center;position:relative;z-index:1}.rsvp-title{font-size:23px;font-weight:400;margin:0 0 5px}.rsvp-intro{font:11px/1.5 Arial,sans-serif;color:var(--muted);margin:0 0 11px}.contacts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;max-width:660px;margin:auto}.contact{min-width:0;text-decoration:none;border:1px solid #d2dfce;background:#fffefa;padding:10px 6px;border-radius:5px;color:var(--deep)}.contact-name{font-size:13px;line-height:1.4;display:block;overflow-wrap:anywhere}.contact-number{display:block;font:10px/1.5 Arial,sans-serif;color:var(--muted);margin-top:4px;overflow-wrap:anywhere}.contact-action{display:block;font:600 9px Arial,sans-serif;color:var(--sage2);margin-top:5px;letter-spacing:.08em;text-transform:uppercase}
.dua{text-align:center;padding:17px 18px 25px;position:relative;z-index:1}.dua-arabic{font-family:'Times New Roman',serif;direction:rtl;font-size:clamp(23px,5vw,32px);line-height:1.7;color:var(--deep)}.dua-translation{font:italic 12px/1.6 Arial,sans-serif;color:var(--muted);margin-top:3px}.footerline{font:9px Arial,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--sage2);margin-top:12px}
@media(max-width:560px){.wrap{padding:7px}.card{outline-offset:-5px}.bismillah{padding:23px 14px 10px}.hero{padding:8px 17px 17px}.hero h1{font-size:clamp(33px,9vw,48px)}.invite-copy{font-size:14px;line-height:1.65}.date-box{margin-top:15px;padding:11px 8px 12px}.content{padding:0 13px 15px}.venue{padding:13px 9px}.rsvp{margin:0 7px 8px;padding:13px 8px 14px}.contacts{grid-template-columns:1fr;gap:7px;max-width:330px}.contact{display:grid;grid-template-columns:1fr auto;align-items:center;text-align:left;padding:9px 12px}.contact-name{font-size:13px}.contact-number{grid-column:1;grid-row:2;margin-top:2px}.contact-action{grid-column:2;grid-row:1/3;margin:0;font-size:9px}.dua{padding:15px 14px 22px}.floral{font-size:35px;opacity:.48}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
</style>
</head>
<body><div class="wrap"><main class="card">
  <span class="floral tl" aria-hidden="true">❀ ❧</span><span class="floral tr" aria-hidden="true">❀ ❧</span>
  <div class="bismillah"><div class="arabic" lang="ar">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div><div class="translation">In the name of Allah, the Most Gracious, the Most Merciful</div></div>
  <section class="hero">
    <div class="kicker">Together with their families</div><div class="ornament">❧ ❀ ❧</div>
    <h1>Muhammad Abdul Rashid</h1><div class="amp">&amp;</div><h1>Areeba Fatima</h1>
    <p class="invite-copy"><strong>Mr. &amp; Mrs. Arshad Rashid</strong> cordially invite you to join them in celebrating the Valima of their beloved son, <strong>Muhammad Abdul Rashid</strong>, with <strong>Areeba Fatima</strong>. Your presence and prayers will make this special occasion truly memorable.</p>
    <div class="date-box"><div class="date-small">Kindly save the date</div><div class="date-main">Friday, 13 November 2026</div><div class="date-time">7:30 IN THE EVENING</div></div>
  </section>
  <section class="content">
    <div class="ornament">✧ ❀ ✧</div><h2 class="section-title">The Celebration</h2><div class="subtle">An evening of love, joy and family blessings</div>
    <div class="venue"><div class="subtle">YOU ARE WARMLY INVITED TO</div><div class="venue-name">Iconic Marquee</div><div class="address">76, Block 14, Gulistan-e-Johar<br>Karachi, Pakistan</div><a class="map-btn" href="https://www.google.com/maps/search/?api=1&amp;query=Iconic+Marquee%2C+76+Block+14%2C+Gulistan-e-Johar%2C+Karachi%2C+Pakistan" target="_blank" rel="noopener">⌖ &nbsp; Open location in Google Maps</a></div>
    <div class="timing"><span class="clock">◷</span><div><div class="time-label">Event timing</div><div class="time-value">7:30 PM</div></div></div>
  </section>
  <section class="rsvp"><h2 class="rsvp-title">Kindly RSVP</h2><p class="rsvp-intro">Please contact any of our family hosts for assistance.</p><div class="contacts">
    <a class="contact" href="https://wa.me/923323178261" target="_blank" rel="noopener"><span class="contact-name">Arshad Rashid</span><span class="contact-number">+92 332 3178261</span><span class="contact-action">WhatsApp ↗</span></a>
    <a class="contact" href="https://wa.me/923357227454" target="_blank" rel="noopener"><span class="contact-name">Amna Arshad</span><span class="contact-number">+92 335 7227454</span><span class="contact-action">WhatsApp ↗</span></a>
    <a class="contact" href="https://wa.me/923312151091" target="_blank" rel="noopener"><span class="contact-name">Daniyal Ayub</span><span class="contact-number">+92 331 2151091</span><span class="contact-action">WhatsApp ↗</span></a>
  </div></section>
  <section class="dua"><div class="ornament">❧ ❀ ❧</div><div class="dua-arabic" lang="ar">وَبَارَكَ اللَّهُ لَكُمَا</div><div class="dua-translation">May Allah bless this union with love, mercy and joy.</div><div class="footerline">With love and blessings · The Rashid Family</div></section>
  <span class="floral bl" aria-hidden="true">❀ ❧</span><span class="floral br" aria-hidden="true">❀ ❧</span>
</main></div></body></html>'''

components.html(INVITATION_HTML, height=2500, scrolling=True)
