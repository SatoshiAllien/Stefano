#!/usr/bin/env python3
"""Generate multilingual IT/EN site for Stefano Ciancimino portfolio."""
import os
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://satoshiallien.github.io/Stefano"
TODAY = date.today().isoformat()
ASSET = "../"

NAV = {
    "it": [
        ("index.html", "Home"),
        ("about.html", "Chi Sono"),
        ("ai-blockchain.html", "AI & Blockchain"),
        ("tech.html", "Tech"),
        ("hospitality.html", "Hospitality"),
        ("fitness.html", "Fitness"),
        ("portfolio.html", "Portfolio"),
        ("blog.html", "Blog"),
        ("contact.html", "Contatti"),
    ],
    "en": [
        ("index.html", "Home"),
        ("about.html", "About Me"),
        ("ai-blockchain.html", "AI & Blockchain"),
        ("tech.html", "Tech"),
        ("hospitality.html", "Hospitality"),
        ("fitness.html", "Fitness"),
        ("portfolio.html", "Portfolio"),
        ("blog.html", "Blog"),
        ("contact.html", "Contact"),
    ],
}

UI = {
    "it": {
        "logo_sub": "Fraud · Blockchain · AI",
        "theme_aria": "Cambia tema",
        "menu_aria": "Menu",
        "cta": "Contattami",
        "download_cv": "Scarica CV",
        "read_more": "Scopri di più",
        "read_article": "Leggi articolo",
        "all_articles": "Tutti gli articoli",
        "footer_tagline": "Fraud & Risk Analyst · Blockchain Researcher · AI Specialist",
        "footer_rights": "Tutti i diritti riservati.",
        "form_success": "Grazie per il messaggio! Ti risponderò entro 24 ore lavorative.",
        "print_cv": "Stampa / Salva PDF",
        "lang_it_aria": "Versione italiana",
        "lang_en_aria": "English version",
    },
    "en": {
        "logo_sub": "Fraud · Blockchain · AI",
        "theme_aria": "Toggle theme",
        "menu_aria": "Menu",
        "cta": "Contact Me",
        "download_cv": "Download CV",
        "read_more": "Learn more",
        "read_article": "Read article",
        "all_articles": "All articles",
        "footer_tagline": "Fraud & Risk Analyst · Blockchain Researcher · AI Specialist",
        "footer_rights": "All rights reserved.",
        "form_success": "Thank you for your message! I will reply within 24 business hours.",
        "print_cv": "Print / Save PDF",
        "lang_it_aria": "Italian version",
        "lang_en_aria": "English version",
    },
}

