# theme.py
"""Blue-and-white visual theme: blue kariert grid paper, navy 'Füllertinte' ink
typography, and table-first grammar styling — a recolor of the reference-sheet
design used for the Grundlagen material. Supports a matching dark variant."""
import streamlit as st

_LIGHT_VARS = """
  --paper:#FAFBFD;
  --panel:#EEF3FB;
  --grid:rgba(30,64,120,0.10);
  --ink:#14213D;
  --ink-soft:#3E5474;
  --ink-faint:#7488A6;
  --accent:#2158C9;
  --accent-soft:rgba(33,88,201,0.12);
  --border:rgba(20,33,61,0.16);
  --warm:#B8791A;
  --warm-soft:rgba(184,121,26,0.12);
  --warm-border:rgba(184,121,26,0.35);
"""

_DARK_VARS = """
  --paper:#0B1220;
  --panel:#141F35;
  --grid:rgba(120,160,220,0.08);
  --ink:#E7EDF7;
  --ink-soft:#B7C4DC;
  --ink-faint:#7E8CA8;
  --accent:#5B9DFF;
  --accent-soft:rgba(91,157,255,0.18);
  --border:rgba(231,237,247,0.16);
  --warm:#E3B44E;
  --warm-soft:rgba(227,180,78,0.14);
  --warm-border:rgba(227,180,78,0.4);
"""

_CSS_TEMPLATE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Archivo+Narrow:wght@500;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;600&display=swap');

:root{{
{theme_vars}
  --display-font:'Archivo Narrow','Arial Narrow',sans-serif;
  --body-font:'Source Serif 4',Georgia,serif;
  --mono-font:'IBM Plex Mono','Consolas',monospace;
}}

[data-testid="stAppViewContainer"]{{
  background:
    repeating-linear-gradient(to bottom, var(--grid) 0 1px, transparent 1px 26px),
    repeating-linear-gradient(to right, var(--grid) 0 1px, transparent 1px 26px),
    var(--paper);
}}
[data-testid="stHeader"]{{ background:transparent; }}

[data-testid="stSidebar"]{{
  background:var(--panel);
  border-right:1px solid var(--border);
}}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3{{
  font-family:var(--display-font) !important;
  color:var(--ink) !important;
  border-bottom:none;
}}

html, body, [class*="css"]{{ color:var(--ink); font-family:var(--body-font); }}

h1, h2, h3{{
  font-family:var(--display-font) !important;
  color:var(--ink) !important;
  letter-spacing:.01em;
}}
h1{{ border-bottom:2px solid var(--accent); padding-bottom:.35em; font-weight:700 !important; }}
h2, h3{{ border-bottom:1px solid var(--border); padding-bottom:.25em; }}

[data-testid="stCaptionContainer"], .stCaption{{ color:var(--ink-faint) !important; opacity:1 !important; }}

/* Tabs */
[data-baseweb="tab-list"]{{ border-bottom:1px solid var(--border); gap:28px; }}
[data-baseweb="tab"]{{
  font-family:var(--display-font);
  letter-spacing:.03em;
  color:var(--ink-soft);
  padding-left:4px;
  padding-right:4px;
}}
[data-baseweb="tab"][aria-selected="true"]{{
  color:var(--accent);
  font-weight:700;
}}
[data-baseweb="tab-highlight"]{{ background-color:var(--accent) !important; }}

/* Buttons */
.stButton>button{{
  font-family:var(--display-font);
  letter-spacing:.03em;
  border:1.5px solid var(--accent);
  color:var(--accent);
  background:var(--paper);
  border-radius:3px;
}}
.stButton>button:hover{{
  background:var(--accent);
  color:#fff;
  border-color:var(--accent);
}}

/* Alerts / notes — reshape to the reference-sheet card, keep Streamlit's own
   semantic hue (info/success/warning/error) rather than forcing blue */
[data-testid="stAlertContainer"]{{
  border-radius:2px;
  border-left-width:4px;
  border-left-style:solid;
  font-family:var(--body-font);
}}

/* Expanders (grammar rules, verb conjugator) */
[data-testid="stExpander"]{{
  border:1px solid var(--border);
  border-radius:3px;
  background:var(--panel);
}}
[data-testid="stExpander"] summary{{ font-family:var(--display-font); color:var(--ink); }}

/* Metrics (quiz score) */
[data-testid="stMetricValue"]{{
  font-family:var(--mono-font);
  font-variant-numeric:tabular-nums;
  color:var(--accent);
}}
[data-testid="stMetricLabel"]{{ font-family:var(--display-font); }}

