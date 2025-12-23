class PageAssemblerAgent:
    def assemble(self, page_type, content_blocks):
        return {
            "page_type": page_type,
            "content": content_blocks
        }
