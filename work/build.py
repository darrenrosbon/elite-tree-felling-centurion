import re
src = open('../clean yard co/index.html', encoding='utf8').read()
head, rest = src.split('<header class="site-head">', 1)
_, script = rest.split('<script>', 1)

# ---------- head / css ----------
colors = {'#0a1f44': '#0f2418', '#11305f': '#173523', '#234a86': '#2f5c40', '#0e2c59': '#133020', '#061532': '#08170e',
          '#8fe06b': '#f5a524', '#07183a': '#1a1205', '#eaf1fb': '#eef5ec', '#b6c8e4': '#b9cdbb', '#f1f6fd': '#f1f7ef',
          '#bccbe3': '#bfd1c0', '#0e3470': '#14301f', '#d6e3f5': '#dfe9dc', '#d3e0f3': '#d3e3d3', '#061f4a': '#06210f',
          '#a3ea84': '#f8b84a'}
for a, b in colors.items():
    head = head.replace(a, b)
for a, b in {'rgba(7, 25, 58,': 'rgba(6, 22, 12,', 'rgba(5, 16, 40,': 'rgba(4, 14, 8,', 'rgba(8, 28, 64,': 'rgba(10, 30, 18,',
             'rgba(14, 52, 112,': 'rgba(20, 60, 34,', 'rgba(10, 31, 68,': 'rgba(15, 36, 24,',
             'rgba(143, 224, 107,': 'rgba(245, 165, 36,'}.items():
    head = head.replace(a, b)
head = head.replace('<title>The Clean Yard Co. | Landscaping and Property Maintenance in Diepsloot</title>',
                    '<title>Elite Tree Felling Centurion | Tree Felling and Tree Removal in Centurion</title>')
head = head.replace('Irrigation, plumbing, renovations, painting and yard care in Diepsloot and surrounds. Free quotes, call or WhatsApp 071 200 7806.',
                    'Tree felling, tree trimming and branch removal in Centurion and Pretoria. Open 24 hours, free quotes, call or WhatsApp 065 610 9056.')
head = re.sub(r'<link rel="preload"[^>]*>',
              '<link rel="preload" as="image" imagesrcset="img/hero-3-480.webp 480w, img/hero-3-800.webp 800w, img/hero-3-1200.webp 1200w" imagesizes="(max-width: 767px) 200vw, 100vw" fetchpriority="high">', head)
EXTRA = '''.hero-slides .hs { animation: none !important; clip-path: none !important; }
.work-gallery { grid-template-columns: 1fr 1fr; }
.work-gallery figure:last-child { grid-column: 1 / -1; }
.work-gallery figure:last-child img { aspect-ratio: 4 / 3; }
@media (min-width: 768px) {
  .gallery.work-gallery { grid-template-columns: repeat(6, 1fr); }
  .gallery.work-gallery figure { grid-column: span 2; }
  .gallery.work-gallery figure:nth-child(n+4) { grid-column: span 3; }
  .gallery.work-gallery figure:nth-child(n+4) img { aspect-ratio: 4 / 3; }
}
.review .avatar { font: 800 1.05rem/1 "Sora", sans-serif; }
'''
head = head.replace('</style>', EXTRA + '</style>', 1)
head = head.replace('.hs3 { z-index: 3; object-position: 50% 80%;', '.hs3 { z-index: 3; object-position: 50% 30%;')
head = head.replace('.hs1 { z-index: 1; object-position: 30% 50%; }', '.hs1 { z-index: 1; object-position: 50% 40%; }')
head = head.replace('.hs2 { z-index: 2; clip-path', '.hs2 { z-index: 2; object-position: 50% 55%; clip-path')
head = head.replace('</defs></svg>', '<symbol id="i-tree" viewBox="0 0 24 24"><path d="M12 2l5.5 7.5h-3L19 16h-5v5h-4v-5H5l4.5-6.5h-3z" fill="currentColor"/></symbol><symbol id="i-saw" viewBox="0 0 24 24"><path d="M3 15l4-9 3 2 3-4 3 3 5-1-2 9-3 1 1 2h-3l-1-2-4 1-1 2H5l1-3z" fill="currentColor"/></symbol><symbol id="i-truck" viewBox="0 0 24 24"><path d="M2 6h12v9H2zm13 3h4l3 3v3h-7zM6 17.5a2 2 0 1 0 .01 0zm11 0a2 2 0 1 0 .01 0z" fill="currentColor"/></symbol><symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 2l8 3v6c0 5-3.4 9-8 11-4.6-2-8-6-8-11V5z" fill="currentColor"/></symbol></defs></svg>', 1)

