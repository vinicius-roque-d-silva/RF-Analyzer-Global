import sqlite3
import os
import socket
import sys
import subprocess
import webbrowser
import csv
from datetime import datetime
from scapy.all import sniff, IP

# --- CORES E ESTILO (ANSI) ---
class Color:
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# --- DEPENDÊNCIAS ---
try:
    import psutil
except ImportError:
    psutil = None

# --- CONFIGURAÇÃO DE CAMINHO ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'network_audit.db')

def draw_header(version="v6.3"):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Color.GREEN}{Color.BOLD}" + "="*75)
    print(f"      RF ANALYZER PRO {version} - GLOBAL ENTERPRISE EDITION")
    print("="*75 + f"{Color.RESET}")
    print(f"{Color.CYAN} HOST: {socket.gethostname()} | DB: {DB_PATH}{Color.RESET}")
    print("-" * 75)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''CREATE TABLE IF NOT EXISTS logs 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, 
                    source TEXT, destination TEXT, size INTEGER, identity TEXT)''')
    conn.commit()
    return conn

# --- FUNÇÕES DE COMANDO ---

def run_scan(limit=None):
    draw_header()
    print(f"{Color.YELLOW}[SCAN ATIVO]{Color.RESET} Alerta: {limit or 'OFF'} KB | CTRL+C para sair")
    conn = init_db()
    def handler(pkt):
        if pkt.haslayer(IP):
            src, dst, size = pkt[IP].src, pkt[IP].dst, len(pkt)
            conn.execute('INSERT INTO logs (source, destination, size, identity) VALUES (?,?,?,?)', 
                         (src, dst, size, dst))
            conn.commit()
            if limit and (size/1024) > limit: print(f"\a{Color.RED}[ALERTA: {size}b]{Color.RESET}")
            bar = "█" * min(size // 400, 30)
            print(f"{Color.GREEN}📶 {src:<15} → {dst:<15} | {bar}{Color.RESET}")
    try: sniff(prn=handler, store=0)
    except KeyboardInterrupt: pass
    finally: conn.close()

def run_observe():
    draw_header()
    conn = sqlite3.connect(DB_PATH)
    total = conn.execute("SELECT SUM(size) FROM logs").fetchone()[0] or 1
    print(f"{'DESTINO':<20} | {'VOLUME':<12} | {'SHARE %'}")
    for row in conn.execute("SELECT destination, SUM(size) as vol FROM logs GROUP BY destination ORDER BY vol DESC LIMIT 10"):
        share = (row[1]/total)*100
        print(f"{row[0]:<20} | {row[1]/1024:<9.2f} KB | {share:>6.1f}%")
    conn.close()
    input("\nEnter...")

def run_health():
    draw_header()
    if psutil:
        mem = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
        print(f"RAM Uso: {mem:.2f} MB")
    print(f"Tamanho DB: {os.path.getsize(DB_PATH)/1024/1024:.2f} MB")
    input("\nEnter...")

def run_web():
    draw_header()
    print(f"{Color.CYAN}Lançando Dashboard...{Color.RESET}")
    # Gerar HTML
    conn = sqlite3.connect(DB_PATH)
    data = conn.execute("SELECT destination, SUM(size) FROM logs GROUP BY destination ORDER BY SUM(size) DESC").fetchall()
    html = f"<html><body style='background:#000;color:#0f0;font-family:monospace;'><h1>AUDIT REPORT</h1>"
    html += "".join([f"<p>{d[0]}: {d[1]} bytes</p>" for d in data]) + "</body></html>"
    with open(os.path.join(BASE_DIR, "index.html"), "w") as f: f.write(html)
    conn.close()
    webbrowser.open("http://localhost:8000")
    subprocess.run(f"python -m http.server 8000 --directory \"{BASE_DIR}\"", shell=True)

def run_export():
    path = os.path.join(BASE_DIR, "audit.csv")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(cursor.fetchall())
    conn.close()
    print(f"Exportado para: {path}")
    input("\nEnter...")

# --- INTERFACE ---

def main():
    if os.name == 'nt': os.system('color')
    while True:
        draw_header()
        print(f"{Color.BOLD}COMMANDS:{Color.RESET} scan | observe | devices | health | web | export | reset | exit")
        cmd = input(f"{Color.GREEN}analyzer@admin:~# {Color.RESET}").lower().split()
        if not cmd: continue
        
        if cmd[0] == 'scan': run_scan(float(cmd[1]) if len(cmd)>1 else None)
        elif cmd[0] == 'observe': run_observe()
        elif cmd[0] == 'health': run_health()
        elif cmd[0] == 'web': run_web()
        elif cmd[0] == 'export': run_export()
        elif cmd[0] == 'devices':
            draw_header(); conn = sqlite3.connect(DB_PATH)
            for r in conn.execute("SELECT source, COUNT(*) FROM logs GROUP BY source"): print(f"IP: {r[0]} | Pacotes: {r[1]}")
            conn.close(); input("\nEnter...")
        elif cmd[0] == 'reset':
            if input("Zerar DB? (s/n): ") == 's':
                c = sqlite3.connect(DB_PATH); c.execute("DELETE FROM logs"); c.commit(); c.close()
        elif cmd[0] == 'exit': break

if __name__ == "__main__":
    main()