ARTICLES = [
    {
        "slug": "antifrode-pagamenti",
        "cat": {"it": "Antifrode & Sicurezza", "en": "Fraud & Security"},
        "title": {
            "it": "Pattern fraudolenti nei pagamenti digitali: come identificarli",
            "en": "Fraudulent patterns in digital payments: how to identify them",
        },
        "desc": {
            "it": "Framework pratico per rilevare e mitigare frodi nelle transazioni online.",
            "en": "Practical framework to detect and mitigate fraud in online transactions.",
        },
        "date": "2026-06-15",
        "read": {"it": "6 min", "en": "6 min"},
        "body": {
            "it": """<p>Dopo oltre otto anni nel settore antifrode presso PayPal, ho osservato che i pattern evolvono rapidamente, ma alcuni schemi ricorrenti restano costanti.</p>
<h2>1. Account takeover (ATO)</h2><p>Segnali tipici: cambio improvviso credenziali, login da geolocalizzazioni inconsuete, transazioni ad alto valore subito dopo.</p>
<h2>2. Friendly fraud</h2><p>Il cliente legittimo contesta una transazione valida. Richiede analisi dello storico e delle comunicazioni.</p>
<h2>3. Reti multi-account</h2><p>Account collegati tramite device fingerprint, IP o metodi di pagamento. L'investigazione cross-account è fondamentale.</p>
<h2>Best practice</h2><ul><li>Soglie di alert basate su dati storici</li><li>Documentazione investigativa rigorosa</li><li>Collaborazione con legal, product e customer support</li></ul>""",
            "en": """<p>After more than eight years in fraud prevention at PayPal, I have seen patterns evolve quickly — yet several recurring schemes remain constant.</p>
<h2>1. Account takeover (ATO)</h2><p>Typical signals: sudden credential changes, logins from unusual locations, high-value transactions immediately afterwards.</p>
<h2>2. Friendly fraud</h2><p>A legitimate customer disputes a valid transaction. Requires purchase history and communication analysis.</p>
<h2>3. Multi-account networks</h2><p>Accounts linked via device fingerprint, IP or payment methods. Cross-account investigation is essential.</p>
<h2>Best practices</h2><ul><li>Alert thresholds based on historical data</li><li>Rigorous investigation documentation</li><li>Collaboration with legal, product and customer support</li></ul>""",
        },
    },
    {
        "slug": "defi-2026",
        "cat": {"it": "Blockchain & Crypto", "en": "Blockchain & Crypto"},
        "title": {
            "it": "DeFi nel 2026: rischi, opportunità e trend emergenti",
            "en": "DeFi in 2026: risks, opportunities and emerging trends",
        },
        "desc": {
            "it": "Panoramica degli ecosistemi decentralizzati e vulnerabilità smart contract.",
            "en": "Overview of decentralised ecosystems and smart contract vulnerabilities.",
        },
        "date": "2026-06-08",
        "read": {"it": "8 min", "en": "8 min"},
        "body": {
            "it": """<p>La ricerca blockchain dal 2017 mi ha portato ad analizzare protocolli DeFi, CeFi e NFT con approccio analitico e risk-oriented.</p>
<h2>Rischi principali</h2><ul><li>Vulnerabilità smart contract e exploit</li><li>Controparte e custodia in CeFi</li><li>Regolamentazione in evoluzione</li></ul>
<h2>Opportunità</h2><p>Tokenizzazione, pagamenti cross-border, automazione on-chain e integrazione istituzionale stanno maturando.</p>""",
            "en": """<p>Blockchain research since 2017 has led me to analyse DeFi, CeFi and NFT ecosystems with an analytical, risk-oriented approach.</p>
<h2>Key risks</h2><ul><li>Smart contract vulnerabilities and exploits</li><li>Counterparty and custody risks in CeFi</li><li>Evolving regulation</li></ul>
<h2>Opportunities</h2><p>Tokenisation, cross-border payments, on-chain automation and institutional integration are maturing.</p>""",
        },
    },
    {
        "slug": "ai-ollama",
        "cat": {"it": "AI & Automazione", "en": "AI & Automation"},
        "title": {
            "it": "Agenti AI locali per operations: guida pratica con Ollama",
            "en": "Local AI agents for operations: practical guide with Ollama",
        },
        "desc": {
            "it": "Configurazione di modelli locali su WSL per automazione e analisi.",
            "en": "Setting up local models on WSL for automation and analysis.",
        },
        "date": "2026-06-01",
        "read": {"it": "7 min", "en": "7 min"},
        "body": {
            "it": """<p>Esperienza con Ollama, WSL, Llama, Qwen e Mistral per workflow privati e automazioni AI.</p>
<h2>Setup consigliato</h2><ul><li>WSL2 con Ubuntu su Windows</li><li>Ollama + modelli quantizzati</li><li>GPU acceleration quando disponibile</li></ul>
<h2>Use case</h2><p>Prompt engineering, reportistica, analisi log e automazioni ripetitive in risk operations.</p>""",
            "en": """<p>Hands-on experience with Ollama, WSL, Llama, Qwen and Mistral for private workflows and AI automation.</p>
<h2>Recommended setup</h2><ul><li>WSL2 with Ubuntu on Windows</li><li>Ollama + quantised models</li><li>GPU acceleration when available</li></ul>
<h2>Use cases</h2><p>Prompt engineering, reporting, log analysis and repetitive automation in risk operations.</p>""",
        },
    },
    {
        "slug": "massa-muscolare",
        "cat": {"it": "Fitness & Nutrizione", "en": "Fitness & Nutrition"},
        "title": {
            "it": "Come aumentare la massa muscolare",
            "en": "How to increase muscle mass",
        },
        "desc": {
            "it": "Ipertrofia progressiva, nutrizione e recupero per crescita sostenibile.",
            "en": "Progressive overload, nutrition and recovery for sustainable growth.",
        },
        "date": "2026-05-20",
        "read": {"it": "5 min", "en": "5 min"},
        "body": {
            "it": """<p>Con oltre 15 anni di bodybuilding, la crescita muscolare richiede tre pilastri: allenamento progressivo, surplus calorico controllato e recupero adeguato.</p>
<h2>Allenamento</h2><p>Focus su compound movements, progressione del carico e volume settimanale sostenibile.</p>
<h2>Nutrizione</h2><p>Proteine 1.6–2.2 g/kg, carboidrati peri-workout e grassi essenziali.</p>""",
            "en": """<p>With over 15 years of bodybuilding, muscle growth requires three pillars: progressive training, controlled caloric surplus and adequate recovery.</p>
<h2>Training</h2><p>Focus on compound movements, load progression and sustainable weekly volume.</p>
<h2>Nutrition</h2><p>Protein 1.6–2.2 g/kg, peri-workout carbohydrates and essential fats.</p>""",
        },
    },
    {
        "slug": "alimentazione-forma",
        "cat": {"it": "Fitness & Nutrizione", "en": "Fitness & Nutrition"},
        "title": {
            "it": "Alimentazione per mantenersi in forma",
            "en": "Nutrition to stay in shape",
        },
        "desc": {
            "it": "Equilibrio, costanza e scelte alimentari sostenibili nel tempo.",
            "en": "Balance, consistency and sustainable food choices over time.",
        },
        "date": "2026-05-15",
        "read": {"it": "5 min", "en": "5 min"},
        "body": {
            "it": """<p>Mantenere la forma non significa diete estreme. Significa equilibrio tra deficit/surplus, qualità degli alimenti e aderenza nel lungo periodo.</p>
<ul><li>Priorità a proteine, fibre e micronutrienti</li><li>Idratazione costante</li><li>Pianificazione dei pasti</li><li>Flessibilità controllata</li></ul>""",
            "en": """<p>Staying in shape does not mean extreme diets. It means balancing deficit/surplus, food quality and long-term adherence.</p>
<ul><li>Prioritise protein, fibre and micronutrients</li><li>Consistent hydration</li><li>Meal planning</li><li>Controlled flexibility</li></ul>""",
        },
    },
    {
        "slug": "zucchero-raffinato",
        "cat": {"it": "Fitness & Nutrizione", "en": "Fitness & Nutrition"},
        "title": {
            "it": "Perché evitare lo zucchero raffinato",
            "en": "Why avoid refined sugar",
        },
        "desc": {
            "it": "Impatto metabolico, energia e composizione corporea.",
            "en": "Metabolic impact, energy and body composition.",
        },
        "date": "2026-05-10",
        "read": {"it": "4 min", "en": "4 min"},
        "body": {
            "it": """<p>Lo zucchero raffinato causa picchi glicemici, craving e difficoltà nel controllo della composizione corporea.</p>
<p>Alternative: frutta intera, carboidrati complessi e dolcificanti moderati quando necessario.</p>""",
            "en": """<p>Refined sugar causes glycaemic spikes, cravings and difficulty managing body composition.</p>
<p>Alternatives: whole fruit, complex carbohydrates and moderate sweeteners when needed.</p>""",
        },
    },
    {
        "slug": "integrazione-proteica",
        "cat": {"it": "Fitness & Nutrizione", "en": "Fitness & Nutrition"},
        "title": {
            "it": "Integrazione proteica per la massa muscolare",
            "en": "Protein supplementation for muscle mass",
        },
        "desc": {
            "it": "Quando ha senso, dosaggi e qualità del prodotto.",
            "en": "When it makes sense, dosages and product quality.",
        },
        "date": "2026-05-05",
        "read": {"it": "5 min", "en": "5 min"},
        "body": {
            "it": """<p>Le proteine in polvere sono un complemento, non un sostituto di un'alimentazione solida.</p>
<h2>Quando usarle</h2><p>Quando non raggiungi il target proteico con il cibo o per comodità post-workout.</p>
<h2>Qualità</h2><p>Whey isolate/concentrate, pochi ingredienti, attenzione a zuccheri aggiunti.</p>""",
            "en": """<p>Protein powder is a supplement, not a replacement for solid nutrition.</p>
<h2>When to use</h2><p>When you cannot hit your protein target from food or for post-workout convenience.</p>
<h2>Quality</h2><p>Whey isolate/concentrate, few ingredients, watch for added sugars.</p>""",
        },
    },
    {
        "slug": "hospitality-estero",
        "cat": {"it": "Hospitality & Estero", "en": "Hospitality & Abroad"},
        "title": {
            "it": "Dal bancone al mondo: hospitality in UK e Sudafrica",
            "en": "From the bar to the world: hospitality in the UK and South Africa",
        },
        "desc": {
            "it": "Oltre 10 anni tra turismo, RSC e resort internazionali.",
            "en": "Over 10 years in tourism, RSC and international resorts.",
        },
        "date": "2026-04-28",
        "read": {"it": "6 min", "en": "6 min"},
        "body": {
            "it": """<p>Prima del fintech, la mia formazione è nata dietro un bancone — hotel, teatri e bar ad alto volume in Inghilterra e Sudafrica.</p>
<p>Royal Shakespeare Company, eventi corporate, qualifica AIBES, corsi mixology e sommelier, HACCP Alberghiero Molinari Sciacca.</p>""",
            "en": """<p>Before fintech, my training started behind a bar — hotels, theatres and high-volume venues in England and South Africa.</p>
<p>Royal Shakespeare Company, corporate events, AIBES qualification, mixology and sommelier courses, HACCP hospitality certification.</p>""",
        },
    },
    {
        "slug": "tech-build-pc",
        "cat": {"it": "Tech & Sperimentazione", "en": "Tech & Experimentation"},
        "title": {
            "it": "Build PC avanzati e server AI locale",
            "en": "Advanced PC builds and local AI servers",
        },
        "desc": {
            "it": "Hardware, multi-OS, GPU acceleration e automazioni.",
            "en": "Hardware, multi-OS, GPU acceleration and automation.",
        },
        "date": "2026-04-20",
        "read": {"it": "6 min", "en": "6 min"},
        "body": {
            "it": """<p>Build PC personalizzati, installazione Windows/Linux/macOS, PowerShell, Bash e server AI locale con GPU.</p>
<ul><li>Selezione componenti per workload AI</li><li>WSL2 + CUDA/ROCm</li><li>Scripting e automazioni</li></ul>""",
            "en": """<p>Custom PC builds, Windows/Linux/macOS setup, PowerShell, Bash and local AI servers with GPU.</p>
<ul><li>Component selection for AI workloads</li><li>WSL2 + CUDA/ROCm</li><li>Scripting and automation</li></ul>""",
        },
    },
]


