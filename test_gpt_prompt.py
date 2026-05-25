"""Quick smoke test: call summarize on one fake repo, print gpt_image_prompt."""
import os
import sys

# Must be set before importing trending.config
os.environ["DEEPSEEK_API_KEY"] = sys.argv[1]

from trending.config import EnrichedRepo
from trending.summarize import summarize

repo = EnrichedRepo(
    owner="microsoft",
    name="autogen",
    full_name="microsoft/autogen",
    description="A programming framework for agentic AI, enabling multi-agent conversations.",
    language="Python",
    stars_total=42000,
    stars_today=1234,
    url="https://github.com/microsoft/autogen",
    readme_head="AutoGen is a framework for building multi-agent AI systems. "
                "It allows multiple LLM-powered agents to converse with each other "
                "and with humans to solve complex tasks. Supports code execution, "
                "human-in-the-loop, and flexible conversation patterns.",
    avatar_url="https://avatars.githubusercontent.com/u/6154722?s=200&v=4",
    license_spdx="CC-BY-4.0",
    default_branch="main",
)

print("Calling DeepSeek for microsoft/autogen ...")
results = summarize([repo])
sr = results[0]

print(f"\n=== intro_zh ===\n{sr.intro_zh}")
print(f"\n=== gpt_image_prompt (len={len(sr.gpt_image_prompt)}) ===")
print(sr.gpt_image_prompt[:500] + "..." if len(sr.gpt_image_prompt) > 500 else sr.gpt_image_prompt)