PH = '+27656109056'
DISP = '065 610 9056'


def svc(img, alt, icon, title, desc, chips, pos):
    ch = ''.join(f'\n              <li><svg class="ico" aria-hidden="true"><use href="#i-check"/></svg>{c}</li>' for c in chips)
    return f'''        <article class="svc reveal">
          <div class="media"><img class="img-fade" decoding="async" loading="lazy" src="img/work-{img}-800.webp" srcset="img/work-{img}-800.webp 800w, img/work-{img}-1200.webp 1200w" sizes="(max-width: 767px) 100vw, 50vw" alt="{alt}" style="object-position: {pos}"><span class="svc-badge" aria-hidden="true"><svg class="ico"><use href="#{icon}"/></svg></span></div>
          <div class="svc-body">
            <h3>{title}</h3>
            <p>{desc}</p>
            <ul class="chips">{ch}
            </ul>
            <a class="btn btn-solid svc-cta" href="#quote" data-service="{title}">Get a quote<svg class="ico" aria-hidden="true"><use href="#i-arrow-right"/></svg></a>
          </div>
        </article>

'''


S = [('4', 'Tall tree cut back to a trunk beside a brick wall', 'i-tree', 'Tree felling', 'Safe, controlled removal of tall and difficult trees, taken down in sections where space is tight.', ['Large trees', 'Sectional felling', 'Safe working'], '50% 35%'),
     ('1', 'Tall palm trees beside a garden wall and lawn', 'i-saw', 'Tree trimming and pruning', 'Palms and garden trees trimmed back to keep your property, wall and power lines clear.', ['Palm trimming', 'Crown reduction', 'Pruning'], '50% 30%'),
     ('3', 'Tall palms next to a house with a manicured lawn', 'i-shield', 'Trees near homes and walls', 'Careful removal of trees overhanging driveways, roofs and boundary walls, with your property protected.', ['Overhanging trees', 'Driveways and roofs', 'Boundary walls'], '50% 40%'),
     ('5', 'Crew loading cut branches onto a truck', 'i-truck', 'Branch and waste removal', 'Cut branches and garden waste loaded and taken away, so you are left with a clean yard.', ['Branches cleared', 'Garden waste', 'Site left tidy'], '50% 50%')]