def head(lang, page_file, title, description, alt_lang_file=None):
    canonical = f"{BASE}/{lang}/{page_file}"
    alt_lang = "en" if lang == "it" else "it"
    alt_href = f"{BASE}/{alt_lang}/{alt_lang_file or page_file}"
    hreflang_self = "it-IT" if lang == "it" else "en-GB"
    hreflang_alt = "en-GB" if lang == "it" else "it-IT"
    html_lang = "it" if lang == "it" else "en-GB"
    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{description}">
  <meta name="author" content="Stefano Davide Ciancimino">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="{BASE}/img/logo-sc-hd.png">
  <title>{title}</title>
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="{hreflang_self}" href="{canonical}">
  <link rel="alternate" hreflang="{hreflang_alt}" href="{alt_href}">
  <link rel="alternate" hreflang="x-default" href="{BASE}/it/{page_file}">
  <link rel="icon" href="{ASSET}img/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="{ASSET}img/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Lato:wght@400;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{ASSET}css/style.css?v=20260622-ml">
</head>"""


def header(lang, current):
    ui = UI[lang]
    other = "en" if lang == "it" else "it"
    nav_links = "".join(
        f'<a href="{href}" class="nav__link{" nav__link--active" if href == current else ""}">{label}</a>'
        for href, label in NAV[lang]
    )
    it_active = " lang-switch__btn--active" if lang == "it" else ""
    en_active = " lang-switch__btn--active" if lang == "en" else ""
    alt_path = f"../{other}/{current}"
    return f"""  <header class="header">
    <div class="container header__inner">
      <a href="index.html" class="logo">
        <div class="logo__icon logo__icon--brand">
          <img src="{ASSET}img/logo-sc-hd.png" alt="Stefano Ciancimino logo" class="logo__img" width="40" height="40" loading="eager" decoding="async">
        </div>
        <div>
          <div class="logo__text">Stefano Ciancimino</div>
          <div class="logo__sub">{ui['logo_sub']}</div>
        </div>
      </a>
      <div class="header__actions">
        <nav class="lang-switch" aria-label="Language">
          <a href="../it/{current}" class="lang-switch__btn{it_active}" aria-label="{ui['lang_it_aria']}" title="Italiano">🇮🇹</a>
          <a href="../en/{current}" class="lang-switch__btn{en_active}" aria-label="{ui['lang_en_aria']}" title="English">🇬🇧</a>
        </nav>
        <button class="theme-toggle" aria-label="{ui['theme_aria']}">
          <svg class="icon-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
          <svg class="icon-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
        </button>
        <button class="nav-toggle" aria-label="{ui['menu_aria']}"><span></span><span></span><span></span></button>
      </div>
      <nav class="nav">
        {nav_links}
        <a href="contact.html" class="nav__link nav__cta btn btn--primary">{ui['cta']}</a>
      </nav>
    </div>
  </header>"""


def footer(lang):
    ui = UI[lang]
    year = date.today().year
    return f"""  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <a href="index.html" class="logo">
            <div class="logo__icon logo__icon--brand">
              <img src="{ASSET}img/logo-transparent.png" alt="" class="logo__img" width="36" height="36" loading="lazy">
            </div>
            <div><div class="logo__text">Stefano Ciancimino</div><div class="logo__sub">{ui['footer_tagline']}</div></div>
          </a>
        </div>
        <div>
          <h4>Email</h4>
          <p><a href="mailto:krown82@outlook.com">krown82@outlook.com</a></p>
        </div>
        <div>
          <h4>LinkedIn</h4>
          <p><a href="https://www.linkedin.com/in/55555555-b5947439" target="_blank" rel="noopener">linkedin.com/in/55555555-b5947439</a></p>
        </div>
      </div>
      <div class="footer__bottom"><span>© {year} Stefano Davide Ciancimino — {ui['footer_rights']}</span></div>
    </div>
  </footer>
  <script src="{ASSET}js/main.js?v=20260622-ml"></script>
  <script src="{ASSET}js/chatbot.js?v=20260622-ml"></script>
