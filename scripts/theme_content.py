"""Fitness & Hospitality thematic blog content — IT/EN."""

FITNESS_CATEGORIES = {
    "it": ["Tutti", "Ipertrofia", "Definizione", "Nutrizione", "Salute", "Integrazione", "Guide"],
    "en": ["All", "Hypertrophy", "Cutting", "Nutrition", "Health", "Supplements", "Guides"],
}

HOSPITALITY_CATEGORIES = {
    "it": ["Tutti", "Formazione", "Esperienze", "Cocktail USA", "Cocktail Intl", "Mixology", "Stories"],
    "en": ["All", "Training", "Experience", "US Cocktails", "Intl Cocktails", "Mixology", "Stories"],
}

FITNESS_ARTICLES = [
    {
        "slug": "bodybuilding-massa",
        "cat": {"it": "Ipertrofia", "en": "Hypertrophy"},
        "img": "fitness-blog-hero.jpg",
        "date": "2026-06-20",
        "read": {"it": "8 min", "en": "8 min"},
        "title": {"it": "Bodybuilding & Massa Muscolare", "en": "Bodybuilding & Muscle Mass"},
        "desc": {"it": "Principi dell'ipertrofia, volume, progressione e alimentazione ipercalorica pulita.", "en": "Hypertrophy principles, volume, progression and clean hypercaloric nutrition."},
        "body": {
            "it": """<p>Con oltre 15 anni di bodybuilding, la crescita muscolare non è mistero: è metodo, costanza e recupero intelligente.</p>
<h2>Principi dell'ipertrofia</h2><p>Lo stimolo meccanico progressivo è la regola d'oro. Senza aumentare tensione, volume o frequenza nel tempo, il corpo non ha motivo di adattarsi.</p>
<h2>Volume e intensità</h2><ul><li><strong>Volume:</strong> 10–20 serie efficaci/settimana per gruppo muscolare</li><li><strong>Intensità:</strong> RIR 1–3 sulle serie principali, tecnica impeccabile</li><li><strong>Frequenza:</strong> 2x/settimana per i distretti principali</li></ul>
<h2>Progressione</h2><p>Aumenta carico, ripetizioni o serie ogni 1–2 settimane. Logga ogni sessione — ciò che non misuri, non migliori.</p>
<h2>Recupero e sonno</h2><p>7–9 ore di sonno, giorni di scarico ogni 4–6 settimane, gestione dello stress. I muscoli crescono quando riposi.</p>
<h2>Alimentazione ipercalorica pulita</h2><p>Surplus moderato +300–500 kcal, cibi integrali, proteine a ogni pasto. Surplus non significa junk food.</p>
<h2>Errori comuni</h2><ul><li>Allenarsi ogni giorno senza recupero</li><li>Surplus eccessivo → troppo grasso</li><li>Cambiare programma ogni mese</li><li>Trascurare le proteine (&lt;1.6 g/kg)</li></ul>""",
            "en": """<p>With over 15 years of bodybuilding, muscle growth is not mystery — it is method, consistency and smart recovery.</p>
<h2>Hypertrophy principles</h2><p>Progressive mechanical tension is the golden rule. Without increasing tension, volume or frequency over time, the body has no reason to adapt.</p>
<h2>Volume and intensity</h2><ul><li><strong>Volume:</strong> 10–20 effective sets/week per muscle group</li><li><strong>Intensity:</strong> RIR 1–3 on main sets, impeccable form</li><li><strong>Frequency:</strong> 2x/week for major muscle groups</li></ul>
<h2>Progression</h2><p>Increase load, reps or sets every 1–2 weeks. Log every session — what you don't measure, you don't improve.</p>
<h2>Recovery and sleep</h2><p>7–9 hours of sleep, deload weeks every 4–6 weeks, stress management. Muscles grow when you rest.</p>
<h2>Clean hypercaloric nutrition</h2><p>Moderate surplus +300–500 kcal, whole foods, protein at every meal. Surplus does not mean junk food.</p>
<h2>Common mistakes</h2><ul><li>Training daily without recovery</li><li>Excessive surplus → too much fat</li><li>Changing programme every month</li><li>Neglecting protein (&lt;1.6 g/kg)</li></ul>""",
        },
    },
    {
        "slug": "definizione-muscolare",
        "cat": {"it": "Definizione", "en": "Cutting"},
        "img": "fitness-nutrition.jpg",
        "date": "2026-06-18",
        "read": {"it": "7 min", "en": "7 min"},
        "title": {"it": "Definizione Muscolare", "en": "Muscle Definition & Cutting"},
        "desc": {"it": "Deficit calorico intelligente, macro per il taglio e come mantenere la massa.", "en": "Smart caloric deficit, cutting macros and preserving muscle mass."},
        "body": {
            "it": """<h2>Deficit calorico intelligente</h2><p>-300/500 kcal dal TDEE. Tagli più aggressivi sacrificano massa muscolare e performance.</p>
<h2>Macronutrienti per la definizione</h2><ul><li><strong>Proteine:</strong> 2–2.4 g/kg (priorità assoluta)</li><li><strong>Grassi:</strong> 0.8–1 g/kg (ormoni e sazietà)</li><li><strong>Carboidrati:</strong> il resto, concentrati pre/post workout</li></ul>
<h2>Cardio vs HIIT</h2><p>LISS (corsa, bici) per deficit extra senza stress eccessivo. HIIT 1–2x/settimana per efficienza. Non abusare — interferisce col recupero.</p>
<h2>Mantenere la massa durante il taglio</h2><ul><li>Mantenere intensità sui big lift</li><li>Proteine alte e distribuite</li><li>Deficit moderato e pazienza</li><li>Refeed strategici se taglio lungo</li></ul>""",
            "en": """<h2>Smart caloric deficit</h2><p>-300/500 kcal from TDEE. More aggressive cuts sacrifice muscle mass and performance.</p>
<h2>Cutting macronutrients</h2><ul><li><strong>Protein:</strong> 2–2.4 g/kg (absolute priority)</li><li><strong>Fats:</strong> 0.8–1 g/kg (hormones and satiety)</li><li><strong>Carbs:</strong> remainder, focused pre/post workout</li></ul>
<h2>Cardio vs HIIT</h2><p>LISS (running, cycling) for extra deficit without excessive stress. HIIT 1–2x/week for efficiency. Don't overdo it — it interferes with recovery.</p>
<h2>Preserving mass during a cut</h2><ul><li>Maintain intensity on big lifts</li><li>High, distributed protein</li><li>Moderate deficit and patience</li><li>Strategic refeeds on long cuts</li></ul>""",
        },
    },
    {
        "slug": "nutrizione-sportiva",
        "cat": {"it": "Nutrizione", "en": "Nutrition"},
        "img": "fitness-nutrition.jpg",
        "date": "2026-06-15",
        "read": {"it": "7 min", "en": "7 min"},
        "title": {"it": "Nutrizione Sportiva", "en": "Sports Nutrition"},
        "desc": {"it": "Bilanciamento macro, timing pasti, idratazione e scelte alimentari.", "en": "Macro balance, meal timing, hydration and food choices."},
        "body": {
            "it": """<h2>Bilanciamento macro</h2><p>Proteine stabili, grassi essenziali, carboidrati variabili in base all'attività. Non esistono macro universali — esiste il contesto.</p>
<h2>Timing dei pasti</h2><p>4–5 pasti al giorno, proteine distribuite (30–40 g/pasto). Pre-workout: carboidrati facili. Post-workout: proteine + carboidrati entro 2 ore.</p>
<h2>Idratazione</h2><p>2–3 litri/die, di più con cardio o caldo. Urina chiara = buon indicatore.</p>
<h2>Cibi consigliati</h2><ul><li>Carni magre, pesce, uova</li><li>Riso, avena, patate, pasta integrale</li><li>Verdura abbondante, frutta intera</li><li>Grassi buoni: olio EVO, avocado, noci</li></ul>
<h2>Cibi da limitare</h2><ul><li>Zucchero raffinato e bevande zuccherate</li><li>Ultra-processati quotidiani</li><li>Alcol frequente</li></ul>""",
            "en": """<h2>Macro balance</h2><p>Stable protein, essential fats, variable carbs based on activity. No universal macros — context matters.</p>
<h2>Meal timing</h2><p>4–5 meals daily, distributed protein (30–40 g/meal). Pre-workout: easy carbs. Post-workout: protein + carbs within 2 hours.</p>
<h2>Hydration</h2><p>2–3 litres/day, more with cardio or heat. Clear urine = good indicator.</p>
<h2>Recommended foods</h2><ul><li>Lean meats, fish, eggs</li><li>Rice, oats, potatoes, wholegrain pasta</li><li>Plenty of vegetables, whole fruit</li><li>Good fats: olive oil, avocado, nuts</li></ul>
<h2>Foods to limit</h2><ul><li>Refined sugar and sugary drinks</li><li>Daily ultra-processed foods</li><li>Frequent alcohol</li></ul>""",
        },
    },
    {
        "slug": "zucchero-raffinato",
        "cat": {"it": "Salute", "en": "Health"},
        "img": "fitness-hero.jpg",
        "date": "2026-06-12",
        "read": {"it": "5 min", "en": "5 min"},
        "title": {"it": "Perché evitare lo zucchero raffinato", "en": "Why avoid refined sugar"},
        "desc": {"it": "Effetti metabolici, infiammazione, dipendenza e alternative sane.", "en": "Metabolic effects, inflammation, dependency and healthy alternatives."},
        "body": {
            "it": """<h2>Effetti metabolici</h2><p>Calorie vuote, picchi glicemici, resistenza insulinica nel lungo periodo. Nemico della composizione corporea e dell'energia stabile.</p>
<h2>Infiammazione</h2><p>Picchi ripetuti favoriscono infiammazione di basso grado — compromette recupero, sonno e salute generale.</p>
<h2>Dipendenza</h2><p>Ciclo picco-crollo → craving → più zucchero. Rompere il ciclo richiede 2–3 settimane di riduzione graduale.</p>
<h2>Alternative sane</h2><ul><li>Frutta intera (fibra rallenta assorbimento)</li><li>Miele crudo con moderazione</li><li>Dark chocolate 85%+</li><li>Dolcificanti naturali se necessario</li></ul>""",
            "en": """<h2>Metabolic effects</h2><p>Empty calories, glycaemic spikes, long-term insulin resistance. Enemy of body composition and stable energy.</p>
<h2>Inflammation</h2><p>Repeated spikes promote low-grade inflammation — compromises recovery, sleep and general health.</p>
<h2>Dependency</h2><p>Spike-crash cycle → cravings → more sugar. Breaking the cycle takes 2–3 weeks of gradual reduction.</p>
<h2>Healthy alternatives</h2><ul><li>Whole fruit (fibre slows absorption)</li><li>Raw honey in moderation</li><li>Dark chocolate 85%+</li><li>Natural sweeteners if needed</li></ul>""",
        },
    },
    {
        "slug": "integrazione-proteica",
        "cat": {"it": "Integrazione", "en": "Supplements"},
        "img": "fitness-nutrition.jpg",
        "date": "2026-06-10",
        "read": {"it": "6 min", "en": "6 min"},
        "title": {"it": "Integrazione proteica", "en": "Protein supplementation"},
        "desc": {"it": "Whey, caseine, vegetali — quando usarle, benefici e dosaggi.", "en": "Whey, casein, plant-based — when to use, benefits and dosages."},
        "body": {
            "it": """<h2>Tipi di proteine</h2><ul><li><strong>Whey:</strong> assorbimento rapido, ideale post-workout</li><li><strong>Caseina:</strong> rilascio lento, pre-nanna o tra pasti lunghi</li><li><strong>Vegetali:</strong> pisello, riso, soia — per intolleranze o scelta etica</li></ul>
<h2>Quando usarle</h2><p>Quando non raggiungi 1.6–2.2 g/kg con il cibo. Non sostituiscono pasti interi — integrano.</p>
<h2>Benefici per la massa</h2><p>Comodità, recupero, mantenimento massa in deficit. Strumento utile, non magia.</p>
<h2>Dosaggi consigliati</h2><p>20–40 g per serving, 1–2 shake al giorno se necessario. Il totale giornaliero conta più del timing perfetto.</p>""",
            "en": """<h2>Protein types</h2><ul><li><strong>Whey:</strong> fast absorption, ideal post-workout</li><li><strong>Casein:</strong> slow release, pre-sleep or between long meals</li><li><strong>Plant-based:</strong> pea, rice, soy — for intolerances or ethical choice</li></ul>
<h2>When to use</h2><p>When you cannot reach 1.6–2.2 g/kg from food. They supplement — they don't replace whole meals.</p>
<h2>Benefits for muscle mass</h2><p>Convenience, recovery, mass maintenance in deficit. Useful tool, not magic.</p>
<h2>Recommended dosages</h2><p>20–40 g per serving, 1–2 shakes daily if needed. Daily total matters more than perfect timing.</p>""",
        },
    },
    {
        "slug": "routine-settimanale",
        "cat": {"it": "Guide", "en": "Guides"},
        "img": "fitness-hero.jpg",
        "date": "2026-06-08",
        "read": {"it": "4 min", "en": "4 min"},
        "title": {"it": "Routine settimanale", "en": "Weekly training routine"},
        "desc": {"it": "Split push/pull/legs, cardio e recupero attivo.", "en": "Push/pull/legs split, cardio and active recovery."},
        "body": {
            "it": """<ul><li><strong>Lun/Mer/Ven:</strong> Pesi — push, pull, legs</li><li><strong>Mar/Gio:</strong> Corsa o bici 45–60 min LISS</li><li><strong>Sab:</strong> Outdoor, funzionale o trail</li><li><strong>Dom:</strong> Riposo attivo, stretching, mobilità</li></ul>
<p>4–5 sessioni efficaci battono 7 sessioni mediocri. La costanza nel lungo periodo è tutto.</p>""",
            "en": """<ul><li><strong>Mon/Wed/Fri:</strong> Weights — push, pull, legs</li><li><strong>Tue/Thu:</strong> Run or bike 45–60 min LISS</li><li><strong>Sat:</strong> Outdoor, functional or trail</li><li><strong>Sun:</strong> Active rest, stretching, mobility</li></ul>
<p>4–5 effective sessions beat 7 mediocre ones. Long-term consistency is everything.</p>""",
        },
    },
    {
        "slug": "consigli-principianti",
        "cat": {"it": "Guide", "en": "Guides"},
        "img": "fitness-blog-hero.jpg",
        "date": "2026-06-05",
        "read": {"it": "5 min", "en": "5 min"},
        "title": {"it": "Consigli per principianti", "en": "Tips for beginners"},
        "desc": {"it": "Come iniziare senza errori e costruire abitudini sostenibili.", "en": "How to start without mistakes and build sustainable habits."},
        "body": {
            "it": """<ul><li>Inizia con 3 sessioni/settimana, non 6</li><li>Impara la tecnica prima del carico</li><li>Proteine ad ogni pasto principale</li><li>Dormi 7+ ore — non negoziabile</li><li>Non confrontarti con chi allena da 10 anni</li><li>Logga allenamenti e pasti per 4 settimane</li></ul>""",
            "en": """<ul><li>Start with 3 sessions/week, not 6</li><li>Learn technique before load</li><li>Protein at every main meal</li><li>Sleep 7+ hours — non-negotiable</li><li>Don't compare yourself to 10-year veterans</li><li>Log workouts and meals for 4 weeks</li></ul>""",
        },
    },
    {
        "slug": "consigli-avanzati",
        "cat": {"it": "Guide", "en": "Guides"},
        "img": "fitness-hero.jpg",
        "date": "2026-06-03",
        "read": {"it": "5 min", "en": "5 min"},
        "title": {"it": "Consigli avanzati", "en": "Advanced tips"},
        "desc": {"it": "Periodizzazione, deload e ottimizzazione per atleti esperti.", "en": "Periodisation, deloads and optimisation for experienced athletes."},
        "body": {
            "it": """<ul><li>Periodizza volume e intensità ogni 4–6 settimane</li><li>Deload obbligatorio prima di stallo o infortunio</li><li>Track HRV e sonno per auto-regolazione</li><li>Mesocicli ipertrofia → forza → definizione</li><li>Specializza 1–2 distretti debole per blocco</li></ul>""",
            "en": """<ul><li>Periodise volume and intensity every 4–6 weeks</li><li>Mandatory deload before plateau or injury</li><li>Track HRV and sleep for auto-regulation</li><li>Hypertrophy → strength → cutting mesocycles</li><li>Specialise 1–2 weak points per block</li></ul>""",
        },
    },
    {
        "slug": "allenamento-outdoor",
        "cat": {"it": "Guide", "en": "Guides"},
        "img": "fitness-hero.jpg",
        "date": "2026-06-01",
        "read": {"it": "4 min", "en": "4 min"},
        "title": {"it": "Allenamento outdoor", "en": "Outdoor training"},
        "desc": {"it": "Corsa, bici, trail e sport outdoor per equilibrio mente-corpo.", "en": "Running, cycling, trail and outdoor sports for mind-body balance."},
        "body": {
            "it": """<p>Il fitness non deve stare solo in palestra. Corsa su strada, bici da corsa, trekking e trail completano forza e cardio.</p>
<ul><li><strong>Corsa:</strong> base aerobica, resistenza mentale</li><li><strong>Bici:</strong> potenza gambe, zero impatto articolare</li><li><strong>Trail:</strong> variabilità, natura, equilibrio</li></ul>
<p>1–2 sessioni outdoor a settimana migliorano recupero psicologico e adherence.</p>""",
            "en": """<p>Fitness doesn't have to stay in the gym. Road running, road cycling, hiking and trail complement strength and cardio.</p>
<ul><li><strong>Running:</strong> aerobic base, mental endurance</li><li><strong>Cycling:</strong> leg power, zero joint impact</li><li><strong>Trail:</strong> variability, nature, balance</li></ul>
<p>1–2 outdoor sessions weekly improve psychological recovery and adherence.</p>""",
        },
    },
    {
        "slug": "recupero-mobilita",
        "cat": {"it": "Guide", "en": "Guides"},
        "img": "fitness-nutrition.jpg",
        "date": "2026-05-28",
        "read": {"it": "5 min", "en": "5 min"},
        "title": {"it": "Recupero e mobilità", "en": "Recovery and mobility"},
        "desc": {"it": "Stretching, foam rolling, sonno e gestione dello stress.", "en": "Stretching, foam rolling, sleep and stress management."},
        "body": {
            "it": """<h2>Recupero attivo</h2><p>Camminata leggera, yoga, stretching dinamico nei giorni off.</p>
<h2>Mobilità</h2><p>10 min pre-workout: cat-cow, hip circles, shoulder dislocations. Previene infortuni e migliora performance.</p>
<h2>Foam rolling</h2><p>Quad, glutei, dorsale post-allenamento. 1–2 min per area, respirazione lenta.</p>
<h2>Sonno</h2><p>7–9 ore, stanza fresca e buia, niente schermi 1h prima. Il sonno è il miglior integratore.</p>""",
            "en": """<h2>Active recovery</h2><p>Light walking, yoga, dynamic stretching on off days.</p>
<h2>Mobility</h2><p>10 min pre-workout: cat-cow, hip circles, shoulder dislocations. Prevents injury and improves performance.</p>
<h2>Foam rolling</h2><p>Quads, glutes, lats post-workout. 1–2 min per area, slow breathing.</p>
<h2>Sleep</h2><p>7–9 hours, cool dark room, no screens 1h before. Sleep is the best supplement.</p>""",
        },
    },
]

