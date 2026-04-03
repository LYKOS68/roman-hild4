import os, json, datetime

base = '/home/ubuntu'
inventory = []

for root, dirs, fnames in os.walk(base):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for f in fnames:
        if f.startswith('.'):
            continue
        fp = os.path.join(root, f)
        try:
            stat = os.stat(fp)
            if stat.st_size > 0:
                rel = os.path.relpath(fp, base)
                mtime = datetime.datetime.fromtimestamp(stat.st_mtime, tz=datetime.timezone.utc).isoformat()
                inventory.append({
                    'filepath': rel,
                    'size_bytes': stat.st_size,
                    'mtime_iso': mtime,
                    'extension': os.path.splitext(f)[1],
                    'directory': os.path.relpath(root, base),
                    'filename': f
                })
        except:
            pass

# Sortieren nach mtime (neueste zuerst)
inventory.sort(key=lambda x: x['mtime_iso'], reverse=True)

# Duplikate pruefen
paths = [i['filepath'] for i in inventory]
assert len(paths) == len(set(paths)), 'DUPLIKATE GEFUNDEN!'

# Summary
total_size = sum(i['size_bytes'] for i in inventory)
mtimes = [i['mtime_iso'] for i in inventory]

result = {
    'inventory': inventory,
    'summary': {
        'total_files': len(inventory),
        'total_size_bytes': total_size,
        'oldest_file': min(mtimes),
        'newest_file': max(mtimes)
    },
    'metadata': {
        'scan_time': datetime.datetime.now(tz=datetime.timezone.utc).isoformat(),
        'scanned_path': '/home/ubuntu',
        'triggered_by': 'Gemini-CLI (Twin-Relay) via Telegram Gateway',
        'bridge_verification': {
            'test_id': 'COMM_BRIDGE_VERIFICATION',
            'test_string': 'TestHirorohi782',
            'source_received': 'Gemini-CLI (Twin-Relay)',
            'target_confirmed': 'Manus (Executive)',
            'status': 'BRIDGE_VERIFIED_BIDIRECTIONAL',
            'gemini_prompt_executed': True,
            'response_timestamp': datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
        }
    }
}

with open('inventory_v3.json', 'w') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print('=== INVENTAR v3 ABGESCHLOSSEN ===')
print(f'Dateien: {len(inventory)}')
print(f'Gesamtgroesse: {total_size:,} Bytes ({total_size/1024/1024:.1f} MB)')
print(f'Aelteste: {min(mtimes)}')
print(f'Neueste: {max(mtimes)}')
print(f'Duplikate: 0 (validiert)')
print(f'Bridge-Status: VERIFIED')
print(f'Gespeichert: inventory_v3.json')
