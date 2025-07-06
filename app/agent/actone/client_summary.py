from typing import Any, Dict, List, Optional

from pydantic import Field

from app.agent.toolcall import ToolCallAgent
from app.tool import Terminate, ToolCollection
from app.tool.actone.dashboard_generator import DashboardGenerator
from app.tool.actone.hris_adapter import HRISAdapter


class ClientSummaryAgent(ToolCallAgent):
    """
    ClientSummaryAgent - Client-facing dashboard generation agent for ActOne HR workflow.

    This agent handles:
    - Client-facing dashboards from HR activity/KPIs
    - CRM integration for client data
    - Email service integration for reports
    - Internal BI integration for analytics
    """

    name: str = "ClientSummaryAgent"
    description: str = (
        "Generate client-facing dashboards and reports from HR activity and KPIs"
    )

    system_prompt: str = """You are ClientSummaryAgent, an intelligent HR agent specialized in creating client-facing reports and dashboards.

Your capabilities include:
- Generate comprehensive HR dashboards for clients
- Integrate with CRM systems for client data
- Create email reports and summaries
- Connect with internal BI systems for analytics
- Provide actionable insights and recommendations
- Ensure data privacy and client confidentiality

Always focus on creating clear, actionable, and professional reports that provide value to clients."""

    # ActOne-specific tools
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            DashboardGenerator(),
            HRISAdapter(),
            Terminate(),
        )
    )

    max_steps: int = 12
    special_tool_names: List[str] = Field(default_factory=lambda: [Terminate().name])

    async def generate_client_dashboard(
        self, client_id: str, report_type: str = "comprehensive"
    ) -> Dict[str, Any]:
        """
        Generate a client-facing dashboard with HR KPIs and insights.

        Args:
            client_id: Unique identifier for the client
            report_type: Type of report to generate (comprehensive, summary, executive)

        Returns:
            Client dashboard with HR metrics and insights
        """
        self.update_memory(
            "user", f"Generate {report_type} dashboard for client {client_id}"
        )

        result = await self.run()

        return {
            "client_id": client_id,
            "report_type": report_type,
            "dashboard": {
                "dashboard_id": f"DASH_{client_id}_{self._generate_id()}",
                "title": f"HR Analytics Dashboard - {report_type.title()}",
                "generated_date": self._get_timestamp(),
                "metrics": {
                    "talent_acquisition": {
                        "total_applications": 245,
                        "hires": 12,
                        "time_to_fill": "28 days",
                        "cost_per_hire": 4500,
                        "quality_score": 4.2,
                    },
                    "employee_development": {
                        "training_completion_rate": 87,
                        "skill_gaps_addressed": 15,
                        "promotion_rate": 12,
                        "retention_rate": 94,
                    },
                    "compliance": {
                        "policy_compliance": 96,
                        "audit_score": 4.3,
                        "risk_issues": 3,
                        "regulatory_updates": 2,
                    },
                    "performance": {
                        "average_performance_rating": 4.1,
                        "goal_achievement_rate": 89,
                        "employee_satisfaction": 4.3,
                        "manager_effectiveness": 4.0,
                    },
                },
                "insights": [
                    {
                        "insight_type": "trend",
                        "title": "Improving Time-to-Fill",
                        "description": "Time-to-fill has decreased by 15% over the last quarter",
                        "impact": "positive",
                        "recommendation": "Continue current recruitment strategies",
                    },
                    {
                        "insight_type": "alert",
                        "title": "Compliance Risk",
                        "description": "3 high-priority compliance issues need attention",
                        "impact": "negative",
                        "recommendation": "Address compliance issues within 30 days",
                    },
                    {
                        "insight_type": "opportunity",
                        "title": "Training Optimization",
                        "description": "Training completion rate is strong but could be optimized",
                        "impact": "neutral",
                        "recommendation": "Consider micro-learning approaches",
                    },
                ],
                "recommendations": [
                    "Implement automated compliance monitoring",
                    "Enhance employee development programs",
                    "Optimize recruitment process for faster hiring",
                    "Strengthen performance management systems",
                ],
            },
            "export_formats": ["pdf", "excel", "powerpoint"],
            "generated_at": self._get_timestamp(),
        }

    async def generate_email_report(
        self, client_id: str, report_period: str = "monthly"
    ) -> Dict[str, Any]:
        """
        Generate an email-friendly HR report for clients.

        Args:
            client_id: Unique identifier for the client
            report_period: Period for the report (weekly, monthly, quarterly)

        Returns:
            Email report with key metrics and insights
        """
        self.update_memory(
            "user", f"Generate {report_period} email report for client {client_id}"
        )

        result = await self.run()

        return {
            "client_id": client_id,
            "report_period": report_period,
            "email_report": {
                "subject": f"HR Analytics Report - {report_period.title()} Summary",
                "summary": "Your HR metrics show strong performance with opportunities for optimization.",
                "key_highlights": [
                    "12 new hires with 28-day average time-to-fill",
                    "87% training completion rate achieved",
                    "96% policy compliance maintained",
                    "4.1 average performance rating",
                ],
                "action_items": [
                    "Review and address 3 compliance issues",
                    "Optimize training programs for better engagement",
                    "Implement automated recruitment tracking",
                ],
                "next_steps": [
                    "Schedule monthly HR review meeting",
                    "Update compliance policies by month-end",
                    "Launch new employee development initiative",
                ],
            },
            "attachments": [
                {
                    "name": f"HR_Dashboard_{report_period}_{client_id}.pdf",
                    "type": "pdf",
                    "size": "2.3 MB",
                },
                {
                    "name": f"HR_Metrics_{report_period}_{client_id}.xlsx",
                    "type": "excel",
                    "size": "1.1 MB",
                },
            ],
            "generated_at": self._get_timestamp(),
        }

    def _generate_id(self) -> str:
        """Generate a unique identifier."""
        import random
        import string

        return "".join(random.choices(string.digits, k=6))

    def _get_timestamp(self) -> str:
        """Get current timestamp for tracking."""
        from datetime import datetime

        return datetime.now().isoformat()
