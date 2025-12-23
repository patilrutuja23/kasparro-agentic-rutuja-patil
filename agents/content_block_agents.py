class ContentBlocks:

    def benefits_block(self, product):
        return {
            "benefits": product["benefits"]
        }

    def usage_block(self, product):
        return {
            "usage_instructions": product["usage"]
        }

    def ingredients_block(self, product):
        return {
            "ingredients": product["ingredients"]
        }

    def price_block(self, product):
        return {
            "price": product["price"]
        }

    def side_effects_block(self, product):
        return {
            "side_effects": product["side_effects"]
        }

    def comparison_block(self, product, competitor):
        return {
            "comparison": {
                "product": product["name"],
                "competitor": competitor["name"],
                "price_difference": "Competitor is more expensive"
            }
        }