B = []
B.append(f'''<header class="site-head">
  <div class="wrap head-in">
    <a class="brand" href="#top" aria-label="Elite Tree Felling Centurion, home">
      <span class="wm"><span class="wm-main wm-long">ELITE TREE FELLING</span><span class="wm-sub">Centurion &amp; Pretoria</span></span>
    </a>
    <nav class="nav-desktop" aria-label="Main">
      <a href="#services">Services</a>
      <a href="#work">Our work</a>
      <a href="#reviews">Reviews</a>
      <a href="#quote">Quote</a>
    </nav>
    <a class="btn btn-solid head-cta" href="tel:{PH}"><svg class="ico" aria-hidden="true"><use href="#i-phone"/></svg>{DISP}</a>
    <button class="burger" id="burger" aria-expanded="false" aria-controls="menu" aria-label="Open menu">
      <svg class="ico" aria-hidden="true"><use href="#i-list"/></svg>
    </button>
  </div>
</header>

<nav class="nav-mobile" id="menu" aria-label="Mobile">
  <a class="link" href="#services">Services <svg class="ico" aria-hidden="true"><use href="#i-arrow-right"/></svg></a>
  <a class="link" href="#work">Our work <svg class="ico" aria-hidden="true"><use href="#i-arrow-right"/></svg></a>
  <a class="link" href="#reviews">Reviews <svg class="ico" aria-hidden="true"><use href="#i-arrow-right"/></svg></a>
  <a class="link" href="#quote">Quote <svg class="ico" aria-hidden="true"><use href="#i-arrow-right"/></svg></a>
  <a class="btn btn-solid" href="tel:{PH}"><svg class="ico" aria-hidden="true"><use href="#i-phone"/></svg>Call {DISP}</a>
</nav>

<main id="top">

  <section class="hero ph" aria-labelledby="hero-title">
    <div class="hero-slides" aria-hidden="true">
      <img class="hs hs1" src="img/hero-3-800.webp" srcset="img/hero-3-480.webp 480w, img/hero-3-800.webp 800w, img/hero-3-1200.webp 1200w" sizes="(max-width: 767px) 200vw, 100vw" width="1200" height="1600" alt="Tall palms beside a house with a manicured lawn and flower beds" fetchpriority="high" decoding="async">
    </div>
    <div class="wrap hero-in">
      <div class="hero-plate" aria-hidden="true"><b>ELITE TREE FELLING</b><span>Centurion &amp; Pretoria</span></div>
      <h1 id="hero-title"><span class="sr-only">Elite Tree Felling Centurion: tree felling, tree trimming and branch removal in Centurion, open 24 hours</span><span class="words" aria-hidden="true"><span>Felling.</span><span>Trimming.</span><span>Cleared.</span></span></h1>
      <p>Safe tree felling, trimming and branch removal for homes and businesses in Centurion and Pretoria. Open 24 hours. Call or WhatsApp for a free quote.</p>
      <div class="hero-cta">
        <a class="btn btn-light" href="#quote"><svg class="ico" aria-hidden="true"><use href="#i-whatsapp-logo"/></svg>Get a free quote</a>
        <a class="btn btn-outline" href="tel:{PH}"><svg class="ico" aria-hidden="true"><use href="#i-phone"/></svg>Call {DISP}</a>
      </div>
    </div>
  </section>

  <section class="facts" aria-label="Quick facts">
    <div class="wrap">
      <ul>
        <li>
          <span class="f-ico"><svg class="ico" aria-hidden="true"><use href="#i-map-pin"/></svg></span>
          <span class="f-text"><span class="f-lab">Based in</span><span class="f-val">Centurion</span></span>
        </li>
        <li>
          <span class="f-ico"><svg class="ico" aria-hidden="true"><use href="#i-clock"/></svg></span>
          <span class="f-text"><span class="f-lab">Open</span><span class="f-val">24 hours</span></span>
        </li>
        <li>
          <span class="f-ico"><svg class="ico" aria-hidden="true"><use href="#i-phone"/></svg></span>
          <span class="f-text"><span class="f-lab">Call or WhatsApp</span><a class="f-val" href="tel:{PH}">{DISP}</a></span>
          <svg class="ico f-arrow" aria-hidden="true"><use href="#i-arrow-up-right"/></svg>
        </li>
      </ul>
    </div>
  </section>

  <section class="section" id="services">
    <div class="wrap">
      <h2 class="reveal">Our services</h2>
      <p class="lead reveal">Trees taken down safely and the site left clean.</p>
      <div class="services-grid">
''')
B.extend(svc(*s) for s in S)
B.append('''      </div>
    </div>
  </section>

  <section class="section" id="work">
    <div class="wrap">
      <h2 class="reveal">Our work</h2>
      <p class="lead reveal">Recent jobs around Centurion.</p>
      <div class="gallery work-gallery reveal">
''')
alts = ['Tall palm trees beside a garden wall and lawn', 'Palm trees above a boundary wall with a crew member working', 'Tall palms next to a house with a manicured lawn', 'Tall tree cut back to a trunk beside a brick wall', 'Crew loading cut branches onto a truck']
tags = ['Palm trimming', 'Palm trimming', 'Garden trees', 'Tree felling', 'Clean-up']
for i in range(1, 6):
    B.append(f'        <figure><img class="img-fade" loading="lazy" decoding="async" src="img/work-{i}-600.webp" srcset="img/work-{i}-600.webp 600w, img/work-{i}-800.webp 800w, img/work-{i}-1200.webp 1200w" sizes="(max-width: 767px) 50vw, 33vw" alt="{alts[i-1]}"><figcaption class="tag">{tags[i-1]}</figcaption></figure>\n')
B.append('''      </div>
    </div>
  </section>

  <section class="section" id="reviews">
    <div class="wrap">
      <h2 class="reveal">What customers say</h2>
      <p class="lead reveal">5.0 stars from 6 reviews on Google.</p>
      <div class="reviews-grid">
''')
R = [('Tantaswa Mkohlwa', 'TM', '3 months ago', 'The guys did a fantastic job removing a large tree that was hanging over our driveway. They were friendly, professional and worked really well together. Everything was cleaned up before they left and we couldn&rsquo;t be happier with the result.'),
     ('Inako Noqoko', 'IN', '10 months ago', 'Superb job done. They did the job with a reasonable price all within 24 hours! They are extremely professional, efficient and polite.'),
     ('Erom Chris', 'EC', '2 years ago', 'They did an excellent job, were on time and professional. I&rsquo;d definitely call them again if I need more tree work done.')]
for n, i, t, q in R:
    B.append(f'        <article class="review reveal"><div class="rev-head"><span class="avatar" aria-hidden="true">{i}</span><div class="rev-who"><b>{n}</b><span>Google review &middot; {t}</span></div></div><div class="stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><blockquote>&ldquo;{q}&rdquo;</blockquote></article>\n')