</body>
</html>"""


def page_hero(label, h1, subtitle):
    return f"""  <section class="page-hero">
    <div class="container reveal">
      <span class="section-label">{label}</span>
      <h1>{h1}</h1>
      <p>{subtitle}</p>
    </div>
  </section>"""


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_index(lang):
    ui = UI[lang]
    if lang == "it":
        badge, h1 = "Disponibile per consulenze", "Fraud Analyst · Blockchain Researcher · AI Specialist"
        sub = "Professionista con oltre 8 anni di esperienza in analisi antifrode, risk management, blockchain e automazione AI. Orientato a sicurezza, efficienza operativa e innovazione tecnologica."
        stats = [("8+", "Anni PayPal"), ("2017+", "Blockchain"), ("15+", "Anni fitness")]
        sections_label = "Aree di competenza"
        sections_h2 = "CV · Portfolio · Blog tematico"
        passions = [
            ("about.html", "CV / Chi Sono", "8+ anni PayPal, competenze internazionali, AI e blockchain."),
            ("ai-blockchain.html", "AI & Blockchain", "Ricerca dal 2017, DeFi/CeFi, Ollama e prompt engineering."),
            ("tech.html", "Tech & Hobby", "Build PC, multi-OS, PowerShell, server AI locale."),
            ("hospitality.html", "Hospitality", "10+ anni turismo, UK, Sudafrica, mixology."),
            ("fitness.html", "Fitness & Health", "15+ anni bodybuilding, nutrizione e articoli dedicati."),
            ("blog.html", "Blog", "6 categorie: antifrode, crypto, AI, fitness, hospitality, tech."),
        ]
    else:
        badge, h1 = "Available for consulting", "Fraud Analyst · Blockchain Researcher · AI Specialist"
        sub = "Professional with 8+ years in fraud analysis, risk management, blockchain and AI automation. Focused on security, operational efficiency and technological innovation."
        stats = [("8+", "Years at PayPal"), ("2017+", "Blockchain"), ("15+", "Years fitness")]
        sections_label = "Areas of expertise"
        sections_h2 = "CV · Portfolio · Thematic blog"
        passions = [
            ("about.html", "CV / About Me", "8+ years at PayPal, international skills, AI and blockchain."),
            ("ai-blockchain.html", "AI & Blockchain", "Research since 2017, DeFi/CeFi, Ollama and prompt engineering."),
            ("tech.html", "Tech & Hobbies", "PC builds, multi-OS, PowerShell, local AI server."),
            ("hospitality.html", "Hospitality", "10+ years tourism, UK, South Africa, mixology."),
            ("fitness.html", "Fitness & Health", "15+ years bodybuilding, nutrition and dedicated articles."),
            ("blog.html", "Blog", "6 categories: fraud, crypto, AI, fitness, hospitality, tech."),
        ]
    cards = "".join(
        f'<article class="passion-card reveal"><div class="passion-card__icon">→</div><h3>{t}</h3><p>{d}</p><a href="{u}" class="passion-card__link">{ui["read_more"]} →</a></article>'
        for u, t, d in passions
    )
    stat_html = "".join(f'<div class="stat-box"><strong>{v}</strong><span>{l}</span></div>' for v, l in stats)
    title = f"Stefano Ciancimino — Fraud Analyst · Blockchain · AI"
    desc = sub[:155]
    body = f"""{head(lang, "index.html", title, desc)}
<body data-lang="{lang}">
{header(lang, "index.html")}
  <section class="hero">
    <div class="container hero__grid">
      <div class="hero__content reveal">
        <div class="hero__badge"><span class="hero__badge-dot"></span>{badge}</div>
        <h1>{h1}</h1>
        <p class="hero__subtitle">{sub}</p>
        <div class="hero__actions">
          <a href="cv.html" class="btn btn--primary" id="download-cv" target="_blank">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
            {ui['download_cv']}
          </a>
          <a href="contact.html" class="btn btn--outline">{ui['cta']}</a>
          <a href="https://www.linkedin.com/in/55555555-b5947439" target="_blank" rel="noopener" class="btn btn--linkedin">LinkedIn</a>
        </div>
        <div class="stat-row">{stat_html}</div>
      </div>
      <div class="hero__image reveal reveal-delay-2">
        <div class="hero__image-frame">
          <img src="{ASSET}img/profile.jpg" alt="Stefano Davide Ciancimino" class="profile-photo" width="480" height="480">
        </div>
      </div>
    </div>
  </section>
  <section class="section section--pearl">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">{sections_label}</span>
        <h2>{sections_h2}</h2>
      </div>
      <div class="passion-grid">{cards}</div>
    </div>
  </section>
{footer(lang)}"""
    write(ROOT / lang / "index.html", body)


def build_about(lang):
    ui = UI[lang]
    if lang == "it":
        title, desc = "Chi Sono — Stefano Ciancimino", "Bio professionale, competenze e percorso in antifrode, blockchain e AI."
        h1, sub = "Chi Sono", "Fraud & Risk Analyst con esperienza internazionale e focus su innovazione."
        bio = """<p>Professionista con oltre <strong>8 anni presso PayPal</strong> in antifrode, risk operations e investigazioni. Esperienza internazionale, competenze in AI, blockchain, DeFi/CeFi, Linux, macOS, PowerShell e troubleshooting hardware/software.</p>
<p>Lingue: <strong>Italiano C2</strong> (madrelingua), <strong>Inglese C1</strong> fluente.</p>
<p>Customer service avanzato, capacità analitiche e collaborazione in team cross-functional ad alto impatto.</p>"""
        skills = ["Antifrode", "Risk Management", "Blockchain", "DeFi/CeFi", "AI / Ollama", "Linux", "macOS", "PowerShell", "Prompt Engineering"]
    else:
        title, desc = "About Me — Stefano Ciancimino", "Professional bio, skills and career in fraud, blockchain and AI."
        h1, sub = "About Me", "Fraud & Risk Analyst with international experience and innovation focus."
        bio = """<p>Professional with <strong>8+ years at PayPal</strong> in fraud prevention, risk operations and investigations. International experience, skills in AI, blockchain, DeFi/CeFi, Linux, macOS, PowerShell and hardware/software troubleshooting.</p>
