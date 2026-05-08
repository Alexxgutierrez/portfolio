# My Portfolio — GitHub Pages

A clean, dark-themed personal portfolio built with pure HTML/CSS.

## 📁 Files

| File | Purpose |
|------|---------|
| `index.html` | Main portfolio page (edit this with your info) |
| `deploy.py` | One-command deploy script to GitHub Pages |
| `resume.pdf` | Place your resume PDF here |

## ✏️ How to Customize

Open `index.html` and replace all placeholder text:

- `Your Name` → your actual name
- `[your role]` → e.g., "Software Engineer"
- `[your city]` → your location
- Project cards → your real projects with GitHub/live links
- Experience section → your work history
- Education section → your degrees/certs
- Awards section → your achievements
- Contact links → your real email, GitHub, LinkedIn

## 🚀 Deploy to GitHub Pages

### Step 1 — Create a GitHub repo
Go to https://github.com/new and create a public repo named `portfolio`.

### Step 2 — Configure the deploy script
Open `deploy.py` and set your username:
```python
GITHUB_USERNAME = "your-github-username"
```

### Step 3 — Run the deployer
```bash
python deploy.py
```

### Step 4 — Enable GitHub Pages
1. Go to your repo → Settings → Pages
2. Source: **Deploy from branch**
3. Branch: `main` → `/ (root)`
4. Save

Your site will be live at `https://your-username.github.io/portfolio/`

## 📬 Contact Form
The contact form uses [Formspree](https://formspree.io) (free).
1. Sign up at formspree.io
2. Create a new form → copy the form ID
3. In `index.html`, replace `YOUR_FORM_ID` in the form action URL

## 🎨 Customizing Colors
Edit the CSS variables at the top of `index.html`:
```css
:root {
  --accent: #c8f060;   /* lime green highlights */
  --accent2: #5be0c8;  /* teal accents */
}
```