B.append(f'''      </div>
    </div>
  </section>

  <section class="section process ph" aria-labelledby="process-title">
    <img class="process-bg img-fade" src="img/bg-800.webp" srcset="img/bg-800.webp 800w, img/bg-1200.webp 1200w, img/bg-1600.webp 1600w" sizes="(max-width: 767px) 220vw, 100vw" width="1600" height="1067" alt="" decoding="async" loading="lazy">
    <div class="wrap">
      <h2 id="process-title" class="reveal">Three simple steps</h2>
      <ol class="process-list">
        <li class="reveal">
          <div class="p-ico"><svg class="ico" aria-hidden="true"><use href="#i-whatsapp-logo"/></svg></div>
          <h3>Call or message</h3>
          <p>Tell us which tree needs to come down and send a photo if you can.</p>
        </li>
        <li class="reveal">
          <div class="p-ico"><svg class="ico" aria-hidden="true"><use href="#i-clipboard-text"/></svg></div>
          <h3>Agree the price</h3>
          <p>You get a clear quote for the job before any work starts.</p>
        </li>
        <li class="reveal">
          <div class="p-ico"><svg class="ico" aria-hidden="true"><use href="#i-tree"/></svg></div>
          <h3>Tree down, site clean</h3>
          <p>We fell the tree safely and clear away the branches when we are finished.</p>
        </li>
      </ol>
    </div>
  </section>

  <section class="section" id="why">
    <div class="wrap why-grid">
      <div class="why-head reveal">
        <h2>Why Centurion calls Elite Tree Felling</h2>
        <p class="lead">Professional, polite and fast. Tree work for homes and businesses around Centurion and Pretoria.</p>
      </div>
      <ul class="why-list reveal">
          <li>
            <span class="avatar" aria-hidden="true"><svg class="ico"><use href="#i-shield"/></svg></span>
            <div><h3>Safe, professional crew</h3><p>Customers describe the team as friendly, professional and great at working together.</p></div>
          </li>
          <li>
            <span class="avatar" aria-hidden="true"><svg class="ico"><use href="#i-clock"/></svg></span>
            <div><h3>Open 24 hours</h3><p>On time and quick to get the job done, often all within 24 hours.</p></div>
          </li>
          <li>
            <span class="avatar" aria-hidden="true"><svg class="ico"><use href="#i-truck"/></svg></span>
            <div><h3>Cleaned up before we leave</h3><p>Branches and waste are cleared away, so you are left with a neat yard at a reasonable price.</p></div>
          </li>
      </ul>
      <div class="why-cta reveal"><a class="btn btn-solid" href="tel:{PH}"><svg class="ico" aria-hidden="true"><use href="#i-phone"/></svg>Call {DISP}</a></div>
    </div>
  </section>

  <section class="section areas" id="areas">
    <div class="wrap">
      <div class="areas-head reveal">
        <h2>Where we work</h2>
        <p class="lead">Not on the list? Send us a message and we will tell you if we can get to you.</p>
      </div>
      <ul class="suburbs reveal">
''')
for s in ['Centurion', 'Pretoria', 'Irene', 'Lyttelton', 'Eldoraigne', 'Wierda Park', 'Highveld', 'Midrand']:
    B.append(f'        <li><svg class="ico" aria-hidden="true"><use href="#i-map-pin"/></svg>{s}</li>\n')
