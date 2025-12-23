from agents.product_parser_agent import ProductParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.content_block_agents import ContentBlocks
from agents.template_engine_agent import TemplateEngineAgent
from agents.page_assembler_agent import PageAssemblerAgent


class ContentPipeline:
    def run(self, raw_data):
        product = ProductParserAgent().run(raw_data)

        questions = QuestionGeneratorAgent().run(product)

        blocks = ContentBlocks()
        product_page = PageAssemblerAgent().assemble(
            "product_page",
            {
                **blocks.ingredients_block(product),
                **blocks.benefits_block(product),
                **blocks.usage_block(product),
                **blocks.price_block(product)
            }
        )

        faq_page = PageAssemblerAgent().assemble(
            "faq",
            {"questions": questions}
        )

        competitor = {
            "name": "RadiancePlus Serum",
            "price": "₹899",
            "ingredients": ["Vitamin C", "Niacinamide"]
        }

        comparison_page = PageAssemblerAgent().assemble(
            "comparison",
            blocks.comparison_block(product, competitor)
        )

        return product_page, faq_page, comparison_page
