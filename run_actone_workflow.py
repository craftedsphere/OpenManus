#!/usr/bin/env python3
"""
ActOne HR Workflow Runner
This script demonstrates the complete ActOne HR workflow integration.
"""

import asyncio
import time
from typing import Any, Dict

from app.agent.actone.client_summary import ClientSummaryAgent
from app.agent.actone.compliance_audit import ComplianceAuditAI
from app.agent.actone.skill_gap_analyzer import SkillGapAnalyzer
from app.agent.actone.talent_scanner import TalentScannerAI
from app.agent.actone.training_path_builder import TrainingPathBuilder

# from app.agent.craftedai import CraftedAI  # Commented out due to import issues
from app.agent.data_analysis import DataAnalysis
from app.agent.lxp import LXPAgent
from app.flow.flow_factory import FlowFactory, FlowType
from app.logger import logger


class ActOneWorkflowRunner:
    """ActOne HR Workflow Runner with all integrated agents."""

    def __init__(self):
        self.agents = self._initialize_agents()
        self.workflow_results = {}

    def _initialize_agents(self) -> Dict[str, Any]:
        """Initialize all ActOne agents."""
        return {
            # ActOne HR Workflow Agents
            "talent_scanner": TalentScannerAI(),
            "skill_gap_analyzer": SkillGapAnalyzer(),
            "training_path_builder": TrainingPathBuilder(),
            "compliance_audit": ComplianceAuditAI(),
            "client_summary": ClientSummaryAgent(),
            # Supporting Agents
            # "craftedai": CraftedAI(),  # Commented out due to import issues
            "data_analysis": DataAnalysis(),
            "lxp": LXPAgent(),
        }

    async def run_complete_hr_workflow(
        self, resume_data: Dict[str, Any], job_id: str, client_id: str
    ):
        """Run the complete ActOne HR workflow."""
        logger.info("🚀 Starting ActOne HR Workflow")
        start_time = time.time()

        try:
            # Step 1: Resume Processing and Job Matching
            logger.info("📝 Step 1: Processing resume and job matching")
            talent_result = await self._run_talent_scanning(resume_data, job_id)
            self.workflow_results["talent_scanning"] = talent_result

            # Step 2: Skill Gap Analysis
            logger.info("🔍 Step 2: Analyzing skill gaps")
            skill_gaps = await self._run_skill_gap_analysis(talent_result)
            self.workflow_results["skill_analysis"] = skill_gaps

            # Step 3: Training Path Generation
            logger.info("📚 Step 3: Generating training path")
            training_plan = await self._run_training_path_builder(skill_gaps)
            self.workflow_results["training_plan"] = training_plan

            # Step 4: Compliance Audit
            logger.info("⚖️ Step 4: Conducting compliance audit")
            compliance_result = await self._run_compliance_audit()
            self.workflow_results["compliance_audit"] = compliance_result

            # Step 5: Client Dashboard Generation
            logger.info("📊 Step 5: Generating client dashboard")
            dashboard = await self._run_client_summary(client_id)
            self.workflow_results["client_dashboard"] = dashboard

            # Generate final summary
            final_summary = self._generate_workflow_summary()

            elapsed_time = time.time() - start_time
            logger.info(
                f"✅ ActOne HR Workflow completed in {elapsed_time:.2f} seconds"
            )

            return final_summary

        except Exception as e:
            logger.error(f"❌ ActOne HR Workflow failed: {str(e)}")
            raise

    async def _run_talent_scanning(
        self, resume_data: Dict[str, Any], job_id: str
    ) -> str:
        """Run talent scanning workflow."""
        talent_agent = self.agents["talent_scanner"]

        # Process resume
        resume_result = await talent_agent.process_resume(resume_data)
        logger.info(f"Resume Processing Result: {resume_result}")

        # Match to job requirements
        match_result = await talent_agent.match_job_requirements(
            resume_data.get("candidate_id", "UNKNOWN"), job_id
        )
        logger.info(f"Job Matching Result: {match_result}")

        return f"Resume Processing: {resume_result}\nJob Matching: {match_result}"

    async def _run_skill_gap_analysis(self, talent_result: str) -> str:
        """Run skill gap analysis workflow."""
        skill_agent = self.agents["skill_gap_analyzer"]
        # Just pass a placeholder since we don't have structured data
        skill_gaps = await skill_agent.analyze_skill_gaps("CAND_001", "ROLE_001")
        logger.info(f"Skill Gap Analysis Result: {skill_gaps}")
        return str(skill_gaps)

    async def _run_training_path_builder(self, skill_gaps: str) -> str:
        """Run training path builder workflow."""
        training_agent = self.agents["training_path_builder"]
        training_plan = await training_agent.generate_training_plan("CAND_001", [])
        logger.info(f"Training Plan Result: {training_plan}")
        return str(training_plan)

    async def _run_compliance_audit(self) -> str:
        """Run compliance audit workflow."""
        compliance_agent = self.agents["compliance_audit"]
        sample_policies = [
            {"name": "Remote Work Policy", "content": "Sample policy content..."},
            {"name": "Data Privacy Policy", "content": "Sample privacy policy..."},
        ]
        audit_result = await compliance_agent.audit_policies(sample_policies)
        logger.info(f"Compliance Audit Result: {audit_result}")
        return str(audit_result)

    async def _run_client_summary(self, client_id: str) -> str:
        """Run client summary generation workflow."""
        client_agent = self.agents["client_summary"]
        dashboard = await client_agent.generate_client_dashboard(
            client_id, "comprehensive"
        )
        email_report = await client_agent.generate_email_report(client_id, "monthly")
        logger.info(f"Dashboard Result: {dashboard}")
        logger.info(f"Email Report Result: {email_report}")
        return f"Dashboard: {dashboard}\nEmail Report: {email_report}"

    def _generate_workflow_summary(self) -> Dict[str, Any]:
        """Generate a comprehensive workflow summary."""
        return {
            "workflow_id": f"ACTONE_{int(time.time())}",
            "status": "completed",
            "steps_completed": len(self.workflow_results),
            "results": self.workflow_results,
            "summary": {"all_results": list(self.workflow_results.values())},
            "recommendations": [
                "Review all step outputs above.",
                "Proceed with candidate if fit score is high (see job matching output)",
                "Address any compliance issues (see compliance audit output)",
                "Implement recommended training plan (see training plan output)",
                "Schedule follow-up review in 30 days",
            ],
            "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        }


async def main():
    """Main function to run ActOne workflow demonstration."""
    logger.info("🎯 ActOne HR Workflow Demonstration")

    # Initialize workflow runner
    runner = ActOneWorkflowRunner()

    # Sample data for demonstration
    sample_resume_data = {
        "candidate_id": "CAND_001",
        "resume_content": "Sample resume content...",
        "format": "pdf",
    }

    sample_job_id = "JOB_001"
    sample_client_id = "CLIENT_001"

    try:
        # Run complete workflow
        result = await runner.run_complete_hr_workflow(
            sample_resume_data, sample_job_id, sample_client_id
        )

        # Display results
        logger.info("📋 Workflow Results:")
        logger.info(f"Workflow ID: {result['workflow_id']}")
        logger.info(f"Status: {result['status']}")
        logger.info(f"Steps Completed: {result['steps_completed']}")

        logger.info("📊 Summary:")
        summary = result["summary"]
        logger.info(f"  - All Results: {summary['all_results']}")

        logger.info("💡 Recommendations:")
        for rec in result["recommendations"]:
            logger.info(f"  - {rec}")

        logger.info("✅ ActOne HR Workflow demonstration completed successfully!")

    except Exception as e:
        logger.error(f"❌ Workflow demonstration failed: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())
