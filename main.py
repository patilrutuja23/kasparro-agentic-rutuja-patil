import json
from orchestrator.pipeline import ContentPipeline

with open("data/product_input.json") as f:
    raw_data = json.load(f)

pipeline = ContentPipeline()
product_page, faq_page, comparison_page = pipeline.run(raw_data)

json.dump(product_page, open("outputs/product_page.json", "w", encoding="utf-8"), indent=2)
json.dump(faq_page, open("outputs/faq.json", "w", encoding="utf-8"), indent=2)
json.dump(comparison_page, open("outputs/comparison_page.json", "w", encoding="utf-8"), indent=2)