def _cocktail_body(name, story_it, story_en, ing_it, ing_en, tech_it, tech_en, glass, garnish, variants_it, variants_en):
    return {
        "it": f"""<div class="recipe-card"><h2>Storia</h2><p>{story_it}</p>
<h2>Ingredienti</h2><ul>{ing_it}</ul>
<h2>Preparazione</h2><p>{tech_it}</p>
<h2>Bicchiere</h2><p>{glass}</p>
<h2>Garnish</h2><p>{garnish}</p>
<h2>Varianti moderne</h2><p>{variants_it}</p></div>""",
        "en": f"""<div class="recipe-card"><h2>History</h2><p>{story_en}</p>
<h2>Ingredients</h2><ul>{ing_en}</ul>
<h2>Method</h2><p>{tech_en}</p>
<h2>Glass</h2><p>{glass}</p>
<h2>Garnish</h2><p>{garnish}</p>
<h2>Modern variations</h2><p>{variants_en}</p></div>""",
    }

HOSPITALITY_ARTICLES = [
    {
        "slug": "aibes-formazione",
        "cat": {"it": "Formazione", "en": "Training"},
        "img": "hospitality-bar.jpg",
        "date": "2026-06-20",
        "read": {"it": "7 min", "en": "7 min"},
        "title": {"it": "Formazione AIBES — Barman Professionale", "en": "AIBES Training — Professional Bartender"},
        "desc": {"it": "Corso professionale presso AIBES: tecniche, standard internazionali e cultura del bar.", "en": "Professional course at AIBES: techniques, international standards and bar culture."},
        "body": {
            "it": """<p>La mia formazione professionale è stata completata presso <strong><a href="https://aibes.it/" target="_blank" rel="noopener">AIBES – Associazione Italiana Barman e Sostenitori</a></strong>, punto di riferimento in Italia per la qualifica barman.</p>
<h2>Formazione professionale</h2><p>Programma strutturato su tecnica di servizio, igiene, organizzazione del banco e standard internazionali IBA.</p>
<h2>Tecniche di miscelazione</h2><ul><li>Stir — cocktail spiritosi e armoniosi</li><li>Shake — texture aerata e temperatura</li><li>Build — drink veloci ad alto volume</li><li>Muddle — estrazione aromi freschi</li></ul>
<h2>Approccio professionale</h2><p>Precisione nelle dosi, pulizia del banco, velocità senza sacrificare qualità. Lo stesso mindset che applico oggi in antifrode e operations.</p>""",
            "en": """<p>My professional training was completed at <strong><a href="https://aibes.it/" target="_blank" rel="noopener">AIBES – Italian Barman and Supporters Association</a></strong>, Italy's reference point for bartender qualification.</p>
<h2>Professional training</h2><p>Structured programme on service technique, hygiene, bar organisation and IBA international standards.</p>
<h2>Mixing techniques</h2><ul><li>Stir — spirit-forward harmonious cocktails</li><li>Shake — aerated texture and temperature</li><li>Build — fast high-volume drinks</li><li>Muddle — fresh aroma extraction</li></ul>
<h2>Professional approach</h2><p>Dose precision, clean bar, speed without sacrificing quality. The same mindset I apply today in fraud and operations.</p>""",
        },
    },
    {
        "slug": "uk-rsc-corporate",
        "cat": {"it": "Esperienze", "en": "Experience"},
        "img": "hospitality-blog-hero.jpg",
        "date": "2026-06-18",
        "read": {"it": "8 min", "en": "8 min"},
        "title": {"it": "Inghilterra: RSC e eventi corporate", "en": "England: RSC and corporate events"},
        "desc": {"it": "Royal Shakespeare Company, hospitality VIP e bar ad alto volume.", "en": "Royal Shakespeare Company, VIP hospitality and high-volume bars."},
        "body": {
            "it": """<p>Anni in <strong>Inghilterra</strong> tra hotel di fascia alta, <strong>Royal Shakespeare Company</strong>, eventi corporate e bar ad altissimo volume.</p>
<h2>Royal Shakespeare Company</h2><p>Intervalli stretti, centinaia di coperti, standard inglesi rigorosi. Ogni secondo conta dietro il bancone.</p>
<h2>Eventi corporate</h2><p>Clientela VIP, servizio impeccabile, coordinamento team multiculturali. Precisione e calma sotto pressione.</p>
<h2>Cocktail bar ad alto volume</h2><p>Code al bancone, drink ripetitivi a velocità sostenuta senza errori. La disciplina inglese forgia resilienza operativa.</p>""",
            "en": """<p>Years in <strong>England</strong> across upscale hotels, the <strong>Royal Shakespeare Company</strong>, corporate events and very high-volume bars.</p>
<h2>Royal Shakespeare Company</h2><p>Tight intervals, hundreds of covers, rigorous English standards. Every second counts behind the bar.</p>
<h2>Corporate events</h2><p>VIP clientele, impeccable service, multicultural team coordination. Precision and calm under pressure.</p>
<h2>High-volume cocktail bars</h2><p>Bar queues, repetitive drinks at sustained speed without errors. English discipline forges operational resilience.</p>""",
        },
    },
    {
        "slug": "sudafrica-sony-kodak",
        "cat": {"it": "Esperienze", "en": "Experience"},
        "img": "hospitality-sa-tech.jpg",
        "date": "2026-06-15",
        "read": {"it": "8 min", "en": "8 min"},
        "title": {"it": "Esperienza Professionale in Sudafrica – Sony Vaio & Kodak", "en": "Professional Experience in South Africa – Sony Vaio & Kodak"},
        "desc": {"it": "Italian Technical Support Agent: supporto tecnico Sony Vaio e Kodak per clienti italiani.", "en": "Italian Technical Support Agent: Sony Vaio and Kodak technical support for Italian customers."},
        "body": {
            "it": """<p>In <strong>Sudafrica</strong> ho ricoperto il ruolo di <strong>Italian Technical Support Agent – Sony Vaio / Kodak</strong>. Un'esperienza nel settore tecnico, non hospitality.</p>
<h2>Supporto clienti italiani</h2><p>Assistenza professionale via telefono, email e CRM per utenti italiani con prodotti Sony Vaio e Kodak.</p>
<h2>Sony Vaio</h2><ul><li>Troubleshooting avanzato notebook</li><li>Diagnosi hardware e software</li><li>Escalation tecniche documentate</li></ul>
<h2>Kodak</h2><ul><li>Stampanti, fotocamere digitali e scanner</li><li>Coordinamento con ingegneri Kodak</li><li>Invio tecnici on-site per plotter e stampanti professionali</li><li>Rispetto SLA e standard operativi</li></ul>
<p>Competenze trasferite oggi in customer operations, troubleshooting e documentazione casi complessi.</p>""",
            "en": """<p>In <strong>South Africa</strong> I held the role of <strong>Italian Technical Support Agent – Sony Vaio / Kodak</strong>. A technical sector experience, not hospitality.</p>
<h2>Italian customer support</h2><p>Professional assistance via phone, email and CRM for Italian users with Sony Vaio and Kodak products.</p>
<h2>Sony Vaio</h2><ul><li>Advanced laptop troubleshooting</li><li>Hardware and software diagnostics</li><li>Documented technical escalations</li></ul>
<h2>Kodak</h2><ul><li>Printers, digital cameras and scanners</li><li>Coordination with Kodak engineering teams</li><li>On-site engineer dispatch for plotters and professional printers</li><li>SLA compliance and operational standards</li></ul>
<p>Skills transferred today to customer operations, troubleshooting and complex case documentation.</p>""",
        },
    },
    {
        "slug": "manhattan",
        "cat": {"it": "Cocktail USA", "en": "US Cocktails"},
        "img": "hospitality-cocktail.jpg",
        "date": "2026-06-12",
        "read": {"it": "4 min", "en": "4 min"},
        "title": {"it": "Manhattan", "en": "Manhattan"},
        "desc": {"it": "Il classico newyorkese: whiskey, vermouth e bitter.", "en": "The New York classic: whiskey, vermouth and bitters."},
        "body": _cocktail_body("Manhattan",
            "Nato a New York nella seconda metà dell'800, il Manhattan è il cocktail americano per eccellenza — elegante, secco, senza tempo.",
            "Born in New York in the late 1800s, the Manhattan is the quintessential American cocktail — elegant, dry, timeless.",
            "<li>60 ml Rye whiskey</li><li>30 ml Vermouth rosso</li><li>2 dash Angostura bitter</li><li>Ghiaccio</li>",
            "<li>60 ml Rye whiskey</li><li>30 ml Sweet vermouth</li><li>2 dashes Angostura bitters</li><li>Ice</li>",
            "Stir in mixing glass con ghiaccio per 30 secondi. Strain in coppa fredda.",
            "Stir in mixing glass with ice for 30 seconds. Strain into chilled coupe.",
            "Coppa cocktail o on the rocks", "Ciliegia maraschino o scorza arancia",
            "Perfect Manhattan (metà dry/metà sweet vermouth), Black Manhattan (Averna al posto del vermouth)",
            "Perfect Manhattan (half dry/half sweet vermouth), Black Manhattan (Averna instead of vermouth)"),
    },
    {
        "slug": "old-fashioned",
        "cat": {"it": "Cocktail USA", "en": "US Cocktails"},
        "img": "hospitality-cocktail.jpg",
        "date": "2026-06-11",
        "read": {"it": "4 min", "en": "4 min"},
        "title": {"it": "Old Fashioned", "en": "Old Fashioned"},
        "desc": {"it": "Il cocktail più antico d'America — puro e potente.", "en": "America's oldest cocktail — pure and powerful."},
        "body": _cocktail_body("Old Fashioned",
            "Il cocktail originale: spirito, zucchero, bitter, acqua. Bourbon o rye, senza fronzoli.",
            "The original cocktail: spirit, sugar, bitters, water. Bourbon or rye, no frills.",
            "<li>60 ml Bourbon o Rye</li><li>1 cubetto zucchero o 5 ml sciroppo</li><li>2 dash Angostura</li><li>Splash acqua</li>",
            "<li>60 ml Bourbon or Rye</li><li>1 sugar cube or 5 ml syrup</li><li>2 dashes Angostura</li><li>Splash water</li>",
            "Muddle zucchero e bitter, aggiungi whiskey e ghiaccio grande. Stir delicato. Garnish.",
            "Muddle sugar and bitters, add whiskey and large ice. Stir gently. Garnish.",
            "Rocks glass", "Scorza arancia espressa",
            "Smoked Old Fashioned, Rum Old Fashioned, Oaxaca Old Fashioned (mezcal + tequila)",
            "Smoked Old Fashioned, Rum Old Fashioned, Oaxaca Old Fashioned (mezcal + tequila)"),
    },
    {
        "slug": "whiskey-sour",
        "cat": {"it": "Cocktail USA", "en": "US Cocktails"},
        "img": "hospitality-cocktail.jpg",
        "date": "2026-06-10",
        "read": {"it": "4 min", "en": "4 min"},
        "title": {"it": "Whiskey Sour", "en": "Whiskey Sour"},
        "desc": {"it": "Equilibrio perfetto tra dolce, acido e spirito.", "en": "Perfect balance of sweet, sour and spirit."},
        "body": _cocktail_body("Whiskey Sour",
            "Classico pre-Prohibition. Il bilanciamento acido/dolce è la chiave — come in ogni grande cocktail.",
            "Pre-Prohibition classic. Sweet/sour balance is the key — as in every great cocktail.",
            "<li>60 ml Bourbon</li><li>30 ml Succo limone fresco</li><li>20 ml Sciroppo semplice</li><li>1 albume (opzionale)</li>",
            "<li>60 ml Bourbon</li><li>30 ml Fresh lemon juice</li><li>20 ml Simple syrup</li><li>1 egg white (optional)</li>",
            "Shake vigoroso senza ghiaccio (dry shake) se con albume, poi shake con ghiaccio. Strain in rocks.",
            "Hard shake without ice (dry shake) if using egg white, then shake with ice. Strain into rocks.",
            "Rocks glass", "Ciliegia e fetta limone",
            "New York Sour (float vino rosso), Boston Sour (albume standard)",
            "New York Sour (red wine float), Boston Sour (standard egg white)"),
    },
    {
        "slug": "mint-julep",
        "cat": {"it": "Cocktail USA", "en": "US Cocktails"},
        "img": "hospitality-cocktail.jpg",
        "date": "2026-06-09",
        "read": {"it": "3 min", "en": "3 min"},
        "title": {"it": "Mint Julep", "en": "Mint Julep"},
        "desc": {"it": "Il drink del Kentucky Derby — bourbon e menta fresca.", "en": "The Kentucky Derby drink — bourbon and fresh mint."},
        "body": _cocktail_body("Mint Julep",
            "Simbolo del Kentucky Derby. Menta fresca schiacciata delicatamente — mai over-muddle.",
            "Symbol of the Kentucky Derby. Fresh mint gently muddled — never over-muddle.",
            "<li>60 ml Bourbon</li><li>10–15 foglie menta fresca</li><li>10 ml Sciroppo semplice</li><li>Ghiaccio tritato</li>",
            "<li>60 ml Bourbon</li><li>10–15 fresh mint leaves</li><li>10 ml Simple syrup</li><li>Crushed ice</li>",
            "Muddle menta con sciroppo (leggero). Bourbon e ghiaccio tritato. Churn. Coppa ghiacciata.",
            "Lightly muddle mint with syrup. Bourbon and crushed ice. Churn. Frosted cup.",
            "Julep cup o rocks", "Rametto menta e powdered sugar",
            "Peach Julep, Raspberry Julep",
            "Peach Julep, Raspberry Julep"),
    },
    {
        "slug": "sazerac",
        "cat": {"it": "Cocktail USA", "en": "US Cocktails"},
        "img": "hospitality-cocktail.jpg",
        "date": "2026-06-08",
        "read": {"it": "4 min", "en": "4 min"},
        "title": {"it": "Sazerac", "en": "Sazerac"},
        "desc": {"it": "Il cocktail ufficiale di New Orleans.", "en": "The official cocktail of New Orleans."},
        "body": _cocktail_body("Sazerac",
            "Nato a New Orleans. Rinse assenzio nel bicchiere — il segreto è non esagerare.",
            "Born in New Orleans. Absinthe rinse in the glass — the secret is not to overdo it.",
            "<li>60 ml Rye whiskey</li><li>1 cubetto zucchero</li><li>3 dash Peychaud's bitter</li><li>Rinse Assenzio</li>",
            "<li>60 ml Rye whiskey</li><li>1 sugar cube</li><li>3 dashes Peychaud's bitters</li><li>Absinthe rinse</li>",
            "Rinse coppa con assenzio. Stir rye, zucchero e bitter con ghiaccio. Strain in coppa rinsata.",
            "Rinse coupe with absinthe. Stir rye, sugar and bitters with ice. Strain into rinsed coupe.",
            "Coppa cocktail", "Scorza limone",
            "Sazerac con Cognac (ricetta originale), Mezcal Sazerac",
            "Sazerac with Cognac (original recipe), Mezcal Sazerac"),
    },
    {
        "slug": "negroni",
        "cat": {"it": "Cocktail Intl", "en": "Intl Cocktails"},
        "img": "hospitality-cocktail.jpg",
        "date": "2026-06-07",
        "read": {"it": "4 min", "en": "4 min"},
        "title": {"it": "Negroni", "en": "Negroni"},
        "desc": {"it": "Il re dei cocktail italiani — equilibrio perfetto.", "en": "King of Italian cocktails — perfect balance."},
        "body": _cocktail_body("Negroni",
            "Inventato a Firenze nel 1919 per il Conte Negroni. Tre ingredienti, proporzioni uguali, perfezione.",
            "Invented in Florence in 1919 for Count Negroni. Three ingredients, equal parts, perfection.",
            "<li>30 ml Gin</li><li>30 ml Campari</li><li>30 ml Vermouth rosso</li><li>Ghiaccio</li>",
            "<li>30 ml Gin</li><li>30 ml Campari</li><li>30 ml Sweet vermouth</li><li>Ice</li>",
            "Build in rocks glass con ghiaccio grande. Stir delicato. Garnish.",
            "Build in rocks glass with large ice. Stir gently. Garnish.",
            "Rocks glass", "Scorza arancia",
            "Boulevardier (bourbon al posto del gin), Negroni Sbagliato (prosecco), White Negroni",
            "Boulevardier (bourbon instead of gin), Negroni Sbagliato (prosecco), White Negroni"),
    },
    {
        "slug": "margarita",
        "cat": {"it": "Cocktail Intl", "en": "Intl Cocktails"},
        "img": "hospitality-cocktail.jpg",
        "date": "2026-06-06",
        "read": {"it": "4 min", "en": "4 min"},
        "title": {"it": "Margarita", "en": "Margarita"},
        "desc": {"it": "Tequila, lime e triple sec — il classico messicano.", "en": "Tequila, lime and triple sec — the Mexican classic."},
        "body": _cocktail_body("Margarita",
            "Il cocktail messicano più famoso al mondo. Lime fresco, mai succo in bottiglia.",
            "The world's most famous Mexican cocktail. Fresh lime, never bottled juice.",
            "<li>50 ml Tequila blanco</li><li>25 ml Triple sec / Cointreau</li><li>25 ml Succo lime fresco</li><li>Sale per il bordo</li>",
            "<li>50 ml Blanco tequila</li><li>25 ml Triple sec / Cointreau</li><li>25 ml Fresh lime juice</li><li>Salt for rim</li>",
            "Shake con ghiaccio. Strain in coppa con bordo salato (opzionale).",
            "Shake with ice. Strain into salt-rimmed coupe (optional).",
            "Coppa o rocks", "Fetta lime",
            "Spicy Margarita (jalapeño), Tommy's Margarita (agave, no triple sec)",
            "Spicy Margarita (jalapeño), Tommy's Margarita (agave, no triple sec)"),
    },
    {
        "slug": "daiquiri",
        "cat": {"it": "Cocktail Intl", "en": "Intl Cocktails"},
        "img": "hospitality-cocktail.jpg",
        "date": "2026-06-05",
        "read": {"it": "3 min", "en": "3 min"},
        "title": {"it": "Daiquiri", "en": "Daiquiri"},
        "desc": {"it": "Rum, lime, zucchero — semplicità cubana perfetta.", "en": "Rum, lime, sugar — perfect Cuban simplicity."},
        "body": _cocktail_body("Daiquiri",
            "Cocktail cubano per eccellenza. Hemingway lo amava frozen — la versione classica è shaken.",
            "Quintessential Cuban cocktail. Hemingway loved it frozen — the classic version is shaken.",
            "<li>60 ml Rum bianco</li><li>30 ml Succo lime fresco</li><li>20 ml Sciroppo semplice</li>",
            "<li>60 ml White rum</li><li>30 ml Fresh lime juice</li><li>20 ml Simple syrup</li>",
            "Shake vigoroso con ghiaccio. Strain in coppa fredda.",
            "Hard shake with ice. Strain into chilled coupe.",
            "Coppa cocktail", "Fetta lime",
            "Hemingway Daiquiri (pompelmo, maraschino), Strawberry Daiquiri",
            "Hemingway Daiquiri (grapefruit, maraschino), Strawberry Daiquiri"),
    },
    {
        "slug": "mojito",
        "cat": {"it": "Cocktail Intl", "en": "Intl Cocktails"},
        "img": "hospitality-cocktail.jpg",
        "date": "2026-06-04",
        "read": {"it": "4 min", "en": "4 min"},
        "title": {"it": "Mojito", "en": "Mojito"},
        "desc": {"it": "Rum, menta, lime e soda — freschezza cubana.", "en": "Rum, mint, lime and soda — Cuban freshness."},
        "body": _cocktail_body("Mojito",
            "Nato a Cuba. Muddle leggero della menta — schiacciare troppo rilascia amarezza.",
            "Born in Cuba. Gentle mint muddle — crushing too hard releases bitterness.",
            "<li>60 ml Rum bianco</li><li>30 ml Succo lime</li><li>20 ml Sciroppo</li><li>8 foglie menta</li><li>Soda</li>",
            "<li>60 ml White rum</li><li>30 ml Lime juice</li><li>20 ml Syrup</li><li>8 mint leaves</li><li>Soda</li>",
            "Muddle menta e lime nel bicchiere. Rum, ghiaccio, top soda. Stir delicato.",
            "Muddle mint and lime in glass. Rum, ice, top soda. Stir gently.",
            "Highball", "Rametto menta e fetta lime",
            "Elderflower Mojito, Coconut Mojito",
            "Elderflower Mojito, Coconut Mojito"),
    },
    {
        "slug": "martini",
        "cat": {"it": "Cocktail Intl", "en": "Intl Cocktails"},
        "img": "hospitality-cocktail.jpg",
        "date": "2026-06-03",
        "read": {"it": "4 min", "en": "4 min"},
        "title": {"it": "Martini", "en": "Martini"},
        "desc": {"it": "Gin e vermouth dry — l'eleganza in un bicchiere.", "en": "Gin and dry vermouth — elegance in a glass."},
        "body": _cocktail_body("Martini",
            "Il cocktail più iconico al mondo. Gin o vodka, vermouth dry, stir — mai shake (salvo eccezioni).",
            "The world's most iconic cocktail. Gin or vodka, dry vermouth, stir — never shake (with exceptions).",
            "<li>60 ml Gin (o Vodka)</li><li>10–15 ml Vermouth dry</li><li>1 dash Orange bitter (opzionale)</li>",
            "<li>60 ml Gin (or Vodka)</li><li>10–15 ml Dry vermouth</li><li>1 dash Orange bitters (optional)</li>",
            "Stir 30 secondi in mixing glass. Strain in coppa congelata.",
            "Stir 30 seconds in mixing glass. Strain into frozen coupe.",
            "Coppa cocktail", "Oliva o scorza limone",
            "Dirty Martini (olive brine), Vesper (gin + vodka + Lillet), Espresso Martini",
            "Dirty Martini (olive brine), Vesper (gin + vodka + Lillet), Espresso Martini"),
    },
    {
        "slug": "mixology-moderna",
        "cat": {"it": "Mixology", "en": "Mixology"},
        "img": "hospitality-cocktail.jpg",
        "date": "2026-06-02",
        "read": {"it": "8 min", "en": "8 min"},
        "title": {"it": "Mixology moderna", "en": "Modern mixology"},
        "desc": {"it": "Tecniche avanzate, bilanciamento acido/dolce, infusi e pairing.", "en": "Advanced techniques, sweet/sour balance, infusions and food pairing."},
        "body": {
            "it": """<h2>Tecniche avanzate</h2><ul><li>Fat washing e clarificazione</li><li>Sous-vide per sciroppi</li><li>Carbonazione e nitro</li><li>Rotovap per distillati custom</li></ul>
<h2>Bilanciamento acido/dolce</h2><p>Regola 2:1:1 (spirito:acido:dolce) come base, poi aggiusta al palato. Il lime fresco è non negoziabile.</p>
<h2>Aromi e bitter</h2><p>Bitter artigianali, tincture, spray assenzio. Un dash può trasformare un drink.</p>
<h2>Infusi e sciroppi</h2><p>Sciroppi homemade: ginger, rosemary, honey. Infusi 24–48h max per evitare amarezza.</p>
<h2>Pairing con cibo</h2><p>Complementare o contrastare: Negroni + salumi, Margarita + tacos, Manhattan + steak.</p>""",
            "en": """<h2>Advanced techniques</h2><ul><li>Fat washing and clarification</li><li>Sous-vide for syrups</li><li>Carbonation and nitro</li><li>Rotovap for custom distillates</li></ul>
<h2>Sweet/sour balance</h2><p>2:1:1 rule (spirit:sour:sweet) as base, then adjust to taste. Fresh lime is non-negotiable.</p>
<h2>Aromas and bitters</h2><p>Artisan bitters, tinctures, absinthe spray. One dash can transform a drink.</p>
<h2>Infusions and syrups</h2><p>Homemade syrups: ginger, rosemary, honey. Infusions 24–48h max to avoid bitterness.</p>
<h2>Food pairing</h2><p>Complement or contrast: Negroni + charcuterie, Margarita + tacos, Manhattan + steak.</p>""",
        },
    },
    {
        "slug": "storia-resort-vip",
        "cat": {"it": "Stories", "en": "Stories"},
        "img": "hospitality-bar.jpg",
        "date": "2026-05-30",
        "read": {"it": "6 min", "en": "6 min"},
        "title": {"it": "Vita nei resort 5 stelle", "en": "Life in 5-star resorts"},
        "desc": {"it": "Dietro le quinte dell'ospitalità di lusso.", "en": "Behind the scenes of luxury hospitality."},
        "body": {
            "it": """<p>Nei resort 5 stelle ogni dettaglio è coreografato: dal piegamento del tovagliolo al timing del servizio cocktail in piscina.</p>
<p>Ho imparato che il lusso non è opulenza — è <strong>anticipazione</strong>. Leggere la sala, capire cosa vuole il cliente prima che lo chieda.</p>""",
            "en": """<p>In 5-star resorts every detail is choreographed: from napkin folding to poolside cocktail timing.</p>
<p>I learned that luxury is not opulence — it is <strong>anticipation</strong>. Reading the room, understanding what the guest wants before they ask.</p>""",
        },
    },
    {
        "slug": "eventi-corporate",
        "cat": {"it": "Stories", "en": "Stories"},
        "img": "hospitality-blog-hero.jpg",
        "date": "2026-05-28",
        "read": {"it": "5 min", "en": "5 min"},
        "title": {"it": "Eventi corporate e clientela VIP", "en": "Corporate events and VIP clientele"},
        "desc": {"it": "Servizio impeccabile sotto pressione massima.", "en": "Impeccable service under maximum pressure."},
        "body": {
            "it": """<p>Eventi corporate in UK: 500+ ospiti, open bar, deadline strette. La calma è la competenza più rara.</p>
<p>Clienti VIP richiedono discrezione, memoria (il loro drink preferito) e velocità senza invadere lo spazio personale.</p>""",
            "en": """<p>Corporate events in the UK: 500+ guests, open bar, tight deadlines. Calm is the rarest skill.</p>
<p>VIP clients require discretion, memory (their favourite drink) and speed without invading personal space.</p>""",
        },
    },
    {
        "slug": "cultura-servizio",
        "cat": {"it": "Stories", "en": "Stories"},
        "img": "hospitality-bar.jpg",
        "date": "2026-05-25",
        "read": {"it": "6 min", "en": "6 min"},
        "title": {"it": "Cultura del servizio: UK, Sudafrica, Italia", "en": "Service culture: UK, South Africa, Italy"},
        "desc": {"it": "Tre continenti, tre approcci al servizio.", "en": "Three continents, three approaches to service."},
        "body": {
            "it": """<p><strong>UK:</strong> precisione, velocità, standard rigidi. Il cliente non sbaglia mai — sbaglia il sistema.</p>
<p><strong>Sudafrica:</strong> calore umano, adattamento, resilienza con risorse limitate.</p>
<p><strong>Italia:</strong> relazione, flessibilità, attenzione al dettaglio personale.</p>
<p>Oggi unisco tutti e tre gli approcci nel customer service e nelle operations.</p>""",
            "en": """<p><strong>UK:</strong> precision, speed, rigid standards. The customer is never wrong — the system is.</p>
<p><strong>South Africa:</strong> human warmth, adaptation, resilience with limited resources.</p>
<p><strong>Italy:</strong> relationship, flexibility, personal attention to detail.</p>
<p>Today I combine all three approaches in customer service and operations.</p>""",
        },
    },
]