<p>Languages: <strong>Italian C2</strong> (native), <strong>English C1</strong> fluent.</p>
<p>Advanced customer service, analytical skills and collaboration in high-impact cross-functional teams.</p>"""
        skills = ["Fraud Prevention", "Risk Management", "Blockchain", "DeFi/CeFi", "AI / Ollama", "Linux", "macOS", "PowerShell", "Prompt Engineering"]
    tags = "".join(f'<span class="skill-tag">{s}</span>' for s in skills)
    body = f"""{head(lang, "about.html", title, desc)}
<body data-lang="{lang}">
{header(lang, "about.html")}
{page_hero("Profile", h1, sub)}
  <section class="section">
    <div class="container about-grid">
      <div class="about__photo reveal"><img src="{ASSET}img/profile.jpg" alt="Stefano Davide Ciancimino" class="profile-photo"></div>
      <div class="reveal reveal-delay-1 content-prose">
        <h2>Stefano Davide Ciancimino</h2>
        <p style="color:var(--color-turquoise);font-weight:600">Fraud & Risk Analyst · Blockchain Researcher · AI Specialist</p>
        {bio}
        <div class="skill-tags">{tags}</div>
        <p style="margin-top:2rem"><a href="cv.html" class="btn btn--primary" target="_blank">{ui['download_cv']}</a></p>
      </div>
    </div>
  </section>
{footer(lang)}"""
    write(ROOT / lang / "about.html", body)


def build_section(lang, slug, label, h1, sub, content_html):
    title = f"{h1} — Stefano Ciancimino"
    body = f"""{head(lang, f"{slug}.html", title, sub)}
<body data-lang="{lang}">
{header(lang, f"{slug}.html")}
{page_hero(label, h1, sub)}
  <section class="section">
    <div class="container content-prose reveal">{content_html}</div>
  </section>
{footer(lang)}"""
    write(ROOT / lang / f"{slug}.html", body)


def build_ai_blockchain(lang):
    if lang == "it":
        c = """<p>Ricerca blockchain dal <strong>2017</strong>. Analisi ecosistemi DeFi, CeFi e NFT con approccio risk-oriented.</p>
<div class="stat-row"><div class="stat-box"><strong>2017+</strong><span>Ricerca crypto</span></div><div class="stat-box"><strong>PayPal</strong><span>Sessioni Bitcoin</span></div><div class="stat-box"><strong>AI</strong><span>Ollama · WSL</span></div></div>
<h2>Blockchain & Crypto</h2><ul><li>Analisi protocolli e ecosistemi DeFi/CeFi/NFT</li><li>Sessioni interne PayPal su Bitcoin</li><li>Crypto Italia Facile — portale educativo</li></ul>
<h2>Intelligenza Artificiale</h2><ul><li>Modelli locali: Ollama, Llama, Qwen, Mistral</li><li>Prompt engineering per operations</li><li>Automazioni AI e server locale su WSL</li></ul>
<p><a href="https://satoshiallien.github.io/cryptoitaliafacile/index.html" target="_blank" rel="noopener" class="btn btn--ghost">Crypto Italia Facile →</a></p>"""
        build_section(lang, "ai-blockchain", "Innovazione", "AI & Blockchain", "Ricerca, automazione e analisi ecosistemi decentralizzati.", c)
    else:
        c = """<p>Blockchain research since <strong>2017</strong>. Analysis of DeFi, CeFi and NFT ecosystems with a risk-oriented approach.</p>
<div class="stat-row"><div class="stat-box"><strong>2017+</strong><span>Crypto research</span></div><div class="stat-box"><strong>PayPal</strong><span>Bitcoin sessions</span></div><div class="stat-box"><strong>AI</strong><span>Ollama · WSL</span></div></div>
<h2>Blockchain & Crypto</h2><ul><li>DeFi/CeFi/NFT protocol and ecosystem analysis</li><li>Internal PayPal Bitcoin training sessions</li><li>Crypto Italia Facile — educational portal</li></ul>
<h2>Artificial Intelligence</h2><ul><li>Local models: Ollama, Llama, Qwen, Mistral</li><li>Prompt engineering for operations</li><li>AI automation and local WSL servers</li></ul>
<p><a href="https://satoshiallien.github.io/cryptoitaliafacile/index.html" target="_blank" rel="noopener" class="btn btn--ghost">Crypto Italia Facile →</a></p>"""
        build_section(lang, "ai-blockchain", "Innovation", "AI & Blockchain", "Research, automation and decentralised ecosystem analysis.", c)


def build_tech(lang):
    if lang == "it":
        c = """<p>Passione per hardware, sistemi operativi e automazione. Build PC avanzati, installazione Windows/Linux/macOS, PowerShell, Bash e terminale.</p>
<div class="feature-list">
<div class="feature-item"><div class="feature-item__icon">🖥</div><div><h3>Build PC avanzati</h3><p>Selezione componenti, airflow, overclocking moderato e workstation per AI.</p></div></div>
<div class="feature-item"><div class="feature-item__icon">⚡</div><div><h3>GPU acceleration</h3><p>CUDA, inferenza locale, modelli quantizzati su server domestico.</p></div></div>
<div class="feature-item"><div class="feature-item__icon">🔧</div><div><h3>Scripting</h3><p>PowerShell, Bash, automazioni e troubleshooting rete/hardware/software.</p></div></div>
</div>"""
        build_section(lang, "tech", "Tech Lab", "Tech & Hobby", "Build, sistemi operativi e sperimentazione tecnologica.", c)
    else:
        c = """<p>Passion for hardware, operating systems and automation. Advanced PC builds, Windows/Linux/macOS setup, PowerShell, Bash and terminal.</p>
