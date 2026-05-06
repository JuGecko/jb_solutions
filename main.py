from collections import Counter
from dotenv import load_dotenv
from docent import Docent

load_dotenv("docent.env")
client = Docent()

# Task 1: Collection: 20260219_mini-v2.0.0_gpt-5-2-codex
collection_id = "fb22a2e4-0a41-4d41-8e1e-388d4cb50d80"
run_ids = client.list_agent_run_ids(collection_id)

for rid in run_ids:
    run = client.get_agent_run(collection_id, rid)
    if not run:
        continue
    counter = Counter()
    total_messages = 0
    for transcript in run.transcripts:
        for msg in transcript.messages:
            role = str(msg.role).lower()
            if role in ["tool", "assistant", "user", "system"]:
                counter[role] += 1
            total_messages += 1

    print(f"\n=========== Agent Run UUID: {rid} ===========")
    print(f"tool: {counter['tool']}")
    print(f"assistant: {counter['assistant']}")
    print(f"user: {counter['user']}")
    print(f"system: {counter['system']}")
    print("-----")
    print(f"Total messages: {total_messages}")
