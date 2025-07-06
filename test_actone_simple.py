#!/usr/bin/env python3
"""
Simple ActOne Test Script
Tests basic import and instantiation of ActOne agents.
"""

import asyncio

from app.logger import logger


def test_imports():
    """Test that all ActOne components can be imported."""
    try:
        logger.info("🔍 Testing ActOne imports...")

        # Test agent imports
        from app.agent.actone.client_summary import ClientSummaryAgent
        from app.agent.actone.compliance_audit import ComplianceAuditAI
        from app.agent.actone.skill_gap_analyzer import SkillGapAnalyzer
        from app.agent.actone.talent_scanner import TalentScannerAI
        from app.agent.actone.training_path_builder import TrainingPathBuilder
        from app.tool.actone.compliance_checker import ComplianceChecker
        from app.tool.actone.dashboard_generator import DashboardGenerator
        from app.tool.actone.hris_adapter import HRISAdapter
        from app.tool.actone.job_matcher import JobMatcher

        # Test tool imports
        from app.tool.actone.resume_parser import ResumeParser
        from app.tool.actone.skill_analyzer import SkillAnalyzer
        from app.tool.actone.training_generator import TrainingGenerator

        logger.info("✅ All imports successful!")
        return True

    except Exception as e:
        logger.error(f"❌ Import failed: {str(e)}")
        return False


def test_agent_instantiation():
    """Test that all ActOne agents can be instantiated."""
    try:
        logger.info("🔧 Testing agent instantiation...")

        # Test agent instantiation
        from app.agent.actone.client_summary import ClientSummaryAgent
        from app.agent.actone.compliance_audit import ComplianceAuditAI
        from app.agent.actone.skill_gap_analyzer import SkillGapAnalyzer
        from app.agent.actone.talent_scanner import TalentScannerAI
        from app.agent.actone.training_path_builder import TrainingPathBuilder

        # Create instances
        talent_agent = TalentScannerAI()
        skill_agent = SkillGapAnalyzer()
        training_agent = TrainingPathBuilder()
        compliance_agent = ComplianceAuditAI()
        client_agent = ClientSummaryAgent()

        logger.info("✅ All agents instantiated successfully!")
        logger.info(f"  - TalentScannerAI: {talent_agent.name}")
        logger.info(f"  - SkillGapAnalyzer: {skill_agent.name}")
        logger.info(f"  - TrainingPathBuilder: {training_agent.name}")
        logger.info(f"  - ComplianceAuditAI: {compliance_agent.name}")
        logger.info(f"  - ClientSummaryAgent: {client_agent.name}")

        return True

    except Exception as e:
        logger.error(f"❌ Agent instantiation failed: {str(e)}")
        return False


def test_tool_instantiation():
    """Test that all ActOne tools can be instantiated."""
    try:
        logger.info("🛠️ Testing tool instantiation...")

        # Test tool instantiation
        from app.tool.actone.compliance_checker import ComplianceChecker
        from app.tool.actone.dashboard_generator import DashboardGenerator
        from app.tool.actone.hris_adapter import HRISAdapter
        from app.tool.actone.job_matcher import JobMatcher
        from app.tool.actone.resume_parser import ResumeParser
        from app.tool.actone.skill_analyzer import SkillAnalyzer
        from app.tool.actone.training_generator import TrainingGenerator

        # Create instances
        resume_tool = ResumeParser()
        job_tool = JobMatcher()
        hris_tool = HRISAdapter()
        skill_tool = SkillAnalyzer()
        training_tool = TrainingGenerator()
        compliance_tool = ComplianceChecker()
        dashboard_tool = DashboardGenerator()

        logger.info("✅ All tools instantiated successfully!")
        logger.info(f"  - ResumeParser: {resume_tool.name}")
        logger.info(f"  - JobMatcher: {job_tool.name}")
        logger.info(f"  - HRISAdapter: {hris_tool.name}")
        logger.info(f"  - SkillAnalyzer: {skill_tool.name}")
        logger.info(f"  - TrainingGenerator: {training_tool.name}")
        logger.info(f"  - ComplianceChecker: {compliance_tool.name}")
        logger.info(f"  - DashboardGenerator: {dashboard_tool.name}")

        return True

    except Exception as e:
        logger.error(f"❌ Tool instantiation failed: {str(e)}")
        return False


async def test_basic_functionality():
    """Test basic functionality of one agent."""
    try:
        logger.info("🚀 Testing basic agent functionality...")

        from app.agent.actone.talent_scanner import TalentScannerAI

        # Create agent
        agent = TalentScannerAI()

        # Test basic method
        timestamp = agent._get_timestamp()
        logger.info(f"✅ Agent timestamp generation: {timestamp}")

        # Test tool collection
        tool_count = len(agent.available_tools.tool_map)
        logger.info(f"✅ Agent has {tool_count} tools available")

        return True

    except Exception as e:
        logger.error(f"❌ Basic functionality test failed: {str(e)}")
        return False


def main():
    """Run all tests."""
    logger.info("🎯 Starting ActOne System Tests")

    # Run tests
    tests = [
        ("Import Test", test_imports),
        ("Agent Instantiation Test", test_agent_instantiation),
        ("Tool Instantiation Test", test_tool_instantiation),
    ]

    results = []
    for test_name, test_func in tests:
        logger.info(f"\n{'='*50}")
        logger.info(f"Running {test_name}")
        logger.info(f"{'='*50}")
        result = test_func()
        results.append((test_name, result))

    # Run async test
    logger.info(f"\n{'='*50}")
    logger.info("Running Basic Functionality Test")
    logger.info(f"{'='*50}")
    async_result = asyncio.run(test_basic_functionality())
    results.append(("Basic Functionality Test", async_result))

    # Summary
    logger.info(f"\n{'='*50}")
    logger.info("TEST SUMMARY")
    logger.info(f"{'='*50}")

    passed = 0
    total = len(results)

    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        logger.info(f"{test_name}: {status}")
        if result:
            passed += 1

    logger.info(f"\nOverall: {passed}/{total} tests passed")

    if passed == total:
        logger.info("🎉 All tests passed! ActOne system is ready.")
    else:
        logger.error("⚠️ Some tests failed. Please check the errors above.")


if __name__ == "__main__":
    main()
