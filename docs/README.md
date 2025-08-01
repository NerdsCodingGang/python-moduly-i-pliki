# 🚀 Nerds Coding Gang Python wakacyjny

Repozytorium kursu **„Python od podstaw”**, realizowanego w ramach letnich warsztatów Nerds Coding Gang.  
Materiały publikowane są jako strona internetowa zbudowana przy użyciu **GitHub Pages** i **Jekyll**.

---

## 🔧 Konfiguracja

- GitHub Pages – hostowanie strony
- Jekyll – konwersja Markdown na stronę
- GitHub Actions – automatyczne budowanie i publikacja (`.github/jekyll-gh-pages.yml`)
- Konfiguracja motywu: `_config.yml`
- Szczegóły motywu: `docs/THEME.md`

📘 [Dokumentacja Jekyll](https://jekyllrb.com/docs/pages)

---

## 📚 Struktura treści

Lekcje kursu znajdują się w katalogu `_pages/`.  
Każdy plik `.md` to osobny rozdział, np.:

```
_pages/
├── 01-python.md
├── 02-narzedzia.md
├── 03-konsola.md
...
```

> Zachowaj numerację (`01-`, `02-`, ...) żeby utrzymać właściwą kolejność.

---

## 🧾 Format plików `.md`

Każdy rozdział zaczyna się od nagłówka YAML:

```markdown
---
title: Why JS?
layout: page
author: Rita Łyczywek
date: 2025-07-01
cover: ../assets/cover.png
---
```

**Wymagane**: `title`, `layout`  
**Opcjonalne**: `author`, `date`, `cover`, `category`

---

## 🧪 Podgląd lokalny

Dla osób technicznych:

```bash
bundle install
bundle exec jekyll serve
```

Lokalnie dostępne pod `http://localhost:4000`.

---

## 🤝 Organizacja

Prowadzenie: **Rita Łyczywek**  
Organizacja: **Nerds Coding Gang**  

---

## 📄 Licencja

Creative Commons BY-NC-SA 4.0  
→ do użytku niekomercyjnego, z podaniem autora, na tych samych zasadach.