/* Dividers */
hr{{ border-color:var(--border) !important; }}

/* Example sentences rendered as "> Satz" markdown */
blockquote{{
  border-left:3px solid var(--accent);
  background:var(--accent-soft);
  padding:8px 16px;
  font-style:italic;
  color:var(--ink);
  border-radius:0 2px 2px 0;
}}

/* Tabular / monospace-friendly content */
code, pre, [data-testid="stDataFrame"]{{
  font-family:var(--mono-font) !important;
  font-variant-numeric:tabular-nums;
}}

/* Radio (quiz answers) */
.stRadio [role="radiogroup"] label{{ font-family:var(--body-font); color:var(--ink); }}

/* Native form widgets — Streamlit's own light-mode chrome doesn't follow our
   CSS variables by default, so force it explicitly to keep dark mode consistent */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stNumberInput"] input,
[data-baseweb="select"] > div,
[data-baseweb="input"]{{
  background:var(--panel) !important;
  color:var(--ink) !important;
  border-color:var(--border) !important;
}}
[data-baseweb="popover"], [data-baseweb="menu"]{{
  background:var(--panel) !important;
  color:var(--ink) !important;
}}
[data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li{{ color:var(--ink); }}

/* Textbook-style margin notes: Merke / Tipp / Beispiel callout boxes */
.note-box{{
  border-radius:2px;
  border-left-width:4px;
  border-left-style:solid;
  padding:10px 16px;
  margin:10px 0;
  font-family:var(--body-font);
}}
.note-box .note-label{{
  font-family:var(--display-font);
  font-weight:700;
  letter-spacing:.04em;
  text-transform:uppercase;
  font-size:.8em;
  display:block;
  margin-bottom:4px;
}}
.note-merke{{ background:var(--accent-soft); border-left-color:var(--accent); color:var(--ink); }}
.note-merke .note-label{{ color:var(--accent); }}
.note-tipp{{ background:var(--warm-soft); border-left-color:var(--warm); color:var(--ink); }}
.note-tipp .note-label{{ color:var(--warm); }}

/* Umlaut-dot accent - a small recurring German-typographic signature, used sparingly */
.umlaut-dots{{
  display:inline-block;
  letter-spacing:2px;
  color:var(--warm);
  font-weight:700;
}}

/* Idiom-of-the-day card - the one place motion is allowed in this app */
@keyframes idiom-settle{{
  from{{ opacity:0; transform:translateY(-6px); }}
  to{{ opacity:1; transform:translateY(0); }}
}}
.idiom-card{{
  border:1.5px solid var(--warm-border);
  background:var(--warm-soft);
  border-radius:4px;
  padding:14px 20px;
  margin-bottom:18px;
  animation:idiom-settle .5s ease-out;
}}
.idiom-card .idiom-label{{
  font-family:var(--display-font);
  font-weight:700;
  letter-spacing:.05em;
  text-transform:uppercase;
  font-size:.78em;
  color:var(--warm);
}}
.idiom-card .idiom-phrase{{
  font-family:var(--display-font);
  font-size:1.3em;
  font-weight:700;
  color:var(--ink);
  margin:2px 0 6px 0;
}}
.idiom-card .idiom-meaning{{ color:var(--ink-soft); font-style:italic; }}
.idiom-card .idiom-example{{ color:var(--ink-faint); margin-top:4px; }}
</style>
"""


def inject_custom_theme(dark: bool = False):
    theme_vars = _DARK_VARS if dark else _LIGHT_VARS
    st.markdown(_CSS_TEMPLATE.format(theme_vars=theme_vars), unsafe_allow_html=True)


def render_note_box(kind: str, label: str, text: str):
    """Textbook-style margin note. kind is 'merke' (grammar rule, navy) or 'tipp' (encouragement, gold)."""
    css_class = "note-merke" if kind == "merke" else "note-tipp"
    st.markdown(
        f'<div class="note-box {css_class}"><span class="note-label">{label}</span>{text}</div>',
        unsafe_allow_html=True,
    )


def render_idiom_card(idiom: str, meaning: str, example: str):
    """The one animated element in the app - a gold-accented 'Redewendung des Tages' card."""
    st.markdown(
        f'''<div class="idiom-card">
          <span class="idiom-label">✷ Redewendung des Tages</span>
          <div class="idiom-phrase">{idiom}</div>
          <div class="idiom-meaning">{meaning}</div>
          <div class="idiom-example">„{example}“</div>
        </div>''',
        unsafe_allow_html=True,
    )
