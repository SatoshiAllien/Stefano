/**
 * Stefano Ciancimino — Professional assistant (IT / EN)
 * Knowledge base: fraud prevention, blockchain, AI, security, consulting
 */

(function () {
  'use strict';

  function assetBase() {
    var parts = window.location.pathname.split('/').filter(Boolean);
    var langIdx = -1;
    for (var i = 0; i < parts.length; i++) {
      if (parts[i] === 'it' || parts[i] === 'en') { langIdx = i; break; }
    }
    var depth = langIdx >= 0 ? Math.max(0, parts.length - langIdx - 2) : 0;
    return (depth > 0 ? '../'.repeat(depth + 1) : '../') + 'img/';
  }

  function getPageLang() {
    var pathParts = window.location.pathname.split('/').filter(Boolean);
    var langSegment = null;
    for (var i = 0; i < pathParts.length; i++) {
      if (pathParts[i] === 'it' || pathParts[i] === 'en') {
        langSegment = pathParts[i];
        break;
      }
    }
    return document.body.getAttribute('data-lang') || langSegment || 'it';
  }

  const LOGO = assetBase() + 'logo-sc-hd.png?v=20260622-brand';
  const LINKEDIN = 'https://www.linkedin.com/in/55555555-b5947439';
  const X_ACCOUNT = 'https://x.com/TheRiser100x';
  const CRYPTO_SITE = 'https://satoshiallien.github.io/cryptoitaliafacile/index.html';
  const EMAIL = 'krown82@outlook.com';

  const CONTENT = {
    it: {
      bot: {
        name: 'Assistente Stefano',
        tagline: 'Fraud & Risk · Blockchain · AI · Consulenza',
        welcome:
          'Benvenuto. Sono l\'assistente virtuale di Stefano Davide Ciancimino — Fraud & Risk Analyst, Blockchain Researcher e AI Specialist.\n\n' +
          'Posso fornire informazioni su competenze professionali, esperienza, servizi di consulenza e recapiti. Seleziona un argomento qui sotto o scrivi la tua domanda.',
        placeholder: 'Es. esperienza antifrode, servizi di consulenza…',
        typing: 'Elaborazione in corso…',
        launcher: 'Assistente Stefano',
        close: 'Chiudi',
        send: 'Invia'
      },
      defaultResponse:
        'Al momento non dispongo di informazioni specifiche su questo argomento.\n\n' +
        'Ti invito a richiedere dettagli su: profilo professionale, antifrode, blockchain, AI, sicurezza, consulenza o contatti.\n\n' +
        'Per comunicazioni dirette: ' + EMAIL,
      suggestions: [
        'Profilo professionale',
        'Esperienza antifrode',
        'Blockchain & DeFi',
        'Servizi di consulenza',
        'Contatti'
      ],
      knowledgeBase: [
        {
          keywords: ['chi sei', 'chi e', 'presentati', 'profilo', 'profilo professionale', 'stefano', 'ciancimino', 'about'],
          response:
            'Stefano Davide Ciancimino è Fraud & Risk Analyst, Blockchain Researcher e AI Specialist, con oltre 8 anni di esperienza in ambienti ad alta complessità operativa.\n\n' +
            'Il suo percorso combina analisi antifrode, ricerca blockchain e applicazione dell\'intelligenza artificiale a processi di risk e operations, con un approccio metodico orientato a risultati misurabili.'
        },
        {
          keywords: ['antifrode', 'frode', 'fraud', 'truffa', 'schemi', 'perdite', 'mitigazione'],
          response:
            'In ambito antifrode, Stefano si occupa di monitoraggio transazioni, rilevazione di schemi fraudolenti, investigazioni su account ad alto rischio e mitigazione delle perdite.\n\n' +
            'Presso PayPal ha contribuito alla prevenzione di frodi per oltre 100.000 USD e all\'ottimizzazione dei flussi operativi antifrode, con focus su efficacia, accuratezza e riduzione dei falsi positivi.'
        },
        {
          keywords: ['risk', 'rischio', 'seller risk', 'buyer fraud', 'operations'],
          response:
            'Come Senior Seller Risk Operations presso PayPal (2018–2022), Stefano ha gestito investigazioni su profili ad alto rischio, formazione di nuovi analisti e coordinamento cross-funzionale.\n\n' +
            'Le sue competenze includono valutazione del rischio, monitoraggio transazionale e implementazione di misure per la riduzione delle perdite operative.'
        },
        {
          keywords: ['blockchain', 'crypto', 'cripto', 'bitcoin', 'ethereum', 'defi', 'cefi', 'nft', 'protocolli'],
          response:
            'Dal 2017 Stefano opera come Blockchain Researcher, con attività di analisi su protocolli, ecosistemi DeFi/CeFi e dinamiche NFT.\n\n' +
            'Ha condotto formazione interna su blockchain in contesto corporate e supporta oggi attività di ricerca, valutazione dei rischi e divulgazione educativa nel settore crypto.'
        },
        {
          keywords: ['ai', 'intelligenza artificiale', 'ollama', 'llama', 'prompt', 'automazione', 'agenti', 'wsl'],
          response:
            'Stefano applica l\'intelligenza artificiale ad analisi dati, prompt engineering e automazione di processi operativi.\n\n' +
            'Sperimenta agenti AI in ambiente locale (Ollama, WSL, Llama) e offre consulenza sull\'integrazione dell\'AI nei workflow di risk, operations e content strategy.'
        },
        {
          keywords: ['sicurezza', 'security', 'investigazione', 'analisi', 'monitoraggio'],
          response:
            'Le competenze in sicurezza operativa di Stefano comprendono investigazione avanzata, analisi di pattern anomali, problem solving strutturato e monitoraggio in tempo reale.\n\n' +
            'Il suo approccio privilegia la riduzione del rischio, la continuità operativa e il miglioramento progressivo dei processi di controllo.'
        },
        {
          keywords: ['paypal', 'esperienza', 'lavoro', 'carriera', 'cv'],
          response:
            'Il percorso professionale principale di Stefano include PayPal (2013–2022) come Buyer Fraud Prevention Analyst e Senior Seller Risk Operations.\n\n' +
            'In precedenza ha lavorato in customer service (National Pen), technical support (SYKES) e nel settore hospitality premium, sviluppando oltre 8 anni di esperienza in analisi, risk management e operations.'
        },
        {
          keywords: ['consulenza', 'servizi', 'servizi di consulenza', 'collaborare', 'assumi', 'lavorare', 'preventivo'],
          response:
            'Stefano offre servizi di consulenza su:\n' +
            '• Analisi antifrode e risk management\n' +
            '• Ricerca e valutazione ecosistemi blockchain\n' +
            '• Integrazione AI nei processi operativi\n' +
            '• Formazione team e audit di processo\n\n' +
            'Per una valutazione preliminare è possibile visitare la pagina Consulenza o scrivere a ' + EMAIL + '.'
        },
        {
          keywords: ['contatti', 'contattare', 'email', 'telefono', 'linkedin', 'scrivere', 'twitter', 'x.com'],
          response:
            'Recapiti professionali di Stefano Ciancimino:\n' +
            '• Email: ' + EMAIL + '\n' +
            '• Telefono: +39 377 350 3049\n' +
            '• LinkedIn: ' + LINKEDIN + '\n' +
            '• X: ' + X_ACCOUNT + '\n\n' +
            'Tempo medio di risposta: entro 24 ore lavorative.'
        },
        {
          keywords: ['cryptoitalia', 'crypto italia', 'crypto facile', 'satoshi', 'little satoshi', 'blogger', 'blog crypto', 'divulgatore'],
          response:
            'Stefano è fondatore di Crypto Italia Facile (The Little Satoshi News), progetto educativo attivo dal 2015 dedicato a Bitcoin, blockchain e Web3 in linguaggio accessibile.\n\n' +
            'Portale: ' + CRYPTO_SITE + '\n\n' +
            'Contenuti disponibili: guide, news, sicurezza crypto, Cardano e assistente AI Satoshi.'
        },
        {
          keywords: ['rapidresponse', 'rapid response', 'x account', 'profilo x'],
          response:
            'Per aggiornamenti professionali e contenuti su crypto e analisi di settore, Stefano è presente su X:\n' + X_ACCOUNT
        },
        {
          keywords: ['lingue', 'inglese', 'italiano', 'language'],
          response:
            'Stefano è madrelingua italiano e possiede un livello C1 in inglese, con esperienza consolidata in contesti internazionali (PayPal) e progetti cross-border in fintech e blockchain.'
        },
        {
          keywords: ['tecnologia', 'linux', 'macos', 'citrix', 'troubleshooting', 'rete', 'hardware'],
          response:
            'Dal punto di vista tecnico, Stefano lavora con macOS, Linux/Ubuntu e Citrix, con competenze in troubleshooting di rete, hardware e software.\n\n' +
            'Il background in technical support (SYKES) include gestione SLA e risoluzione strutturata di incidenti complessi.'
        },
        {
          keywords: ['customer', 'clienti', 'service', 'operazioni', 'empatia'],
          response:
            'Stefano unisce rigore analitico e capacità relazionale: gestione di casi complessi, comunicazione chiara e orientamento alla soluzione.\n\n' +
            'Questo equilibrio è stato consolidato in contesti ad alto impatto come PayPal e nel settore hospitality premium.'
        },
        {
          keywords: ['blog', 'articoli', 'contenuti', 'educativi'],
          response:
            'Il blog professionale affronta tematiche di antifrode, sicurezza, blockchain, AI e risk management, con contenuti pensati per professionisti fintech e tech.\n\n' +
            'Per gli ultimi articoli, visita la sezione Blog del portfolio.'
        },
        {
          keywords: ['portfolio', 'progetti', 'demo', 'presentazioni'],
          response:
            'Il portfolio include articoli specialistici, analisi di ecosistemi crypto, demo AI con agenti locali e materiali formativi.\n\n' +
            'Per una panoramica completa dei progetti, visita la pagina Portfolio.'
        },
        {
          keywords: ['ciao', 'salve', 'buongiorno', 'buonasera', 'hey', 'hello', 'hi'],
          response:
            'Buongiorno. Sono a disposizione per fornire informazioni su competenze, esperienza e servizi di Stefano Ciancimino in ambito antifrode, blockchain, AI e sicurezza operativa.\n\n' +
            'Come posso assisterti?'
        },
        {
          keywords: ['grazie', 'thanks', 'perfetto', 'ok'],
          response:
            'Con piacere. Resto a disposizione per ulteriori chiarimenti.\n\n' +
            'Per un contatto diretto con Stefano: ' + EMAIL + ' oppure LinkedIn.'
        }
      ]
    },
    en: {
      bot: {
        name: 'Stefano Assistant',
        tagline: 'Fraud & Risk · Blockchain · AI · Consulting',
        welcome:
          'Welcome. I am the virtual assistant for Stefano Davide Ciancimino — Fraud & Risk Analyst, Blockchain Researcher and AI Specialist.\n\n' +
          'I can provide information on professional skills, experience, consulting services and contact details. Select a topic below or type your question.',
        placeholder: 'E.g. fraud prevention experience, consulting services…',
        typing: 'Processing…',
        launcher: 'Stefano Assistant',
        close: 'Close',
        send: 'Send'
      },
      defaultResponse:
        'I do not have specific information on this topic at the moment.\n\n' +
        'Please ask about: professional profile, fraud prevention, blockchain, AI, security, consulting or contact details.\n\n' +
        'For direct enquiries: ' + EMAIL,
      suggestions: [
        'Professional profile',
        'Fraud prevention experience',
        'Blockchain & DeFi',
        'Consulting services',
        'Contact details'
      ],
      knowledgeBase: [
        {
          keywords: ['who are you', 'who is', 'introduce', 'profile', 'professional profile', 'stefano', 'ciancimino', 'about', 'tell me about'],
          response:
            'Stefano Davide Ciancimino is a Fraud & Risk Analyst, Blockchain Researcher and AI Specialist with over 8 years of experience in high-complexity operational environments.\n\n' +
            'His career combines fraud analysis, blockchain research and the application of artificial intelligence to risk and operations processes, with a methodical, results-driven approach.'
        },
        {
          keywords: ['antifraud', 'fraud', 'scam', 'schemes', 'losses', 'mitigation', 'fraud prevention'],
          response:
            'In fraud prevention, Stefano focuses on transaction monitoring, detection of fraudulent schemes, high-risk account investigations and loss mitigation.\n\n' +
            'At PayPal he contributed to preventing fraud worth over USD 100,000 and optimising antifraud operational workflows, with a focus on effectiveness, accuracy and reducing false positives.'
        },
        {
          keywords: ['risk', 'seller risk', 'buyer fraud', 'operations', 'risk management'],
          response:
            'As Senior Seller Risk Operations at PayPal (2018–2022), Stefano managed high-risk profile investigations, trained new analysts and coordinated cross-functional teams.\n\n' +
            'His skills include risk assessment, transaction monitoring and implementing measures to reduce operational losses.'
        },
        {
          keywords: ['blockchain', 'crypto', 'cryptocurrency', 'bitcoin', 'ethereum', 'defi', 'cefi', 'nft', 'protocols', 'web3'],
          response:
            'Since 2017 Stefano has worked as a Blockchain Researcher, analysing protocols, DeFi/CeFi ecosystems and NFT market dynamics.\n\n' +
            'He has delivered internal blockchain training in corporate settings and now supports research, risk assessment and educational outreach in the crypto sector.'
        },
        {
          keywords: ['ai', 'artificial intelligence', 'ollama', 'llama', 'prompt', 'automation', 'agents', 'wsl', 'machine learning'],
          response:
            'Stefano applies artificial intelligence to data analysis, prompt engineering and operational process automation.\n\n' +
            'He experiments with local AI agents (Ollama, WSL, Llama) and offers consulting on integrating AI into risk, operations and content strategy workflows.'
        },
        {
          keywords: ['security', 'investigation', 'analysis', 'monitoring', 'operational security'],
          response:
            'Stefano\'s operational security skills include advanced investigation, anomalous pattern analysis, structured problem solving and real-time monitoring.\n\n' +
            'His approach prioritises risk reduction, operational continuity and continuous improvement of control processes.'
        },
        {
          keywords: ['paypal', 'experience', 'work', 'career', 'cv', 'resume', 'background'],
          response:
            'Stefano\'s main professional background includes PayPal (2013–2022) as Buyer Fraud Prevention Analyst and Senior Seller Risk Operations.\n\n' +
            'Previously he worked in customer service (National Pen), technical support (SYKES) and premium hospitality, building over 8 years of experience in analysis, risk management and operations.'
        },
        {
          keywords: ['consulting', 'services', 'consultancy', 'collaborate', 'hire', 'work together', 'quote', 'engagement'],
          response:
            'Stefano offers consulting services in:\n' +
            '• Fraud analysis and risk management\n' +
            '• Blockchain ecosystem research and assessment\n' +
            '• AI integration into operational processes\n' +
            '• Team training and process audits\n\n' +
            'For an initial assessment, visit the Consulting page or email ' + EMAIL + '.'
        },
        {
          keywords: ['contact', 'contacts', 'email', 'phone', 'linkedin', 'reach', 'twitter', 'x.com', 'get in touch'],
          response:
            'Stefano Ciancimino — professional contact details:\n' +
            '• Email: ' + EMAIL + '\n' +
            '• Phone: +39 377 350 3049\n' +
            '• LinkedIn: ' + LINKEDIN + '\n' +
            '• X: ' + X_ACCOUNT + '\n\n' +
            'Average response time: within 24 business hours.'
        },
        {
          keywords: ['cryptoitalia', 'crypto italia', 'crypto facile', 'satoshi', 'little satoshi', 'blogger', 'crypto blog', 'educator'],
          response:
            'Stefano founded Crypto Italia Facile (The Little Satoshi News), an educational project active since 2015 covering Bitcoin, blockchain and Web3 in accessible language.\n\n' +
            'Website: ' + CRYPTO_SITE + '\n\n' +
            'Content includes guides, news, crypto security, Cardano and the Satoshi AI assistant.'
        },
        {
          keywords: ['rapidresponse', 'rapid response', 'x account', 'x profile'],
          response:
            'For professional updates and content on crypto and sector analysis, Stefano is on X:\n' + X_ACCOUNT
        },
        {
          keywords: ['languages', 'english', 'italian', 'language', 'bilingual'],
          response:
            'Stefano is a native Italian speaker with C1-level English, with extensive experience in international environments (PayPal) and cross-border fintech and blockchain projects.'
        },
        {
          keywords: ['technology', 'linux', 'macos', 'citrix', 'troubleshooting', 'network', 'hardware', 'tech'],
          response:
            'Technically, Stefano works with macOS, Linux/Ubuntu and Citrix, with skills in network, hardware and software troubleshooting.\n\n' +
            'His technical support background (SYKES) includes SLA management and structured resolution of complex incidents.'
        },
        {
          keywords: ['customer', 'clients', 'service', 'operations', 'empathy', 'client relations'],
          response:
            'Stefano combines analytical rigour with strong interpersonal skills: managing complex cases, clear communication and solution-oriented support.\n\n' +
            'This balance was honed in high-impact environments such as PayPal and premium hospitality.'
        },
        {
          keywords: ['blog', 'articles', 'content', 'educational', 'posts'],
          response:
            'The professional blog covers fraud prevention, security, blockchain, AI and risk management, with content aimed at fintech and tech professionals.\n\n' +
            'For the latest articles, visit the Blog section of the portfolio.'
        },
        {
          keywords: ['portfolio', 'projects', 'demo', 'presentations', 'showcase'],
          response:
            'The portfolio includes specialist articles, crypto ecosystem analysis, AI demos with local agents and training materials.\n\n' +
            'For a full overview of projects, visit the Portfolio page.'
        },
        {
          keywords: ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening', 'greetings'],
          response:
            'Hello. I am here to provide information on Stefano Ciancimino\'s skills, experience and services in fraud prevention, blockchain, AI and operational security.\n\n' +
            'How may I assist you?'
        },
        {
          keywords: ['thanks', 'thank you', 'cheers', 'perfect', 'great', 'ok', 'okay'],
          response:
            'You\'re welcome. I remain available for any further questions.\n\n' +
            'To contact Stefano directly: ' + EMAIL + ' or LinkedIn.'
        }
      ]
    }
  };

  function normalize(text) {
    return text
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .trim();
  }

  function findResponse(query, knowledgeBase, defaultResponse) {
    const normalized = normalize(query);

    let bestMatch = null;
    let bestScore = 0;

    knowledgeBase.forEach(function (entry) {
      let score = 0;
      entry.keywords.forEach(function (keyword) {
        if (normalized.includes(normalize(keyword))) {
          score += keyword.split(' ').length;
        }
      });
      if (score > bestScore) {
        bestScore = score;
        bestMatch = entry;
      }
    });

    return bestMatch ? bestMatch.response : defaultResponse;
  }

  function createChatbot() {
    const lang = getPageLang() === 'en' ? 'en' : 'it';
    const cfg = CONTENT[lang];
    const BOT = cfg.bot;

    const chatbot = document.createElement('div');
    chatbot.className = 'chatbot';
    chatbot.setAttribute('data-lang', lang);
    chatbot.innerHTML =
      '<div class="chatbot__launcher">' +
      '<span class="chatbot__launcher-label">' + BOT.launcher + '</span>' +
      '<button class="chatbot__toggle" aria-label="' + BOT.name + '" title="' + BOT.name + '">' +
      '<img src="' + LOGO + '" alt="' + BOT.name + '" class="chatbot__toggle-logo" width="44" height="44" loading="eager" decoding="async">' +
      '</button></div>' +
      '<div class="chatbot__panel">' +
      '<div class="chatbot__header">' +
      '<div class="chatbot__avatar"><img src="' + LOGO + '" alt="' + BOT.name + '" class="chatbot__avatar-logo" width="36" height="36" loading="eager" decoding="async"></div>' +
      '<div class="chatbot__header-info"><strong>' + BOT.name + '</strong><span>' + BOT.tagline + '</span></div>' +
      '<button class="chatbot__close" aria-label="' + BOT.close + '"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg></button>' +
      '</div>' +
      '<div class="chatbot__messages"></div>' +
      '<div class="chatbot__typing">' + BOT.typing + '</div>' +
      '<div class="chatbot__suggestions"></div>' +
      '<div class="chatbot__input-area">' +
      '<input type="text" class="chatbot__input" placeholder="' + BOT.placeholder + '" autocomplete="off">' +
      '<button class="chatbot__send" aria-label="' + BOT.send + '"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg></button>' +
      '</div></div>';

    document.body.appendChild(chatbot);

    const toggle = chatbot.querySelector('.chatbot__toggle');
    const close = chatbot.querySelector('.chatbot__close');
    const messages = chatbot.querySelector('.chatbot__messages');
    const typing = chatbot.querySelector('.chatbot__typing');
    const input = chatbot.querySelector('.chatbot__input');
    const send = chatbot.querySelector('.chatbot__send');
    const suggestionsEl = chatbot.querySelector('.chatbot__suggestions');

    function addMessage(text, type) {
      const wrap = document.createElement('div');
      wrap.className = 'chatbot__message-row chatbot__message-row--' + type;

      if (type === 'bot') {
        const avatar = document.createElement('img');
        avatar.src = LOGO;
        avatar.alt = '';
        avatar.className = 'chatbot__msg-logo';
        avatar.width = 24;
        avatar.height = 24;
        wrap.appendChild(avatar);
      }

      const msg = document.createElement('div');
      msg.className = 'chatbot__message chatbot__message--' + type;
      if (type === 'bot' && text === BOT.welcome) {
        msg.classList.add('chatbot__message--welcome');
      }
      msg.textContent = text;
      wrap.appendChild(msg);
      messages.appendChild(wrap);
      messages.scrollTop = messages.scrollHeight;
    }

    function showTyping() {
      typing.classList.add('chatbot__typing--visible');
      messages.scrollTop = messages.scrollHeight;
    }

    function hideTyping() {
      typing.classList.remove('chatbot__typing--visible');
    }

    function respond(query) {
      showTyping();
      setTimeout(function () {
        hideTyping();
        addMessage(findResponse(query, cfg.knowledgeBase, cfg.defaultResponse), 'bot');
      }, 600 + Math.random() * 400);
    }

    function handleSend() {
      const text = input.value.trim();
      if (!text) return;
      addMessage(text, 'user');
      input.value = '';
      respond(text);
    }

    toggle.addEventListener('click', function () {
      chatbot.classList.toggle('chatbot--open');
      if (chatbot.classList.contains('chatbot--open') && messages.children.length === 0) {
        addMessage(BOT.welcome, 'bot');
      }
    });

    close.addEventListener('click', function () {
      chatbot.classList.remove('chatbot--open');
    });

    send.addEventListener('click', handleSend);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') handleSend();
    });

    cfg.suggestions.forEach(function (text) {
      const btn = document.createElement('button');
      btn.className = 'chatbot__suggestion';
      btn.textContent = text;
      btn.addEventListener('click', function () {
        addMessage(text, 'user');
        respond(text);
      });
      suggestionsEl.appendChild(btn);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createChatbot);
  } else {
    createChatbot();
  }
})();