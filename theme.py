# theme.py
"""Blue-and-white visual theme: blue kariert grid paper, navy 'Füllertinte' ink
typography, and table-first grammar styling — a recolor of the reference-sheet
design used for the Grundlagen material."""
import streamlit as st

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Archivo+Narrow:wght@500;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;600&display=swap');

:root{
  --paper:#FAFBFD;
  --panel:#EEF3FB;
  --grid:rgba(30,64,120,0.10);
  --ink:#14213D;
  --ink-soft:#3E5474;
  --ink-faint:#7488A6;
  --accent:#2158C9;
  --accent-soft:rgba(33,88,201,0.12);
  --border:rgba(20,33,61,0.16);
  --display-font:'Archivo Narrow','Arial Narrow',sans-serif;
  --body-font:'Source Serif 4',Georgia,serif;
  --mono-font:'IBM Plex Mono','Consolas',monospace;
}

[data-testid="stAppViewContainer"]{
  background:
    repeating-linear-gradient(to bottom, var(--grid) 0 1px, transparent 1px 26px),
    repeating-linear-gradient(to right, var(--grid) 0 1px, transparent 1px 26px),
    var(--paper);
}
[data-testid="stHeader"]{ background:transparent; }

html, body, [class*="css"]{ color:var(--ink); font-family:var(--body-font); }

h1, h2, h3{
  font-family:var(--display-font) !important;
  color:var(--ink) !important;
  letter-spacing:.01em;
}
h1{ border-bottom:2px solid var(--accent); padding-bottom:.35em; font-weight:700 !important; }
h2, h3{ border-bottom:1px solid var(--border); padding-bottom:.25em; }

[data-testid="stCaptionContainer"], .stCaption{ color:var(--ink-faint) !important; opacity:1 !important; }

/* Tabs */
[data-baseweb="tab-list"]{ border-bottom:1px solid var(--border); gap:6px; }
[data-baseweb="tab"]{
  font-family:var(--display-font);
  letter-spacing:.03em;
  color:var(--ink-soft);
}
[data-baseweb="tab"][aria-selected="true"]{
  color:var(--accent);
  font-weight:700;
}
[data-baseweb="tab-highlight"]{ background-color:var(--accent) !important; }

/* Buttons */
.stButton>button{
  font-family:var(--display-font);
  letter-spacing:.03em;
  border:1.5px solid var(--accent);
  color:var(--accent);
  background:var(--paper);
  border-radius:3px;
}
.stButton>button:hover{
  background:var(--accent);
  color:#fff;
  border-color:var(--accent);
}

/* Alerts / notes — reshape to the reference-sheet card, keep Streamlit's own
   semantic hue (info/success/warning/error) rather than forcing blue */
[data-testid="stAlertContainer"]{
  border-radius:2px;
  border-left-width:4px;
  border-left-style:solid;
  font-family:var(--body-font);
}

/* Expanders (grammar rules, verb conjugator) */
[data-testid="stExpander"]{
  border:1px solid var(--border);
  border-radius:3px;
  background:var(--panel);
}
[data-testid="stExpander"] summary{ font-family:var(--display-font); }

/* Metrics (quiz score) */
[data-testid="stMetricValue"]{
  font-family:var(--mono-font);
  font-variant-numeric:tabular-nums;
  color:var(--accent);
}
[data-testid="stMetricLabel"]{ font-family:var(--display-font); }

/* Dividers */
hr{ border-color:var(--border) !important; }

/* Example sentences rendered as "> Satz" markdown */
blockquote{
  border-left:3px solid var(--accent);
  background:var(--accent-soft);
  padding:8px 16px;
  font-style:italic;
  color:var(--ink);
  border-radius:0 2px 2px 0;
}

/* Tabular / monospace-friendly content */
code, pre, [data-testid="stDataFrame"]{
  font-family:var(--mono-font) !important;
  font-variant-numeric:tabular-nums;
}

/* Radio (quiz answers) */
.stRadio [role="radiogroup"] label{ font-family:var(--body-font); }
</style>
"""


def inject_custom_theme():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
