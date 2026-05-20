#!/usr/bin/env python3
"""
VAULT Build Script
==================
Reads:   index.html  (your source — never commit this)
Outputs: vault-deploy.html  (obfuscated — safe for public GitHub)

Run:  python3 build.py
"""

import re, subprocess, sys, os, datetime

SRC  = os.path.join(os.path.dirname(__file__), 'index.html')
DEST = os.path.join(os.path.dirname(__file__), 'vault-deploy.html')
OBF  = '/tmp/vault-tools/node_modules/.bin/javascript-obfuscator'

# ── Check tools ────────────────────────────────────────────────────────────────
if not os.path.exists(SRC):
    print('✗ index.html not found'); sys.exit(1)
if not os.path.exists(OBF):
    print('Installing obfuscator…')
    subprocess.run(['npm','install','--prefix','/tmp/vault-tools','javascript-obfuscator'],
                   check=True, capture_output=True)

# ── Read source ────────────────────────────────────────────────────────────────
print(f'Reading {SRC}…')
with open(SRC, encoding='utf-8') as f:
    html = f.read()

src_size = len(html)

# ── Extract & obfuscate all <script> blocks ────────────────────────────────────
SCRIPT_RE = re.compile(r'(<script(?:\s[^>]*)?>)([\s\S]*?)(</script>)', re.IGNORECASE)

def obfuscate_js(js_code):
    if not js_code.strip():
        return js_code
    tmp_in  = '/tmp/_vault_chunk_in.js'
    tmp_out = '/tmp/_vault_chunk_out.js'
    with open(tmp_in, 'w', encoding='utf-8') as f:
        f.write(js_code)
    result = subprocess.run([
        OBF, tmp_in,
        '--output', tmp_out,
        '--compact', 'true',
        '--control-flow-flattening', 'false',
        '--dead-code-injection', 'false',
        '--string-array', 'true',
        '--string-array-encoding', 'base64',
        '--string-array-threshold', '0.75',
        '--rename-globals', 'false',    # keeps onclick= handlers working
        '--rename-properties', 'false',
        '--identifier-names-generator', 'hexadecimal',
        '--self-defending', 'false',
        '--disable-console-output', 'true',
    ], capture_output=True, text=True)
    if result.returncode != 0:
        print(f'  ⚠ obfuscation warning: {result.stderr[:200]}')
        return js_code  # fallback: keep original
    with open(tmp_out, encoding='utf-8') as f:
        return f.read()

print('Obfuscating <script> blocks…')
counter = [0]

def replace_script(m):
    open_tag, js, close_tag = m.group(1), m.group(2), m.group(3)
    # Skip empty or tiny blocks
    if len(js.strip()) < 50:
        return m.group(0)
    counter[0] += 1
    print(f'  Block {counter[0]}: {len(js):,} chars → ', end='', flush=True)
    obf = obfuscate_js(js)
    print(f'{len(obf):,} chars')
    return open_tag + '\n' + obf + '\n' + close_tag

html_out = SCRIPT_RE.sub(replace_script, html)

# ── Add build stamp as HTML comment ───────────────────────────────────────────
stamp = f'<!-- VAULT build {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} -->\n'
html_out = stamp + html_out

# ── Write deploy file ──────────────────────────────────────────────────────────
with open(DEST, 'w', encoding='utf-8') as f:
    f.write(html_out)

dest_size = os.path.getsize(DEST)
print()
print('─' * 44)
print(f'✅  vault-deploy.html written')
print(f'    Source : {src_size/1024:.1f} KB')
print(f'    Deploy : {dest_size/1024:.1f} KB')
print(f'    Blocks : {counter[0]} script block(s) obfuscated')
print('─' * 44)
print('Push vault-deploy.html to GitHub. Keep index.html local.')
