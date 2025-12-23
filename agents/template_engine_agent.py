class TemplateEngineAgent:

    def get_template(self, page_type):
        if page_type == "product_page":
            return ["ingredients", "benefits", "usage_instructions", "price"]

        if page_type == "faq":
            return ["questions_and_answers"]

        if page_type == "comparison":
            return ["comparison"]
