import csv
from enum import Enum

class Rule(Enum):
    KEYWORDS = "keywords"
    TOPIC = "topic"
    CLARIFYING = "clarifying"

RULE_TEMPLATES = {
    Rule.KEYWORDS: "llm-rubric:verify if the content of the answer contain these keywords: {{variables}}",
    Rule.TOPIC: "llm-rubric:verify if the content of the answer is related to this topic: {{variables}}",
    Rule.CLARIFYING: "llm-rubric:verify if the content is asking about this info: {{variables}}"
}

test_cases = [
    {
        "question": "Ik ben een werknemer. Wat betekent een volledige loopbaan in België?",
        "rule": Rule.KEYWORDS,
        "variables": {"keywords": "Geen antwoord, mypension.be, mypension-check"}
    },
    {
        "question": "Ik werk als werknemer. Wanneer kan ik vervroegd met pensioen gaan?",
        "rule": Rule.TOPIC,
        "variables": {"topic": "pensioenleeftijd en pensioendatum"}
    },
    {
        "question": "Ik ben werknemer en mijn pensioen is laag. Heb ik recht op een minimumpensioen?",
        "rule": Rule.CLARIFYING,
        "variables": {"info": "voorwaarden voor minimumpensioen"}
    }
]

output_file = "promptfoo_eval.csv"

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["question", "variables", "__expected"])
    
    for case in test_cases:
        template = RULE_TEMPLATES[case["rule"]]
        variables_str = "; ".join(case["variables"].values())
        writer.writerow([case["question"], variables_str, template])

print(f"CSV file '{output_file}' generated successfully!")
