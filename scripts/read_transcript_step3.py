import json

with open(r'C:\Users\karma\.gemini\antigravity\brain\5e9a81ab-3e75-499e-94e7-7e11fb483cbb\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        idx = obj.get('step_index')
        if idx in range(1665, 1680):
            print(f"=== STEP {idx} ({obj.get('type')}) ===")
            print(f"Content: {obj.get('content')[:300] if obj.get('content') else ''}")
            print(f"Thinking: {obj.get('thinking')[:300] if obj.get('thinking') else ''}")
