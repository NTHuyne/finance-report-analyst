from src.nodes.html_generator.html_template import html_template
from langchain_core.prompts import ChatPromptTemplate


safe_html_template = html_template.replace("{", "{{").replace("}", "}}")


system_prompt = f"""
You are an expert web developer and data visualizer.

## Provided Inputs:
1. HTML Template:
{safe_html_template}

## Task:
- Use the provided report content to fill in the appropriate sections of the HTML template.
- Preserve the structure and styling of the template.
- Generate **interactive or static charts/graphs** (e.g., bar charts, line charts, pie charts) where the content includes relevant numerical data or comparisons.
- **Do not include** any sections from the template that do not have corresponding content in the report.
- If the content mentions key metrics (e.g., tăng trưởng, so sánh, cao nhất, thấp nhất), generate suitable charts to visualize them.

## Output Requirements:
- Return only the complete HTML code.
- Do not output any explanations, comments, or extra text.
- Ensure all placeholders in the template are properly filled or removed if not applicable.

"""


code_generator_instruction = """
Convert the provided financial analysis report into a complete HTML document using the given template.
{content}
"""


code_generator_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("placeholder", "{messages}"),
    ]
)

