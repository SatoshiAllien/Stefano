# Guida Hosting — Stefano Ciancimino Portfolio

Sito statico HTML/CSS/JS nella cartella `stefano-ciancimino/`, indipendente dal sito Piergigi Ferrara nella root del repository.

Per pubblicarlo, usa un **repository GitHub dedicato** oppure configura Netlify con publish directory `stefano-ciancimino/`.

## Opzione 1: GitHub Pages (consigliata)

Il repository include già il workflow `.github/workflows/pages.yml`.

### Passaggi

1. Crea un repository GitHub (es. `stefano-ciancimino-portfolio`)
2. Carica tutti i file del sito nella root del repository
3. Vai su **Settings → Pages**
4. In **Source**, seleziona **GitHub Actions**
5. Esegui push sul branch `main` — il deploy parte automaticamente
6. Il sito sarà disponibile su `https://tuousername.github.io/nome-repo/`

### Dominio personalizzato

1. Acquista un dominio (es. `stefanociancimino.dev`)
2. In **Settings → Pages → Custom domain**, inserisci il dominio
3. Configura i DNS del registrar:
   - Tipo `A` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - Oppure `CNAME` → `tuousername.github.io`
4. Aggiorna gli URL in `sitemap.xml` e i tag `canonical` nelle pagine HTML

### Anteprima locale

```bash
cd /percorso/sito
python3 -m http.server 8080
# Apri http://localhost:8080
```

Oppure usa lo script incluso:

```bash
./avvia-sito.sh
```

---

## Opzione 2: Netlify

1. Vai su [netlify.com](https://www.netlify.com) e crea un account
2. Trascina la cartella del sito in **Sites → Add new site → Deploy manually**
3. Il sito è online in pochi secondi con URL `*.netlify.app`
4. Per dominio custom: **Domain settings → Add custom domain**

### Deploy automatico da Git

1. Collega il repository GitHub a Netlify
2. Build command: *(lascia vuoto)*
3. Publish directory: `/` (root)
4. Ogni push su `main` aggiorna il sito automaticamente

---

## Personalizzazioni post-deploy

| Elemento | File da modificare |
|----------|-------------------|
| Foto professionale | Sostituisci `img/profile.svg` con `img/profile.jpg` e aggiorna i riferimenti |
| Link Calendly | `consulenza.html` — sostituisci il placeholder con iframe Calendly |
| Dominio in SEO | `sitemap.xml`, tag `canonical` in ogni `.html` |
| Email form backend | Integra Formspree, Netlify Forms o EmailJS in `js/main.js` |

---

## SEO checklist

- [x] Meta description su ogni pagina
- [x] Tag Open Graph
- [x] `sitemap.xml`
- [x] `robots.txt`
- [x] HTML semantico (header, nav, article, footer)
- [x] URL canonical
- [ ] Google Search Console — aggiungi il sito dopo il deploy
- [ ] Google Analytics (opzionale)

---

## Struttura file

```
├── index.html          # Homepage
├── chi-sono.html       # Bio e valori
├── competenze.html     # Skills + AI/Blockchain
├── esperienza.html     # Timeline carriera
├── portfolio.html      # Progetti
├── blog.html           # Lista articoli
├── articolo-*.html     # Articoli singoli
├── consulenza.html     # Servizi + form
├── contatti.html       # Contatti + QR CV
├── cv.html             # CV stampabile
├── css/style.css       # Design system + dark mode
├── js/main.js          # Navigazione, animazioni, form
├── js/chatbot.js       # Bot AI integrato
├── sitemap.xml
├── robots.txt
└── img/profile.svg     # Foto placeholder
```