<div class="feature-list">
<div class="feature-item"><div class="feature-item__icon">🖥</div><div><h3>Advanced PC builds</h3><p>Component selection, airflow, moderate overclocking and AI workstations.</p></div></div>
<div class="feature-item"><div class="feature-item__icon">⚡</div><div><h3>GPU acceleration</h3><p>CUDA, local inference, quantised models on home server.</p></div></div>
<div class="feature-item"><div class="feature-item__icon">🔧</div><div><h3>Scripting</h3><p>PowerShell, Bash, automation and network/hardware/software troubleshooting.</p></div></div>
</div>"""
        build_section(lang, "tech", "Tech Lab", "Tech & Hobbies", "Builds, operating systems and tech experimentation.", c)


def build_hospitality(lang):
    if lang == "it":
        c = """<p>Oltre <strong>10 anni</strong> nel turismo e ristorazione. Esperienze in Inghilterra (Royal Shakespeare Company, eventi corporate), Sudafrica e Italia.</p>
<div class="stat-row"><div class="stat-box"><strong>10+</strong><span>anni settore</span></div><div class="stat-box"><strong>UK</strong><span>RSC · Corporate</span></div><div class="stat-box"><strong>AIBES</strong><span>Bartender pro</span></div></div>
<ul><li>Bartender professionale e barista</li><li>Qualifica AIBES, corsi mixology e sommelier</li><li>HACCP Alberghiero Molinari Sciacca</li><li>Gestione picchi operativi e clientela VIP</li></ul>"""
        build_section(lang, "hospitality", "Hospitality", "Hospitality & Estero", "Dal bancone al mondo: servizio, disciplina e standard internazionali.", c)
    else:
        c = """<p>Over <strong>10 years</strong> in tourism and hospitality. Experience in England (Royal Shakespeare Company, corporate events), South Africa and Italy.</p>
<div class="stat-row"><div class="stat-box"><strong>10+</strong><span>years in sector</span></div><div class="stat-box"><strong>UK</strong><span>RSC · Corporate</span></div><div class="stat-box"><strong>AIBES</strong><span>Pro bartender</span></div></div>
<ul><li>Professional bartender and barista</li><li>AIBES qualification, mixology and sommelier courses</li><li>HACCP hospitality certification Molinari Sciacca</li><li>Peak service management and VIP clientele</li></ul>"""
        build_section(lang, "hospitality", "Hospitality", "Hospitality & Abroad", "From the bar to the world: service, discipline and international standards.", c)


def build_fitness(lang):
    ui = UI[lang]
    if lang == "it":
        articles = [
            ("blog/massa-muscolare.html", "Come aumentare la massa muscolare"),
            ("blog/alimentazione-forma.html", "Alimentazione per mantenersi in forma"),
            ("blog/zucchero-raffinato.html", "Perché evitare lo zucchero raffinato"),
            ("blog/integrazione-proteica.html", "Integrazione proteica per la massa muscolare"),
        ]
        c = """<p>Oltre <strong>15 anni</strong> di bodybuilding, corsa su strada, bici da corsa e nutrizione sportiva. Approccio naturale, evidence-based e costanza.</p>
<div class="stat-row"><div class="stat-box"><strong>15+</strong><span>anni fitness</span></div><div class="stat-box"><strong>5</strong><span>sport praticati</span></div><div class="stat-box"><strong>100%</strong><span>approccio naturale</span></div></div>
<h2>Articoli</h2><ul>""" + "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in articles) + "</ul>"
        build_section(lang, "fitness", "Fitness", "Fitness & Health", "Allenamento, nutrizione e benessere a lungo termine.", c)
    else:
        articles = [
            ("blog/massa-muscolare.html", "How to increase muscle mass"),
            ("blog/alimentazione-forma.html", "Nutrition to stay in shape"),
            ("blog/zucchero-raffinato.html", "Why avoid refined sugar"),
            ("blog/integrazione-proteica.html", "Protein supplementation for muscle mass"),
        ]
        c = """<p>Over <strong>15 years</strong> of bodybuilding, road running, road cycling and sports nutrition. Natural, evidence-based and consistent approach.</p>
<div class="stat-row"><div class="stat-box"><strong>15+</strong><span>years fitness</span></div><div class="stat-box"><strong>5</strong><span>sports practised</span></div><div class="stat-box"><strong>100%</strong><span>natural approach</span></div></div>
<h2>Articles</h2><ul>""" + "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in articles) + "</ul>"
        build_section(lang, "fitness", "Fitness", "Fitness & Health", "Training, nutrition and long-term wellbeing.", c)


def build_portfolio(lang):
    ui = UI[lang]
    if lang == "it":
        h1, sub = "Portfolio", "Progetti, analisi e contenuti educativi."
        cards = [
            ("blog/antifrode-pagamenti.html", "Framework Antifrode", "Guide e analisi su pattern fraudolenti.", ["Antifrode", "Risk"]),
            ("https://satoshiallien.github.io/cryptoitaliafacile/index.html", "Crypto Italia Facile", "Portale educativo Bitcoin e blockchain.", ["Bitcoin", "Education"]),
            ("blog/ai-ollama.html", "Demo AI Locale", "Agenti Ollama per automazione operations.", ["AI", "Ollama"]),
        ]
    else:
        h1, sub = "Portfolio", "Projects, analysis and educational content."
        cards = [
            ("blog/antifrode-pagamenti.html", "Fraud Framework", "Guides and analysis on fraud patterns.", ["Fraud", "Risk"]),
            ("https://satoshiallien.github.io/cryptoitaliafacile/index.html", "Crypto Italia Facile", "Bitcoin and blockchain educational portal.", ["Bitcoin", "Education"]),
            ("blog/ai-ollama.html", "Local AI Demo", "Ollama agents for operations automation.", ["AI", "Ollama"]),
        ]
    items = ""
    for link, title, desc, tags in cards:
        ext = ' target="_blank" rel="noopener"' if link.startswith("http") else ""
        tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
        items += f'<div class="portfolio-card reveal"><div class="portfolio-card__body"><h3>{title}</h3><p>{desc}</p><div class="portfolio-card__tags">{tag_html}</div><a href="{link}" class="blog-card__link"{ext}>{ui["read_more"]} →</a></div></div>'
    body = f"""{head(lang, "portfolio.html", f"Portfolio — Stefano Ciancimino", sub)}
