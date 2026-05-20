<div align="center">

# 🔐 VAULT
### Privacy-first Personal Finance for India

**No cloud · No login · No ads · No tracking**  
Your money data lives only on your phone. Always.

[![PWA](https://img.shields.io/badge/PWA-Ready-4a7a58?style=flat-square&logo=pwa)](https://web.dev/progressive-web-apps/)
[![Offline](https://img.shields.io/badge/Works-Offline-3a6898?style=flat-square)](.)
[![Zero Dependencies](https://img.shields.io/badge/Framework-None-c87030?style=flat-square)](.)
[![Single File](https://img.shields.io/badge/Build-Single%20HTML-7a68c8?style=flat-square)](.)

[**→ Open VAULT**](https://yourusername.github.io/vault/)

</div>

---

## Why VAULT?

Every finance app asks you to create an account.  
That account lives on someone's server.  
That server can be hacked, sold, or shut down.

VAULT is different — it runs entirely in your browser.  
No server. No account. No one else can see your data.

---

## Install in 30 seconds

**Android (Chrome)**
1. Open the link in Chrome
2. Tap the banner → **"Add to Home Screen"**
3. Done — opens like a real app

**iPhone / iPad (Safari)**
1. Open the link in Safari
2. Tap the **Share** button ⬆️
3. Tap **"Add to Home Screen"** → **Add**
4. Done — opens like a real app

> Works on any device with a modern browser. No app store needed.

---

## What it does

| Feature | Details |
|---|---|
| ⚡ Quick Add | Type naturally — `"500 zomato"` auto-fills category + method |
| 📊 Dashboard | Monthly balance, budget bar, smart spending insights |
| 🗂 Categories | 20+ built-in + add your own custom categories |
| 💳 UPI / Cash / Card | Track payment method per transaction |
| 📈 Expense Trends | 6-month chart with category breakdown |
| 🔍 Search | Find any transaction instantly |
| 🔒 PIN Lock | 4-digit lock screen to protect your data |
| 🤝 Settle Up | Track who owes you / who you owe |
| 🎯 Goals | Save towards specific targets |
| 📱 Bank SMS Parser | Paste any bank SMS — auto-extracts amount, merchant, type |
| 💾 Backup & Restore | Export `.vault` file, restore anytime |
| 🌙 Works Offline | No internet needed after first load |

---

## Privacy — the full picture

| Question | Answer |
|---|---|
| Does VAULT collect any data? | No. Zero. |
| Does it send anything to a server? | No server exists. |
| Does it use analytics or tracking? | No. |
| Where is my data stored? | Your phone only (browser localStorage) |
| What happens if I clear browser data? | Use the backup feature to save a `.vault` file first |
| Is there a login? | No. Never. |

---

## Tech — built with nothing

```
HTML  +  CSS  +  Vanilla JavaScript
No React. No Vue. No Node. No build tools. No npm. No backend.
One file. That's it.
```

This is a deliberate choice. Less code = less attack surface = less to break.  
The entire app is a single `index.html` file (~250 KB).

---

## For developers

The public file (`index.html`) is obfuscated to protect the product logic.  
The architecture is:

```
localStorage  ←→  Vanilla JS engine  ←→  Single-file HTML/CSS UI
                        ↕
                 Service Worker (offline cache)
                        ↕
                  IndexedDB (encrypted txs)
```

All data is encrypted at rest using the Web Crypto API.  
The passphrase (6-word phrase shown on first launch) is the encryption key — it never leaves the device.

---

## Roadmap

- [ ] EMI tracker
- [ ] Recurring transactions
- [ ] Multiple accounts (wallet, bank, cash)
- [ ] CSV export
- [ ] Play Store (TWA via PWABuilder)
- [ ] Dark mode

---

<div align="center">

Built in India 🇮🇳 · For people who value privacy  
Made with zero dependencies and a lot of care

</div>
