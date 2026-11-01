# 🚀 Launch Playbook: Deploying REPURPOSED to repurposed.tech

This turnkey deployment guide walks you through publishing the **Maker's Bible of Electromechanical Salvage & Repurposing** live to your new custom domain **`repurposed.tech`**.

---

## 📦 What We Prepared For You

Everything needed for a production deployment has been built into the **[`dist/`](file:///c:/Users/karma/Desktop/REPURPOSE/dist)** directory (`2.81 MB` total, 18 self-contained files):

| Path / File | Purpose |
| :--- | :--- |
| **[`dist/index.html`](file:///c:/Users/karma/Desktop/REPURPOSE/dist/index.html)** | Full interactive modern REPURPOSED web app: sleek dark cyber-engineering design, 3 core views (Compendium, 50 Blueprints, 88 Donor Scrap Atlas), Spotlight Command Palette (`Ctrl+K`), canonical `https://repurposed.tech`, SEO meta, and digital downloads modal. |
| **[`dist/ebook.html`](file:///c:/Users/karma/Desktop/REPURPOSE/dist/ebook.html)** | Standalone, print-ready reading room eBook with return navigation bar to `repurposed.tech`. |
| **`dist/downloads/`** | Direct download copies: `.epub` (295 KB), `.md` (672 KB), and quick matrix `salvage-compendium.md` (79 KB). |
| **`dist/favicon.svg` & `.ico`** | Modern glowing rotor/circuit favicon in scalable SVG + 32x32 binary ICO. |
| **`dist/assets/og-card.png` & `.svg`** | 1200x630 high-resolution modern social share preview card for Twitter, Discord, LinkedIn, and iMessage. |
| **`dist/manifest.json`** | Progressive Web App (PWA) manifest — allows mobile and desktop users to click "Install App" and run it offline like a native app. |
| **`dist/robots.txt` & `sitemap.xml`** | Pre-configured SEO crawling rules and sitemap for search engines. |
| **`dist/404.html`** | Modern glassmorphic 404 diagnostic screen with safe redirect back to home. |
| **`dist/CNAME`** | Pre-populated with `repurposed.tech` for instant custom domain matching. |
| **`dist/_headers` & `_redirects`** | Edge caching and URL rewrites (`/read`, `/bible.epub`, `/compendium`). |
| **`dist/vercel.json` & `firebase.json`** | Zero-config deployment manifests for Vercel and Firebase Hosting. |

---

## 🌐 Choose Your Hosting Method (All 100% Free)

Choose any of the four options below. **Option 1 (Cloudflare Pages)** is strongly recommended for speed, global edge caching, and automated HTTPS.

---

### Option 1: Cloudflare Pages (Recommended — 2 Minutes, Zero CLI)

Cloudflare Pages provides global edge CDN distribution, unlimited bandwidth, and automatic zero-maintenance SSL certificates.

1. Go to **[pages.cloudflare.com](https://pages.cloudflare.com/)** and sign in (or create a free account).
2. Click **Create a project** &rarr; select **Direct Upload**.
3. Name your project (e.g., `repurposed-tech`).
4. **Drag and drop** your entire **`dist/`** folder (`c:\Users\karma\Desktop\REPURPOSE\dist`) into the upload area.
5. Click **Deploy site**. Your site will be live immediately on a temporary `*.pages.dev` URL.
6. **Connect your domain `repurposed.tech`:**
   - On the project page, click the **Custom domains** tab.
   - Click **Set up a custom domain**.
   - Type **`repurposed.tech`** and click **Continue**.
   - If your domain is registered on Cloudflare, it connects automatically with one click.
   - If registered elsewhere (Namecheap, GoDaddy, Porkbun, Google/Squarespace), Cloudflare will show you the CNAME or Nameserver records to copy (see DNS section below).
   - Also add **`www.repurposed.tech`** as a second custom domain.

---

### Option 2: Vercel (1-Command CLI or Web Upload)

#### Method A: Via Command Line (Fastest)
Open PowerShell in the project directory and run:
```powershell
cd c:\Users\karma\Desktop\REPURPOSE\dist
npx vercel --prod
```
- When prompted:
  - *Set up and deploy?* &rarr; **y**
  - *Which scope?* &rarr; Select your account
  - *Link to existing project?* &rarr; **n**
  - *Project name?* &rarr; `repurposed-tech`
  - *In which directory is your code located?* &rarr; `.` (hit Enter)
- Once deployed, go to the Vercel dashboard:
  - Project Settings &rarr; **Domains** &rarr; Add `repurposed.tech`.

#### Method B: Web UI
1. Go to **[vercel.com/new](https://vercel.com/new)**.
2. Drag and drop the **`dist`** folder.
3. Once deployed, add `repurposed.tech` under Project Settings &rarr; **Domains**.

---

### Option 3: Netlify (Drag & Drop)

1. Go to **[app.netlify.com/drop](https://app.netlify.com/drop)**.
2. Drag and drop the **`dist`** folder into the circle.
3. Once deployed:
   - Go to **Site Configuration** &rarr; **Domain Management**.
   - Click **Add custom domain** and enter `repurposed.tech`.
   - Netlify will provision a free Let's Encrypt SSL certificate within minutes.

---

### Option 4: Firebase Hosting

1. Open PowerShell and install the Firebase CLI (if not already installed):
   ```powershell
   npm install -g firebase-tools
   ```
2. Log in and initialize:
   ```powershell
   firebase login
   firebase init hosting
   ```
   - When asked for public directory, enter: **`dist`**
   - Configure as single-page app? &rarr; **No**
   - Overwrite existing files? &rarr; **No**
3. Deploy:
   ```powershell
   firebase deploy --only hosting
   ```
4. Connect Domain:
   - In the **[Firebase Console](https://console.firebase.google.com/)**, select your project &rarr; **Hosting** &rarr; **Add Custom Domain** &rarr; enter `repurposed.tech`.

---

## 📡 DNS Configuration Table (For Your Domain Registrar)

Log into the registrar where you bought `repurposed.tech` (e.g., **Namecheap, GoDaddy, Porkbun, Cloudflare Registrar, Squarespace/Google Domains**), open **DNS Management / Advanced DNS**, and add the records corresponding to your chosen host:

### If Using Cloudflare Pages:
| Type | Name / Host | Target / Value | Proxy Status |
| :--- | :--- | :--- | :--- |
| **CNAME** | `@` (or apex) | `repurposed-tech.pages.dev` | DNS Only (or Proxied) |
| **CNAME** | `www` | `repurposed-tech.pages.dev` | DNS Only (or Proxied) |

*(Note: If your registrar does not support CNAME flattening on the `@` apex record, you can either switch your domain's nameservers to Cloudflare's free DNS, or use an ALIAS/ANAME record).*

### If Using Vercel:
| Type | Name / Host | Target / Value | TTL |
| :--- | :--- | :--- | :--- |
| **A** | `@` | `76.76.21.21` | Automatic / 3600 |
| **CNAME** | `www` | `cname.vercel-dns.com` | Automatic / 3600 |

### If Using Netlify:
| Type | Name / Host | Target / Value | TTL |
| :--- | :--- | :--- | :--- |
| **A** | `@` | `75.2.60.5` | Automatic / 3600 |
| **CNAME** | `www` | `<your-site-name>.netlify.app` | Automatic / 3600 |

### If Using GitHub Pages:
| Type | Name / Host | Target / Value | TTL |
| :--- | :--- | :--- | :--- |
| **A** | `@` | `185.199.108.153` | Automatic |
| **A** | `@` | `185.199.109.153` | Automatic |
| **A** | `@` | `185.199.110.153` | Automatic |
| **A** | `@` | `185.199.111.153` | Automatic |
| **CNAME** | `www` | `<username>.github.io` | Automatic |

---

## 🔄 Rebuilding & Updating in the Future

Whenever you expand donors, add new blueprints, or revise chapters, simply run one command to rebuild everything:

```powershell
python scripts/build_production.py
```

This updates the root files and regenerates `dist/` with updated word counts, sitemaps, and downloadable files, ready to redeploy in seconds!
