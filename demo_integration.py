#!/usr/bin/env python3
"""
OpenManus + Autonomous LXP Integration Demo

This script demonstrates the integration between OpenManus's general-purpose
AI agent framework and the Autonomous LXP's specialized learning capabilities.
"""

import asyncio
import json
from typing import Any, Dict

from app.agent.craftedai import CraftedAI
from app.agent.lxp import LXPAgent
from app.logger import logger
from app.tool.lxp_tool import LXPTool


async def demo_learning_scenario():
    """Demonstrate a complete learning scenario using the integrated system"""

    print("🚀 OpenManus + Autonomous LXP Integration Demo")
    print("=" * 60)

    # Initialize the LXP tool
    lxp_tool = LXPTool()

    # Demo 1: Skill Assessment
    print("\n📊 Demo 1: Skill Assessment")
    print("-" * 30)

    assessment_result = await lxp_tool.execute(
        action="assess_skills",
        learner_profile={
            "name": "Alice Johnson",
            "role": "Data Analyst",
            "experience": "2 years",
            "background": "Business degree, some Python experience",
        },
        learning_goals=["Master machine learning", "Improve data visualization"],
        context={"learner_id": "alice_001"},
    )

    print("Skill Assessment Result:")
    print(json.dumps(json.loads(assessment_result), indent=2))

    # Demo 2: Curriculum Generation
    print("\n📚 Demo 2: Personalized Curriculum Generation")
    print("-" * 45)

    curriculum_result = await lxp_tool.execute(
        action="generate_curriculum",
        learner_profile={
            "name": "Alice Johnson",
            "role": "Data Analyst",
            "skill_levels": {
                "programming": {"current_level": 3, "target_level": 8},
                "data_analysis": {"current_level": 2, "target_level": 7},
                "machine_learning": {"current_level": 1, "target_level": 6},
            },
        },
        learning_goals=["Master machine learning", "Improve data visualization"],
        context={"learner_id": "alice_001"},
    )

    print("Generated Curriculum:")
    curriculum_data = json.loads(curriculum_result)
    for module in curriculum_data.get("modules", []):
        print(f"  • {module['title']} ({module['duration']}) - {module['difficulty']}")

    # Demo 3: Exercise Creation
    print("\n🎯 Demo 3: Interactive Exercise Creation")
    print("-" * 35)

    exercise_result = await lxp_tool.execute(
        action="create_exercise",
        context={
            "learner_id": "alice_001",
            "current_module": "Data Analysis Essentials",
        },
    )

    exercise_data = json.loads(exercise_result)
    print(f"Exercise: {exercise_data['title']}")
    print(f"Difficulty: {exercise_data['difficulty']}")
    print(f"Estimated Time: {exercise_data['estimated_time']}")
    print("Learning Objectives:")
    for objective in exercise_data["learning_objectives"]:
        print(f"  • {objective}")

    # Demo 4: Progress Tracking
    print("\n📈 Demo 4: Progress Tracking and Analysis")
    print("-" * 40)

    progress_result = await lxp_tool.execute(
        action="track_progress", context={"learner_id": "alice_001"}
    )

    progress_data = json.loads(progress_result)
    print(
        f"Overall Progress: {progress_data['overall_progress']['completion_percentage']}%"
    )
    print(
        f"Modules Completed: {progress_data['overall_progress']['modules_completed']}/{progress_data['overall_progress']['total_modules']}"
    )
    print("Recent Achievements:")
    for achievement in progress_data["achievements"][:3]:
        print(f"  • {achievement}")

    # Demo 5: Adaptive Learning Path Adjustment
    print("\n🔄 Demo 5: Adaptive Learning Path Adjustment")
    print("-" * 45)

    adjustment_result = await lxp_tool.execute(
        action="adjust_path", context={"learner_id": "alice_001"}
    )

    adjustment_data = json.loads(adjustment_result)
    print(f"Adjustment Reason: {adjustment_data['reason_for_adjustment']}")
    print("Path Adjustments:")
    for module, changes in adjustment_data["adjustments"].items():
        print(f"  • {module}: {changes}")

    return {
        "assessment": assessment_result,
        "curriculum": curriculum_result,
        "exercise": exercise_result,
        "progress": progress_result,
        "adjustment": adjustment_result,
    }


async def demo_craftedai_with_lxp():
    """Demonstrate how CraftedAI agent can use LXP capabilities"""

    print("\n🤖 Demo: CraftedAI Agent with LXP Integration")
    print("=" * 50)

    # Initialize CraftedAI agent (which now includes LXP tool)
    craftedai = CraftedAI()

    # Simulate a learning request
    learning_request = """
    I'm a data analyst with 2 years of experience. I want to learn machine learning
    to advance my career. I have some Python experience but need to improve my skills.
    Can you help me create a personalized learning plan and assess my current skills?
    """

    print(f"User Request: {learning_request}")
    print("\nCraftedAI Agent Response:")
    print("-" * 25)

    # Add the request to CraftedAI's memory
    craftedai.update_memory("user", learning_request)

    # Let CraftedAI think and respond
    await craftedai.think()

    # Show CraftedAI's response
    if craftedai.memory.messages:
        last_message = craftedai.memory.messages[-1]
        if last_message.role == "assistant":
            print(last_message.content)

    return craftedai


async def demo_lxp_agent():
    """Demonstrate the standalone LXP agent"""

    print("\n🎓 Demo: Standalone LXP Agent")
    print("=" * 35)

    # Initialize LXP agent
    lxp_agent = LXPAgent()

    # Simulate a learning session
    learning_session = """
    I want to learn Python programming for data science. I'm a complete beginner
    but motivated to learn. Can you assess my current skills and create a learning path?
    """

    print(f"Learner Request: {learning_session}")
    print("\nLXP Agent Processing:")
    print("-" * 25)

    # Add the request to LXP agent's memory
    lxp_agent.update_memory("user", learning_session)

    # Run the LXP agent for a few steps
    result = await lxp_agent.run(learning_session)

    print("LXP Agent Result:")
    print(result)

    # Show learner summary
    summary = lxp_agent.get_learner_summary()
    print("\nLearner Summary:")
    print(f"Total Steps: {summary['total_steps']}")
    print(f"Current Step: {summary['current_step']}")

    return lxp_agent


async def main():
    """Main demonstration function"""

    try:
        # Demo 1: LXP Tool functionality
        print("Starting LXP Tool Demonstrations...")
        tool_results = await demo_learning_scenario()

        # Demo 2: CraftedAI with LXP integration
        print("\nStarting CraftedAI + LXP Integration Demo...")
        craftedai_agent = await demo_craftedai_with_lxp()

        # Demo 3: Standalone LXP agent
        print("\nStarting Standalone LXP Agent Demo...")
        lxp_agent = await demo_lxp_agent()

        print("\n✅ All demonstrations completed successfully!")
        print("\n🎉 Integration Summary:")
        print("• OpenCraftedAI provides the general-purpose AI agent framework")
        print("• LXP Tool adds specialized learning capabilities to CraftedAI")
        print("• LXP Agent provides standalone learning experience management")
        print("• Both systems can work together or independently")

    except Exception as e:
        logger.error(f"Demo failed: {e}")
        print(f"❌ Demo failed: {e}")


if __name__ == "__main__":
    asyncio.run(main())
