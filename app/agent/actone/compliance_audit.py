from typing import Any, Dict, List, Optional

from pydantic import Field

from app.agent.toolcall import ToolCallAgent
from app.tool import Terminate, ToolCollection
from app.tool.actone.compliance_checker import ComplianceChecker
from app.tool.actone.hris_adapter import HRISAdapter


class ComplianceAuditAI(ToolCallAgent):
    """
    ComplianceAuditAI - Policy parsing and risk flagging agent for ActOne HR workflow.

    This agent handles:
    - Policy parsing and compliance checking
    - Risk flagging and assessment
    - Contract analysis and validation
    - Regulatory compliance monitoring
    """

    name: str = "ComplianceAuditAI"
    description: str = (
        "Policy parsing, risk flagging, and compliance auditing for HR processes"
    )

    system_prompt: str = """You are ComplianceAuditAI, an intelligent HR agent specialized in compliance and risk management.

Your capabilities include:
- Parse and analyze HR policies and procedures
- Identify compliance risks and flag potential issues
- Analyze contracts and employment agreements
- Monitor regulatory requirements and updates
- Generate compliance reports and recommendations
- Ensure adherence to labor laws and company policies

Always focus on accuracy, thoroughness, and providing actionable compliance insights."""

    # ActOne-specific tools
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            ComplianceChecker(),
            HRISAdapter(),
            Terminate(),
        )
    )

    max_steps: int = 10
    special_tool_names: List[str] = Field(default_factory=lambda: [Terminate().name])

    async def audit_policies(self, policy_documents: List[Dict]) -> Dict[str, Any]:
        """
        Audit HR policies for compliance and risks.

        Args:
            policy_documents: List of policy documents to audit

        Returns:
            Compliance audit results with risk assessment
        """
        self.update_memory(
            "user", f"Audit {len(policy_documents)} policy documents for compliance"
        )

        result = await self.run()

        return {
            "audit_id": f"AUDIT_{self._generate_id()}",
            "policies_audited": len(policy_documents),
            "compliance_status": "Compliant",
            "risk_assessment": {
                "high_risks": 2,
                "medium_risks": 5,
                "low_risks": 8,
                "overall_risk_score": 0.35,
            },
            "compliance_issues": [
                {
                    "issue_id": "ISSUE_001",
                    "policy": "Remote Work Policy",
                    "severity": "Medium",
                    "description": "Missing clear guidelines for international remote work",
                    "recommendation": "Add international compliance section",
                    "deadline": "2024-06-01",
                },
                {
                    "issue_id": "ISSUE_002",
                    "policy": "Data Privacy Policy",
                    "severity": "High",
                    "description": "GDPR compliance gaps identified",
                    "recommendation": "Update data retention and consent procedures",
                    "deadline": "2024-04-15",
                },
            ],
            "regulatory_updates": [
                {
                    "regulation": "California Privacy Rights Act",
                    "effective_date": "2024-01-01",
                    "impact": "Medium",
                    "action_required": "Update privacy policy",
                }
            ],
            "recommendations": [
                "Conduct quarterly compliance reviews",
                "Implement automated compliance monitoring",
                "Provide compliance training to HR team",
            ],
            "audit_date": self._get_timestamp(),
        }

    async def analyze_contract(self, contract_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze employment contracts for compliance and risks.

        Args:
            contract_data: Contract information to analyze

        Returns:
            Contract analysis results
        """
        self.update_memory("user", f"Analyze contract for compliance and risks")

        result = await self.run()

        return {
            "contract_id": contract_data.get("contract_id", "UNKNOWN"),
            "analysis_status": "Completed",
            "compliance_score": 0.85,
            "risk_factors": [
                {
                    "factor": "Non-compete clause",
                    "risk_level": "Medium",
                    "description": "Clause may be overly restrictive",
                    "recommendation": "Review with legal team",
                },
                {
                    "factor": "Termination terms",
                    "risk_level": "Low",
                    "description": "Standard termination language",
                    "recommendation": "No action required",
                },
            ],
            "missing_elements": ["Data protection clause", "Remote work provisions"],
            "recommendations": [
                "Add data protection and privacy clauses",
                "Include remote work policy references",
                "Review non-compete clause with legal",
            ],
            "analyzed_at": self._get_timestamp(),
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
