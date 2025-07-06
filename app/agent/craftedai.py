from pydantic import model_validator

from app.agent.base import ToolCallAgent
from app.prompt.craftedai import NEXT_STEP_PROMPT, SYSTEM_PROMPT
from app.sandbox.client import BrowserContextHelper
from app.tool import Terminate, ToolCollection
from app.tool.ask_human import AskHuman
from app.tool.bash import Bash
from app.tool.browser_use_tool import BrowserUseTool
from app.tool.create_chat_completion import CreateChatCompletion
from app.tool.file_operators import FileOperators
from app.tool.lxp_tool import LXPTool
from app.tool.planning import PlanningTool
from app.tool.str_replace_editor import StrReplaceEditor
from app.tool.terminate import Terminate
from app.tool.tool_collection import ToolCollection
from app.tool.web_search import WebSearch


class CraftedAI(ToolCallAgent):
    """A versatile general-purpose agent with support for both local and MCP tools."""

    name: str = "CraftedAI"
    description: str = (
        "A versatile agent that can solve various tasks using multiple tools including MCP-based tools"
    )

    @model_validator(mode="after")
    def initialize_helper(self) -> "CraftedAI":
        """Initialize basic components synchronously."""
        self.browser_context_helper = BrowserContextHelper(self)
        return self

    @classmethod
    async def create(cls, **kwargs) -> "CraftedAI":
        """Factory method to create and properly initialize a CraftedAI instance."""
        instance = cls(**kwargs)
        await instance.initialize_mcp_servers()
        return instance

    async def cleanup(self):
        """Clean up CraftedAI agent resources."""
        if self.browser_context_helper:
            await self.browser_context_helper.cleanup_browser()
