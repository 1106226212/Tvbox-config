import json, zipfile, os

base = r'E:\LoomyData\Workspace\资源搜集'
src = os.path.join(base, '.loomy-attachments', 'ses_e4ffd1aa6ffeqjbYkJthcoGw36', '1793954342350-0-tvbox-merged_jar_.json')
workdir = os.path.join(base, 'tvbox-config')

# Read original JSON
with open(src, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Enhance with TVBox metadata for JAR compatibility
config = {
    'version': '1.0.0',
    'home': 'https://www.lovedan.net',
    'logo': 'https://api.apibdzy.com/logo.png',
    'sites': data['sites'],
    'lives': data['lives'],
    'parses': data['parses'],
    'warnings': ''
}

# Write box.json (for both interface URL and JAR)
box_json_path = os.path.join(workdir, 'box.json')
with open(box_json_path, 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

# Create JAR (ZIP) containing box.json
jar_path = os.path.join(workdir, 'tvbox-config.jar')
with zipfile.ZipFile(jar_path, 'w', zipfile.ZIP_DEFLATED) as jar:
    jar.write(box_json_path, 'box.json')

# Also create a standalone interface JSON for direct URL use
iface_path = os.path.join(workdir, 'tvbox-interface.json')
with open(iface_path, 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print('=== Files created ===')
for p in [box_json_path, jar_path, iface_path]:
    print(f'{os.path.getsize(p)} bytes  {p}')
print(f'Sites: {len(data["sites"])}  Lives: {len(data["lives"])}  Parses: {len(data["parses"])}')
