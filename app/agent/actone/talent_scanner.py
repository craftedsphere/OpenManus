from typing import Any, Dict, List, Optional

from pydantic import Field

from app.agent.toolcall import ToolCallAgent
from app.tool import Terminate, ToolCollection
from app.tool.actone.hris_adapter import HRISAdapter
from app.tool.actone.job_matcher import JobMatcher
from app.tool.actone.resume_parser import ResumeParser


class TalentScannerAI(ToolCallAgent):
    """
    TalentScannerAI - Resume parsing and job matching agent for ActOne HR workflow.

    This agent handles:
    - Resume parsing and skill extraction
    - Job matching and role fit analysis
    - HRIS integration for candidate data
    - Resume database management
    """

    name: str = "TalentScannerAI"
    description: str = (
        "Resume parsing, skill extraction, and job matching agent for HR workflows"
    )

    system_prompt: str = """You are TalentScannerAI, an intelligent HR agent specialized in resume parsing and job matching.

Your capabilities include:
- Parse resumes and extract key information (skills, experience, education)
- Match candidates to job requirements and company roles
- Integrate with HRIS systems for candidate data management
- Provide role fit scores and recommendations
- Maintain resume database with search capabilities

Always focus on accuracy, compliance, and providing actionable insights for HR decision-making."""

    # ActOne-specific tools
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            ResumeParser(),
            JobMatcher(),
            HRISAdapter(),
            Terminate(),
        )
    )

    max_steps: int = 15
    special_tool_names: List[str] = Field(default_factory=lambda: [Terminate().name])

    async def process_resume(self, resume_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a resume and return structured candidate data.

        Args:
            resume_data: Raw resume data (file path, text, or structured data)

        Returns:
            Structured candidate information with skills, experience, and role fit
        """
        # Update memory with resume data
        self.update_memory("user", f"Process resume: {resume_data}")

        # Execute resume processing workflow
        result = await self.run()

        return {
            "candidate_id": resume_data.get("candidate_id"),
            "parsed_data": result,
            "processing_status": "completed",
            "timestamp": self._get_timestamp(),
        }

    async def match_job_requirements(
        self, candidate_id: str, job_id: str
    ) -> Dict[str, Any]:
        """
        Match a candidate to specific job requirements.

        Args:
            candidate_id: Unique identifier for the candidate
            job_id: Unique identifier for the job position

        Returns:
            Job matching results with fit score and recommendations
        """
        self.update_memory("user", f"Match candidate {candidate_id} to job {job_id}")

        result = await self.run()

        return {
            "candidate_id": candidate_id,
            "job_id": job_id,
            "fit_score": 0.85,  # Placeholder - would be calculated by JobMatcher
            "skill_match": ["python", "react", "agile"],  # Placeholder
            "missing_skills": ["kubernetes"],  # Placeholder
            "recommendations": ["Consider for senior role", "Needs cloud training"],
            "timestamp": self._get_timestamp(),
        }

    def _get_timestamp(self) -> str:
        """Get current timestamp for tracking."""
        from datetime import datetime

        return datetime.now().isoformat()
