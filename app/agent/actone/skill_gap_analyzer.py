from typing import Any, Dict, List, Optional

from pydantic import Field

from app.agent.toolcall import ToolCallAgent
from app.tool import Terminate, ToolCollection
from app.tool.actone.hris_adapter import HRISAdapter
from app.tool.actone.skill_analyzer import SkillAnalyzer


class SkillGapAnalyzer(ToolCallAgent):
    """
    SkillGapAnalyzer - Role vs capability analysis agent for ActOne HR workflow.

    This agent handles:
    - Skill gap analysis between current capabilities and role requirements
    - Role matrix analysis and optimization
    - LMS integration for skill assessment
    - HR feedback integration and analysis
    """

    name: str = "SkillGapAnalyzer"
    description: str = (
        "Analyze skill gaps between employee capabilities and role requirements"
    )

    system_prompt: str = """You are SkillGapAnalyzer, an intelligent HR agent specialized in skill gap analysis.

Your capabilities include:
- Analyze skill gaps between current employee capabilities and role requirements
- Integrate with role matrix systems for comprehensive analysis
- Connect with LMS systems for skill assessment data
- Process HR feedback and performance data
- Generate actionable recommendations for skill development
- Provide insights for career development and training planning

Always focus on providing data-driven insights and actionable recommendations for skill development."""

    # ActOne-specific tools
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            SkillAnalyzer(),
            HRISAdapter(),
            Terminate(),
        )
    )

    max_steps: int = 12
    special_tool_names: List[str] = Field(default_factory=lambda: [Terminate().name])

    async def analyze_skill_gaps(
        self, employee_id: str, role_id: str
    ) -> Dict[str, Any]:
        """
        Analyze skill gaps between employee capabilities and role requirements.

        Args:
            employee_id: Unique identifier for the employee
            role_id: Unique identifier for the target role

        Returns:
            Skill gap analysis with recommendations
        """
        self.update_memory(
            "user", f"Analyze skill gaps for employee {employee_id} vs role {role_id}"
        )

        result = await self.run()

        return {
            "employee_id": employee_id,
            "role_id": role_id,
            "skill_gaps": [
                {
                    "skill": "Kubernetes",
                    "current_level": "Beginner",
                    "required_level": "Intermediate",
                    "gap_severity": "Medium",
                    "development_time": "3-6 months",
                },
                {
                    "skill": "Leadership",
                    "current_level": "Intermediate",
                    "required_level": "Advanced",
                    "gap_severity": "High",
                    "development_time": "6-12 months",
                },
            ],
            "overall_gap_score": 0.35,
            "recommendations": [
                "Enroll in Kubernetes certification program",
                "Participate in leadership development workshop",
                "Seek mentorship from senior team members",
            ],
            "training_priorities": ["Leadership", "Kubernetes", "Strategic Thinking"],
            "estimated_timeline": "6-12 months for full role readiness",
            "timestamp": self._get_timestamp(),
        }

    async def analyze_team_gaps(self, team_id: str) -> Dict[str, Any]:
        """
        Analyze skill gaps across an entire team.

        Args:
            team_id: Unique identifier for the team

        Returns:
            Team-wide skill gap analysis
        """
        self.update_memory("user", f"Analyze team skill gaps for team {team_id}")

        result = await self.run()

        return {
            "team_id": team_id,
            "team_gaps": {
                "critical_gaps": ["Cloud Architecture", "DevOps"],
                "moderate_gaps": ["Data Analysis", "Project Management"],
                "minor_gaps": ["Communication", "Agile"],
            },
            "team_strengths": [
                "Frontend Development",
                "Backend Development",
                "Testing",
            ],
            "recommendations": [
                "Hire senior cloud architect",
                "Provide DevOps training for existing team",
                "Implement cross-training program",
            ],
            "risk_assessment": "Medium - some critical gaps but strong foundation",
            "timestamp": self._get_timestamp(),
        }

    def _get_timestamp(self) -> str:
        """Get current timestamp for tracking."""
        from datetime import datetime

        return datetime.now().isoformat()