<body data-lang="{lang}">
{header(lang, "portfolio.html")}
{page_hero("Projects", h1, sub)}
  <section class="section"><div class="container"><div class="portfolio-grid">{items}</div></div></section>
{footer(lang)}"""
    write(ROOT / lang / "portfolio.html", body)


def build_blog(lang):
    ui = UI[lang]
    if lang == "it":
        h1, sub = "Blog Professionale", "Articoli su antifrode, blockchain, AI, fitness, hospitality e tech."
    else:
        h1, sub = "Professional Blog", "Articles on fraud, blockchain, AI, fitness, hospitality and tech."
    cards = ""
    for i, art in enumerate(ARTICLES):
        delay = f' reveal-delay-{i % 3}' if i % 3 else ""
        cards += f"""<article class="blog-card reveal{delay}">
          <div class="blog-card__image-wrap"><div class="blog-card__image"></div><span class="blog-card__category">{art['cat'][lang]}</span></div>
          <div class="blog-card__body">
            <div class="blog-card__meta"><span>{art['date']}</span><span>{art['read'][lang]}</span></div>
            <h3>{art['title'][lang]}</h3>
            <p>{art['desc'][lang]}</p>
            <a href="blog/{art['slug']}.html" class="blog-card__link">{ui['read_article']} →</a>
          </div>
        </article>"""
    body = f"""{head(lang, "blog.html", f"Blog — Stefano Ciancimino", sub)}
<body data-lang="{lang}">
{header(lang, "blog.html")}
{page_hero("Insights", h1, sub)}
  <section class="section"><div class="container"><div class="blog-grid">{cards}</div></div></section>
{footer(lang)}"""
    write(ROOT / lang / "blog.html", body)


def build_contact(lang):
    ui = UI[lang]
    if lang == "it":
        h1, sub = "Contatti", "Rispondo entro 24 ore lavorative."
        form = """<label for="nome">Nome *</label><input type="text" id="nome" name="nome" required>
<label for="email">Email *</label><input type="email" id="email" name="email" required>
<label for="telefono">Telefono</label><input type="tel" id="telefono" name="telefono">
<label for="servizio">Argomento *</label><select id="servizio" name="servizio" required><option value="">Seleziona</option><option>Consulenza antifrode</option><option>Blockchain / Crypto</option><option>AI / Automazione</option><option>Altro</option></select>
<label for="messaggio">Messaggio *</label><textarea id="messaggio" name="messaggio" rows="5" required></textarea>
<button type="submit" class="btn btn--primary">Invia messaggio</button>"""
        info_h = "Informazioni di contatto"
    else:
        h1, sub = "Contact", "I reply within 24 business hours."
        form = """<label for="nome">Name *</label><input type="text" id="nome" name="nome" required>
<label for="email">Email *</label><input type="email" id="email" name="email" required>
<label for="telefono">Phone</label><input type="tel" id="telefono" name="telefono">
<label for="servizio">Subject *</label><select id="servizio" name="servizio" required><option value="">Select</option><option>Fraud consulting</option><option>Blockchain / Crypto</option><option>AI / Automation</option><option>Other</option></select>
<label for="messaggio">Message *</label><textarea id="messaggio" name="messaggio" rows="5" required></textarea>
<button type="submit" class="btn btn--primary">Send message</button>"""
        info_h = "Contact information"
    body = f"""{head(lang, "contact.html", f"Contact — Stefano Ciancimino", sub)}
<body data-lang="{lang}" data-form-success="{ui['form_success']}">
{header(lang, "contact.html")}
{page_hero("Contact", h1, sub)}
  <section class="section">
    <div class="container contact-grid">
      <div class="reveal">
        <h2 style="margin-bottom:2rem">{info_h}</h2>
        <div class="contact-info__item"><div class="contact-info__icon">✉</div><div><strong>Email</strong><br><a href="mailto:krown82@outlook.com">krown82@outlook.com</a></div></div>
        <div class="contact-info__item"><div class="contact-info__icon">📞</div><div><strong>Tel</strong><br><a href="tel:+393773503049">+39 377 350 3049</a></div></div>
        <div class="contact-info__item"><div class="contact-info__icon">in</div><div><strong>LinkedIn</strong><br><a href="https://www.linkedin.com/in/55555555-b5947439" target="_blank" rel="noopener">linkedin.com/in/55555555-b5947439</a></div></div>
      </div>
      <div class="reveal reveal-delay-1">
        <div id="form-success" class="form-success"></div>
        <form id="contact-form" class="form-grid">{form}</form>
      </div>
    </div>
  </section>
{footer(lang)}"""
    write(ROOT / lang / "contact.html", body)


def build_cv(lang):
    if lang == "it":
        role = "Fraud & Risk Analyst · Blockchain Researcher · AI Specialist"
        prof = "Professionista con oltre 8 anni in analisi antifrode, risk management, blockchain e AI. Italiano madrelingua, Inglese C1."
        exp = """<div class="cv-item"><h3>Senior Seller Risk Operations</h3><div class="meta">PayPal · 2018 – 2022</div><ul><li>Investigazioni account ad alto rischio</li><li>Mitigazione frodi e coaching team</li></ul></div>
<div class="cv-item"><h3>Buyer Fraud Prevention Analyst</h3><div class="meta">PayPal · 2013 – 2018</div><ul><li>Monitoraggio transazioni e schemi fraudolenti</li><li>Prevenzione frodi da 100.000 USD</li></ul></div>
<div class="cv-item"><h3>Blockchain Researcher</h3><div class="meta">Indipendente · 2017 – oggi</div><ul><li>DeFi/CeFi, formazione interna PayPal</li></ul></div>"""
        skills_h = "Competenze"
        skills = "<p><strong>AI:</strong> Ollama, prompt engineering, automazioni<br><strong>Blockchain:</strong> DeFi, CeFi, NFT<br><strong>Tech:</strong> Linux, macOS, PowerShell, WSL</p>"
    else:
        role = "Fraud & Risk Analyst · Blockchain Researcher · AI Specialist"
        prof = "Professional with 8+ years in fraud analysis, risk management, blockchain and AI. Native Italian, English C1."
        exp = """<div class="cv-item"><h3>Senior Seller Risk Operations</h3><div class="meta">PayPal · 2018 – 2022</div><ul><li>High-risk account investigations</li><li>Fraud mitigation and team coaching</li></ul></div>