B.append(f'''      </ul>
      <div class="contact-strip reveal">
        <div><span class="f-ico"><svg class="ico" aria-hidden="true"><use href="#i-phone"/></svg></span><span class="cs-text"><span class="cs-lab">Phone and WhatsApp</span><a class="cs-val" href="tel:{PH}">+27 65 610 9056</a></span></div>
        <div><span class="f-ico"><svg class="ico" aria-hidden="true"><use href="#i-clock"/></svg></span><span class="cs-text"><span class="cs-lab">Hours</span><span class="cs-val">Open 24 hours</span></span></div>
        <div><span class="f-ico"><svg class="ico" aria-hidden="true"><use href="#i-map-pin"/></svg></span><span class="cs-text"><span class="cs-lab">Area</span><span class="cs-val">Centurion, Pretoria</span></span></div>
      </div>
    </div>
  </section>

  <section class="section" id="quote">
    <div class="wrap">
      <div class="quote-card reveal">
        <div class="map" id="map" data-src="https://www.google.com/maps?q=-25.8601024,28.076185&z=11&output=embed">
          <span class="map-pin" aria-hidden="true"><svg class="ico"><use href="#i-map-pin"/></svg></span>
          <a class="map-open" href="https://www.google.com/maps/place/?q=place_id:ChIJ24A-EKuQkSgRMuoE6NxC5nA" target="_blank" rel="noopener">Open in Maps</a>
          <button class="map-load" type="button"><svg class="ico" aria-hidden="true"><use href="#i-hand-tap"/></svg>Interactive map</button>
          <div class="map-pill"><span class="ico-tile"><svg class="ico" aria-hidden="true"><use href="#i-map-pin"/></svg></span><b>Centurion and surrounds</b></div>
        </div>
        <div class="quote-body">
          <div class="quote-head">
            <div>
              <h2>Book a free quote</h2>
              <p class="lead">Fill in the form and it opens in WhatsApp, ready to send to Elite Tree Felling Centurion. Not sure we cover your area? Ask anyway.</p>
            </div>
            <ul class="quote-facts">
              <li><svg class="ico" aria-hidden="true"><use href="#i-check"/></svg>Free quotes</li>
              <li><svg class="ico" aria-hidden="true"><use href="#i-phone"/></svg><a href="tel:{PH}">+27 65 610 9056</a></li>
            </ul>
          </div>
          <form id="quote-form" novalidate>
            <div class="q-grid">
              <div class="field">
                <label for="f-name">Your name</label>
                <input id="f-name" name="name" type="text" autocomplete="name" placeholder="e.g. Sipho Dlamini" required>
                <span class="err">Please enter your name.</span>
              </div>
              <div class="field">
                <label for="f-suburb">Suburb</label>
                <input id="f-suburb" name="suburb" type="text" autocomplete="address-level3" placeholder="e.g. Eldoraigne" required>
                <span class="err">Please enter your suburb.</span>
              </div>
              <div class="field full">
                <label for="f-service">What do you need?</label>
                <select id="f-service" name="service" required>
                  <option value="">Choose a service</option>
                  <option>Tree felling</option>
                  <option>Tree trimming and pruning</option>
                  <option>Trees near homes and walls</option>
                  <option>Branch and waste removal</option>
                  <option>Something else</option>
                </select>
                <span class="err">Please choose a service.</span>
              </div>
              <div class="field full">
                <label for="f-msg">Details (optional)</label>
                <textarea id="f-msg" name="message" placeholder="Tell us about the tree, for example the type, height and where it is."></textarea>
              </div>
              <div class="full">
                <button class="btn btn-wa" type="submit"><svg class="ico" aria-hidden="true"><use href="#i-whatsapp-logo"/></svg>Send on WhatsApp</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a class="brand brand-stack" href="#top">
          <span class="wm"><span class="wm-main wm-long">ELITE TREE FELLING</span><span class="wm-sub">Centurion &amp; Pretoria</span></span>
        </a>
        <p class="foot-blurb" style="margin-top:10px;max-width:34ch;font-size:.95rem">Tree felling, trimming and branch removal in Centurion and surrounds.</p>
      </div>
      <div class="foot-contact">
        <h3>Contact</h3>
        <ul>
          <li><a href="tel:{PH}">+27 65 610 9056</a></li>
          <li>Centurion, Pretoria</li>
          <li>Open 24 hours</li>
        </ul>
      </div>
      <div class="foot-jump">
        <h3>Jump to</h3>
        <ul>
          <li><a href="#services">Services</a></li>
          <li><a href="#work">Our work</a></li>
          <li><a href="#reviews">Reviews</a></li>
          <li><a href="#areas">Areas</a></li>
          <li><a href="#quote">Quote</a></li>
        </ul>
      </div>
    </div>
    <p class="legal">&copy; <span id="yr">2026</span> Elite Tree Felling Centurion. Preview mockup.</p>
  </div>
</footer>

<div class="fab-stack" role="group" aria-label="Quick contact">
  <a class="fab fab-call" href="tel:{PH}" aria-label="Call us"><svg class="fab-ico" aria-hidden="true"><use href="#i-tb-phone"/></svg></a>
  <a class="fab fab-wa" href="https://wa.me/27656109056?text=Hi%20Elite%20Tree%20Felling%2C%20I%20would%20like%20a%20free%20quote." target="_blank" rel="noopener" aria-label="Message us on WhatsApp"><svg class="fab-ico" aria-hidden="true"><use href="#i-tb-wa"/></svg></a>
</div>

<script>''')
script = script.replace('27712007806', '27656109056').replace('Hi The Clean Yard Co., I', 'Hi Elite Tree Felling, I').replace('Interactive map of Diepsloot', 'Interactive map of Centurion').replace('var fast = conn && !conn.saveData && conn.effectiveType === "4g";', 'var fast = !(conn && (conn.saveData || conn.effectiveType !== "4g"));')
open('index.html', 'w', encoding='utf8').write(head + ''.join(B) + script)
