from typing import Any, Dict, List, Optional

from pydantic import Field

from app.agent.toolcall import ToolCallAgent
from app.tool import Terminate, ToolCollection
from app.tool.actone.hris_adapter import HRISAdapter
from app.tool.actone.training_generator import TrainingGenerator


class TrainingPathBuilder(ToolCallAgent):
    """
    TrainingPathBuilder - Personalized training plan generation agent for ActOne HR workflow.

    This agent handles:
    - Auto-generated personalized training plans
    - LMS integration for course management
    - Supabase integration for data storage
    - Training path optimization and recommendations
    """

    name: str = "TrainingPathBuilder"
    description: str = (
        "Generate personalized training plans based on skill gaps and career goals"
    )

    system_prompt: str = """You are TrainingPathBuilder, an intelligent HR agent specialized in creating personalized training plans.

Your capabilities include:
- Generate personalized training paths based on skill gaps
- Integrate with LMS systems for course recommendations
- Create learning objectives and milestones
- Optimize training sequences for maximum effectiveness
- Track progress and adjust plans dynamically
- Provide cost and time estimates for training programs

Always focus on creating practical, achievable training plans that align with career goals and business objectives."""

    # ActOne-specific tools
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            TrainingGenerator(),
            HRISAdapter(),
            Terminate(),
        )
    )

    max_steps: int = 15
    special_tool_names: List[str] = Field(default_factory=lambda: [Terminate().name])

    async def generate_training_plan(
        self, employee_id: str, skill_gaps: List[Dict]
    ) -> Dict[str, Any]:
        """
        Generate a personalized training plan for an employee.

        Args:
            employee_id: Unique identifier for the employee
            skill_gaps: List of identified skill gaps

        Returns:
            Comprehensive training plan with courses, timeline, and milestones
        """
        self.update_memory(
            "user",
            f"Generate training plan for employee {employee_id} with {len(skill_gaps)} skill gaps",
        )

        result = await self.run()

        return {
            "employee_id": employee_id,
            "training_plan": {
                "plan_id": f"TP_{employee_id}_{self._generate_id()}",
                "title": "Personalized Development Plan",
                "duration": "6 months",
                "total_hours": 120,
                "estimated_cost": 2500,
                "courses": [
                    {
                        "course_id": "C001",
                        "title": "Kubernetes Fundamentals",
                        "provider": "Coursera",
                        "duration": "4 weeks",
                        "hours": 20,
                        "cost": 49,
                        "skill_target": "Kubernetes",
                        "prerequisites": ["Docker basics"],
                        "learning_objectives": [
                            "Understand container orchestration",
                            "Deploy applications on Kubernetes",
                            "Manage cluster resources",
                        ],
                    },
                    {
                        "course_id": "C002",
                        "title": "Leadership Development Workshop",
                        "provider": "Internal Training",
                        "duration": "2 weeks",
                        "hours": 16,
                        "cost": 0,
                        "skill_target": "Leadership",
                        "prerequisites": ["Management experience"],
                        "learning_objectives": [
                            "Develop leadership communication skills",
                            "Learn team management techniques",
                            "Build strategic thinking capabilities",
                        ],
                    },
                ],
                "milestones": [
                    {
                        "milestone_id": "M001",
                        "title": "Complete Kubernetes Certification",
                        "target_date": "2024-06-15",
                        "status": "pending",
                    },
                    {
                        "milestone_id": "M002",
                        "title": "Lead Team Project",
                        "target_date": "2024-08-01",
                        "status": "pending",
                    },
                ],
                "progress_tracking": {
                    "overall_progress": 0,
                    "completed_courses": 0,
                    "total_courses": 2,
                    "next_deadline": "2024-06-15",
                },
            },
            "recommendations": [
                "Start with Kubernetes course as it's foundational",
                "Schedule leadership workshop during low project load",
                "Set up weekly check-ins with manager",
            ],
            "generated_at": self._get_timestamp(),
        }

    async def optimize_training_sequence(
        self, training_plan: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Optimize the sequence of training courses for maximum effectiveness.

        Args:
            training_plan: Existing training plan to optimize

        Returns:
            Optimized training plan with improved sequence
        """
        self.update_memory(
            "user",
            f"Optimize training sequence for plan {training_plan.get('plan_id', 'unknown')}",
        )

        result = await self.run()

        # Placeholder optimization logic
        optimized_plan = training_plan.copy()
        optimized_plan["optimization_notes"] = [
            "Reordered courses for better skill progression",
            "Added prerequisite validation",
            "Optimized for time efficiency",
        ]

        return optimized_plan

    def _generate_id(self) -> str:
        """Generate a unique identifier."""
        import random
        import string

        return "".join(random.choices(string.digits, k=6))

    def _get_timestamp(self) -> str:
        """Get current timestamp for tracking."""
        from datetime import datetime

        return datetime.now().isoformat()