<div class="cv-item"><h3>Buyer Fraud Prevention Analyst</h3><div class="meta">PayPal · 2013 – 2018</div><ul><li>Transaction monitoring and fraud schemes</li><li>Prevented fraud worth USD 100,000</li></ul></div>
<div class="cv-item"><h3>Blockchain Researcher</h3><div class="meta">Independent · 2017 – present</div><ul><li>DeFi/CeFi, internal PayPal training</li></ul></div>"""
        skills_h = "Skills"
        skills = "<p><strong>AI:</strong> Ollama, prompt engineering, automation<br><strong>Blockchain:</strong> DeFi, CeFi, NFT<br><strong>Tech:</strong> Linux, macOS, PowerShell, WSL</p>"
    print_btn = UI[lang]["print_cv"]
    body = f"""{head(lang, "cv.html", "CV — Stefano Ciancimino", "Curriculum professionale di Stefano Davide Ciancimino.")}
<body data-lang="{lang}">
<button class="print-btn" onclick="window.print()" style="position:fixed;top:1rem;right:1rem;padding:.75rem 1.5rem;background:#14b8a6;color:#fff;border:none;border-radius:9999px;cursor:pointer">{print_btn}</button>
<div class="cv-page" style="max-width:800px;margin:2rem auto;background:#fff;padding:3rem;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,.08)">
<header style="border-bottom:3px solid #14b8a6;padding-bottom:1.5rem;margin-bottom:2rem">
<h1 style="font-family:Poppins,sans-serif">Stefano Davide Ciancimino</h1>
<p style="color:#14b8a6;font-weight:600">{role}</p>
<p>krown82@outlook.com · +39 377 350 3049 · <a href="https://www.linkedin.com/in/55555555-b5947439">LinkedIn</a></p>
</header>
<section><h2 style="color:#14b8a6;text-transform:uppercase;font-size:1rem">{"Profilo" if lang=="it" else "Profile"}</h2><p>{prof}</p></section>
<section style="margin-top:2rem"><h2 style="color:#14b8a6;text-transform:uppercase;font-size:1rem">{"Esperienza" if lang=="it" else "Experience"}</h2>{exp}</section>
<section style="margin-top:2rem"><h2 style="color:#14b8a6;text-transform:uppercase;font-size:1rem">{skills_h}</h2>{skills}</section>
</div>
</body></html>"""
    write(ROOT / lang / "cv.html", body)


def build_article(lang, art):
    slug = f"blog/{art['slug']}.html"
    title = f"{art['title'][lang]} — Stefano Ciancimino"
    breadcrumb_blog = "Blog"
    body = f"""{head(lang, slug, title, art['desc'][lang])}
<body data-lang="{lang}">
{header(lang, slug)}
  <header class="article-header">
    <div class="container">
      <nav class="breadcrumb"><a href="index.html">Home</a><span>/</span><a href="blog.html">{breadcrumb_blog}</a><span>/</span><span>{art['cat'][lang]}</span></nav>
      <span class="section-label">{art['cat'][lang]}</span>
      <h1>{art['title'][lang]}</h1>
      <div class="article-meta"><span>Stefano Davide Ciancimino</span><span>{art['date']}</span><span>{art['read'][lang]}</span></div>
    </div>
  </header>
  <article class="article-content"><div class="container content-prose">{art['body'][lang]}</div></article>
{footer(lang)}"""
    write(ROOT / lang / slug, body)


def build_root_redirect():
    content = """<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0;url=it/">
  <title>Stefano Ciancimino — Redirect</title>
  <link rel="canonical" href="https://satoshiallien.github.io/Stefano/it/">
  <script>
    (function () {
      var base = location.pathname.indexOf('/Stefano') >= 0 ? '/Stefano' : '';
      var lang = (navigator.language || '').toLowerCase().startsWith('it') ? 'it' : 'en';
      location.replace(base + '/' + lang + '/');
    })();
  </script>
</head>
<body><p><a href="it/">Italiano</a> · <a href="en/">English</a></p></body>
</html>"""
    write(ROOT / "index.html", content)


def build_sitemap():
    pages = [
        "index.html", "about.html", "ai-blockchain.html", "tech.html",
        "hospitality.html", "fitness.html", "portfolio.html", "blog.html",
        "contact.html", "cv.html",
    ]
    for art in ARTICLES:
        pages.append(f"blog/{art['slug']}.html")
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for p in pages:
        it_url = f"{BASE}/it/{p}"
        en_url = f"{BASE}/en/{p}"
        lines.append("  <url>")
        lines.append(f"    <loc>{it_url}</loc>")
        lines.append(f"    <lastmod>{TODAY}</lastmod>")
        lines.append(f'    <xhtml:link rel="alternate" hreflang="it-IT" href="{it_url}"/>')
        lines.append(f'    <xhtml:link rel="alternate" hreflang="en-GB" href="{en_url}"/>')
        lines.append("  </url>")
        lines.append("  <url>")
        lines.append(f"    <loc>{en_url}</loc>")
        lines.append(f"    <lastmod>{TODAY}</lastmod>")
        lines.append(f'    <xhtml:link rel="alternate" hreflang="it-IT" href="{it_url}"/>')
        lines.append(f'    <xhtml:link rel="alternate" hreflang="en-GB" href="{en_url}"/>')
        lines.append("  </url>")
    lines.append("</urlset>")
    write(ROOT / "sitemap.xml", "\n".join(lines))


def build_favicon():
    try:
        from PIL import Image
        src = ROOT / "img" / "logo-sc-mark.png"
        if src.exists():
            img = Image.open(src).convert("RGBA")
            img.resize((32, 32), Image.Resampling.LANCZOS).save(ROOT / "img" / "favicon.png")
    except Exception as e:
        print("favicon skip:", e)


def main():
    for lang in ("it", "en"):
        build_index(lang)
        build_about(lang)
        build_ai_blockchain(lang)
        build_tech(lang)
        build_hospitality(lang)
        build_fitness(lang)
        build_portfolio(lang)
        build_blog(lang)
        build_contact(lang)
        build_cv(lang)
        for art in ARTICLES:
            build_article(lang, art)
    build_root_redirect()
    build_sitemap()
    build_favicon()
    print("Site built: IT + EN pages generated.")


if __name__ == "__main__":
    main()