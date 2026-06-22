/**
 * Stefano Ciancimino — Parla con Stefano
 * Knowledge base: antifrode, blockchain, AI, sicurezza
 */

(function () {
  'use strict';

  const LOGO = 'img/logo-sc-hd.png';
  const LINKEDIN = 'https://www.linkedin.com/in/55555555-b5947439';
  const X_ACCOUNT = 'https://x.com/TheRiser100x';
  const CRYPTO_SITE = 'https://satoshiallien.github.io/cryptoitaliafacile/index.html';
  const EMAIL = 'krown82@outlook.com';

  const knowledgeBase = [
    {
      keywords: ['chi sei', 'chi e', 'presentati', 'profilo', 'stefano', 'ciancimino', 'about'],
      response: 'Sono l\'assistente di Stefano Davide Ciancimino — Fraud & Risk Analyst, Blockchain Researcher e AI Specialist con oltre 8 anni di esperienza. Ha lavorato presso PayPal in antifrode e risk operations, e continua la ricerca su blockchain e automazione AI.'
    },
    {
      keywords: ['antifrode', 'frode', 'fraud', 'truffa', 'schemi', 'perdite', 'mitigazione'],
      response: 'Stefano ha esperienza diretta in analisi antifrode: monitoraggio transazioni, identificazione schemi fraudolenti, investigazioni su account ad alto rischio e mitigazione perdite. Presso PayPal ha contribuito alla prevenzione frodi da oltre 100.000 USD e all\'ottimizzazione dei flussi antifrode.'
    },
    {
      keywords: ['risk', 'rischio', 'seller risk', 'buyer fraud', 'operations'],
      response: 'Come Senior Seller Risk Operations presso PayPal (2018–2022), Stefano gestiva investigazioni su account ad alto rischio, coaching di nuovi colleghi e supporto cross-functional. La sua expertise copre valutazione del rischio, monitoraggio transazioni e riduzione perdite operative.'
    },
    {
      keywords: ['blockchain', 'crypto', 'cripto', 'bitcoin', 'ethereum', 'defi', 'cefi', 'nft', 'protocolli'],
      response: 'Stefano è Blockchain Researcher dal 2017: analizza protocolli, ecosistemi DeFi/CeFi e NFT. Ha condotto formazione interna su blockchain presso PayPal e investe attivamente nel settore crypto. Può supportare su analisi ecosistemi, ricerca protocolli e valutazione rischi crypto.'
    },
    {
      keywords: ['ai', 'intelligenza artificiale', 'ollama', 'llama', 'prompt', 'automazione', 'agenti', 'wsl'],
      response: 'Stefano utilizza AI avanzata per analisi dati, prompt engineering e automazione processi operativi. Sperimenta con agenti AI locali (Ollama, WSL, Llama) e crea contenuti educativi con AI. Offre consulenza su integrazione AI nei workflow di risk e operations.'
    },
    {
      keywords: ['sicurezza', 'security', 'investigazione', 'analisi', 'monitoraggio'],
      response: 'Le competenze di Stefano in sicurezza includono: investigazione avanzata, problem solving analitico, identificazione pattern fraudolenti e monitoraggio transazioni in tempo reale. Approccio metodico orientato a ridurre rischi e migliorare l\'efficienza operativa.'
    },
    {
      keywords: ['paypal', 'esperienza', 'lavoro', 'carriera', 'cv'],
      response: 'Esperienza principale: PayPal (2013–2022) come Buyer Fraud Prevention Analyst e Senior Seller Risk Operations. Prima: National Pen (Customer Service), SYKES (Technical Support) e settore Hospitality premium. Oltre 8 anni totali in analisi, risk e customer operations.'
    },
    {
      keywords: ['consulenza', 'servizi', 'collaborare', 'assumi', 'lavorare', 'preventivo'],
      response: 'Stefano offre consulenza su: analisi antifrode e risk management, ricerca blockchain, integrazione AI nei processi operativi, formazione team e audit processi. Visita la pagina Consulenza o contattalo a ' + EMAIL + ' per una sessione introduttiva.'
    },
    {
      keywords: ['contatti', 'contattare', 'email', 'telefono', 'linkedin', 'scrivere', 'twitter', 'x.com'],
      response: 'Puoi contattare Stefano:\n• Email: ' + EMAIL + '\n• Telefono: +39 377 350 3049\n• LinkedIn: ' + LINKEDIN + '\n• X: ' + X_ACCOUNT + '\n\nRisponde entro 24 ore lavorative.'
    },
    {
      keywords: ['cryptoitalia', 'crypto italia', 'crypto facile', 'satoshi', 'little satoshi', 'blogger', 'blog crypto', 'divulgatore'],
      response: 'Stefano è il creatore di Crypto Italia Facile (The Little Satoshi News) — portale educativo dove spiega Bitcoin, blockchain e Web3 in modo semplice dal 2015. Visita: ' + CRYPTO_SITE + '\n\nTrovi guide, news, sicurezza crypto, Cardano e l\'assistente AI Satoshi.'
    },
    {
      keywords: ['rapidresponse', 'rapid response', 'x account', 'profilo x'],
      response: 'Segui Stefano su X: ' + X_ACCOUNT + ' — aggiornamenti su crypto, analisi e contenuti da Crypto Italia Facile.'
    },
    {
      keywords: ['lingue', 'inglese', 'italiano', 'language'],
      response: 'Stefano parla Italiano (madrelingua) e Inglese (C1 fluente). Ideale per contesti internazionali come PayPal e progetti cross-border in blockchain e fintech.'
    },
    {
      keywords: ['tecnologia', 'linux', 'macos', 'citrix', 'troubleshooting', 'rete', 'hardware'],
      response: 'Competenze tecniche: macOS, Linux/Ubuntu, Citrix, troubleshooting rete/hardware/software. Background in technical support (SYKES) con gestione SLA e risoluzione problemi complessi.'
    },
    {
      keywords: ['customer', 'clienti', 'service', 'operazioni', 'empatia'],
      response: 'Stefano combina analisi tecnica con eccellente customer operations: gestione casi complessi, comunicazione chiara, empatia e orientamento alla soluzione. Esperienza in contesti ad alto impatto come PayPal e settore premium hospitality.'
    },
    {
      keywords: ['blog', 'articoli', 'contenuti', 'educativi'],
      response: 'Il blog professionale copre antifrode, sicurezza, blockchain, AI e risk management. Articoli educativi pensati per professionisti del settore fintech e tech. Visita la sezione Blog per gli ultimi contenuti.'
    },
    {
      keywords: ['portfolio', 'progetti', 'demo', 'presentazioni'],
      response: 'Nel portfolio trovi: articoli educativi su antifrode e blockchain, analisi ecosistemi crypto, demo AI con agenti locali e presentazioni formative. Visita la pagina Portfolio per esplorare i progetti.'
    },
    {
      keywords: ['ciao', 'salve', 'buongiorno', 'buonasera', 'hey', 'hello', 'hi'],
      response: 'Ciao! Benvenuto in Parla con Stefano. Posso aiutarti su antifrode, blockchain, AI, sicurezza e consulenze. Come posso assisterti?'
    },
    {
      keywords: ['grazie', 'thanks', 'perfetto', 'ok'],
      response: 'Prego! Se hai altre domande su competenze, servizi o come collaborare con Stefano, sono qui. Puoi anche contattarlo direttamente via email o LinkedIn.'
    }
  ];

  const defaultResponse =
    'Non ho trovato una risposta specifica. Prova a chiedere su: antifrode, blockchain, AI, sicurezza, consulenze o contatti. Oppure scrivi direttamente a ' + EMAIL;

  const suggestions = [
    'Esperienza antifrode',
    'Blockchain & DeFi',
    'AI & automazione',
    'Servizi consulenza',
    'Contatti'
  ];

  function normalize(text) {
    return text
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .trim();
  }

  function findResponse(query) {
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
    const chatbot = document.createElement('div');
    chatbot.className = 'chatbot';
    chatbot.innerHTML =
      '<div class="chatbot__launcher">' +
      '<span class="chatbot__launcher-label">Parla con Stefano</span>' +
      '<button class="chatbot__toggle" aria-label="Parla con Stefano" title="Parla con Stefano">' +
      '<img src="' + LOGO + '" alt="Parla con Stefano" class="chatbot__toggle-logo" width="44" height="44" loading="eager" decoding="async">' +
      '</button></div>' +
      '<div class="chatbot__panel">' +
      '<div class="chatbot__header">' +
      '<div class="chatbot__avatar"><img src="' + LOGO + '" alt="Parla con Stefano" class="chatbot__avatar-logo" width="36" height="36" loading="eager" decoding="async"></div>' +
      '<div class="chatbot__header-info"><strong>Parla con Stefano</strong><span>Antifrode · Blockchain · AI</span></div>' +
      '<button class="chatbot__close" aria-label="Chiudi"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg></button>' +
      '</div>' +
      '<div class="chatbot__messages"></div>' +
      '<div class="chatbot__typing">Sto scrivendo...</div>' +
      '<div class="chatbot__suggestions"></div>' +
      '<div class="chatbot__input-area">' +
      '<input type="text" class="chatbot__input" placeholder="Chiedi su antifrode, blockchain, AI..." autocomplete="off">' +
      '<button class="chatbot__send" aria-label="Invia"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg></button>' +
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
        addMessage(findResponse(query), 'bot');
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
        addMessage(
          'Ciao! Sono Parla con Stefano — l\'assistente di Stefano Ciancimino. Chiedimi di antifrode, blockchain, AI, sicurezza o consulenze.',
          'bot'
        );
      }
    });

    close.addEventListener('click', function () {
      chatbot.classList.remove('chatbot--open');
    });

    send.addEventListener('click', handleSend);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') handleSend();
    });

    suggestions.forEach(function (text) {
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