import json
from agent_updated import analyze

with open("policies.json", encoding="utf-8") as f:
    policies = json.load(f)
with open("tickets.json", encoding="utf-8") as f:
    tickets = json.load(f)

cases = [
    ("REQ-01", "My laptop won’t turn on at all, it’s completely dead, had it about 3.5 years now.", "Human Review", True),
    ("REQ-02", "Can I get Wi-Fi access for a guest visiting our office tomorrow?", "Resolve", False),
    ("REQ-03", "I’m locked out of my account, tried my password 6 times.", "Resolve", True),
    ("REQ-04", "Need approval to install a data-analysis tool that’s not in the software catalog.", "Security Escalation", True),
    ("REQ-05", "My VPN stopped working this morning, says credentials expired.", "Employee Action Required", False),
    ("REQ-06", "Printer on the 3rd floor keeps showing paper jam even though there’s no jam.", "Employee/IT Action Required", False),
    ("REQ-07", "I’ve started working from home 4 days a week, how do I get a monitor?", "Employee Action Required", False),
    ("REQ-08", "I think I got a phishing email asking for my login — forwarding it to a few teammates to check.", "Security Escalation", False),
    ("REQ-09", "My mailbox is full and I can’t send emails.", "Employee Action Required", False),
    ("REQ-10", "Can someone give me admin access to the finance reporting server? Need it urgently for month-end.", "Human Review", True),
    ("REQ-11", "New contractor joining my team next week, they’ll need VPN access.", "Approval Required", True),
    ("REQ-12", "I can’t log into the expense tool, keeps saying invalid credentials.", "Route to Finance / IT support", True),
    ("REQ-13", "Laptop screen is flickering on and off, had it 2 years, might just need a fix not a replacement.", "Human Review", True),
    ("REQ-14", "Requesting approval to install a browser extension for productivity tracking.", "Human Review", False),
    ("REQ-15", "hey can you help, its not working", "Clarification Required", False),
]

for request_id, text, expected_decision, expected_ticket in cases:
    result = analyze(text, policies, tickets)
    assert result["decision"] == expected_decision, (request_id, result)
    assert result["ticket_required"] is expected_ticket, (request_id, result)

# Boundary cases
assert analyze("I tried my password 5 times", policies, tickets)["ticket_required"] is True
assert analyze("Guest wifi please", policies, tickets)["ticket_required"] is False
assert analyze("My VPN is not working", policies, tickets)["decision"] == "Clarification Required"
assert analyze("", policies, tickets)["decision"] == "Clarification Required"
security_result = analyze("I think I got a phishing email asking for my login.", policies, tickets)
assert security_result["ticket_required"] is False
assert "security@veridian-corp.example" in security_result["next_action"]

print("All Python decision tests passed.")
