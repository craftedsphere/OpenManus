import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import Field

from app.agent.toolcall import ToolCallAgent
from app.config import config
from app.logger import logger
from app.tool import Terminate, ToolCollection
from app.tool.ask_human import AskHuman
from app.tool.python_execute import PythonExecute


class LXPAgent(ToolCallAgent):
    """
    Learning Experience Platform Agent that integrates Autonomous LXP capabilities
    into OpenCraftedAI's agent framework.

    This agent provides personalized learning experiences, skill assessment,
    curriculum generation, and adaptive learning paths.
    """

    name: str = "LXP_Agent"
    description: str = (
        "An intelligent learning agent that provides personalized education experiences, skill assessment, and adaptive learning paths"
    )

    system_prompt: str = """You are an intelligent Learning Experience Platform (LXP) agent designed to provide personalized learning experiences.

Your capabilities include:
- Curriculum generation and personalization
- Skill gap analysis and assessment
- Adaptive learning path creation
- Real-time feedback and mentoring
- Learning progress tracking and optimization

You work within the OpenCraftedAI framework and can use various tools to:
- Execute Python code for data analysis and learning exercises
- Generate and modify learning content
- Track learner progress and performance
- Provide personalized recommendations
- Create interactive learning experiences

Always focus on creating engaging, effective, and personalized learning experiences that adapt to each learner's needs, preferences, and progress."""

    next_step_prompt: str = """Based on the current conversation and learner context, determine the next best action:

1. If this is a new learner or learning request:
   - Assess their current skills and learning goals
   - Generate a personalized learning path
   - Provide initial guidance and resources

2. If the learner is in progress:
   - Review their current progress and performance
   - Provide targeted feedback and recommendations
   - Adjust the learning path if needed
   - Offer next steps or exercises

3. If the learner needs assessment:
   - Create or administer skill assessments
   - Analyze results and provide insights
   - Update their learning profile

4. If the learner needs content or resources:
   - Generate or curate relevant learning materials
   - Create interactive exercises or projects
   - Provide explanations and examples

Consider the learner's:
- Current skill level and background
- Learning goals and objectives
- Preferred learning style
- Available time and resources
- Previous progress and performance

Choose the most appropriate tool or action to advance their learning journey."""

    max_observe: int = 15000
    max_steps: int = 25

    # Learner context and state
    learner_profile: Dict[str, Any] = Field(default_factory=dict)
    current_learning_path: Dict[str, Any] = Field(default_factory=dict)
    learning_progress: Dict[str, Any] = Field(default_factory=dict)

    # Add LXP-specific tools to the tool collection
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            PythonExecute(),
            AskHuman(),
            Terminate(),
        )
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._initialize_lxp_components()

    def _initialize_lxp_components(self):
        """Initialize LXP-specific components and connections"""
        try:
            # Try to import LXP components if available
            lxp_path = (
                Path(__file__).parent.parent.parent.parent
                / "autonomous_lxp_complete"
                / "autonomous_lxp_backend"
                / "src"
            )
            if lxp_path.exists():
                sys.path.insert(0, str(lxp_path))
                logger.info("LXP components found and initialized")
            else:
                logger.warning("LXP components not found - running in standalone mode")
        except Exception as e:
            logger.warning(f"Could not initialize LXP components: {e}")

    async def step(self) -> str:
        """Execute a single step in the LXP agent's workflow"""
        try:
            # Analyze current context and learner state
            context_analysis = await self._analyze_learner_context()

            # Determine next action based on context
            action = await self._determine_next_action(context_analysis)

            # Execute the action
            result = await self._execute_action(action)

            # Update learner state
            await self._update_learner_state(action, result)

            return f"LXP Step: {action['type']} - {result}"

        except Exception as e:
            logger.error(f"Error in LXP step: {e}")
            return f"Error in LXP step: {str(e)}"

    async def _analyze_learner_context(self) -> Dict[str, Any]:
        """Analyze current learner context and state"""
        # Get recent messages to understand current situation
        recent_messages = self.memory.messages[-5:] if self.memory.messages else []

        context = {
            "learner_profile": self.learner_profile,
            "current_learning_path": self.current_learning_path,
            "learning_progress": self.learning_progress,
            "recent_interaction": (
                recent_messages[-1].content if recent_messages else ""
            ),
            "interaction_history": [msg.content for msg in recent_messages],
            "current_step": self.current_step,
            "max_steps": self.max_steps,
        }

        return context

    async def _determine_next_action(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Determine the next action based on current context"""
        # Use the LLM to determine the best next action
        action_prompt = f"""
        Based on the current learner context, determine the best next action:

        Context: {json.dumps(context, indent=2)}

        Available actions:
        1. assess_skills - Assess learner's current skills and knowledge
        2. generate_curriculum - Create a personalized learning path
        3. provide_feedback - Give feedback on current progress
        4. create_exercise - Generate a learning exercise or project
        5. explain_concept - Explain a concept or topic
        6. track_progress - Update and analyze learning progress
        7. adjust_path - Modify the learning path based on performance

        Return a JSON object with:
        - "type": The action type
        - "description": Brief description of what to do
        - "parameters": Any specific parameters for the action
        """

        response = await self.llm.ask([{"role": "user", "content": action_prompt}])

        try:
            action = json.loads(response)
            return action
        except json.JSONDecodeError:
            # Fallback to default action
            return {
                "type": "assess_skills",
                "description": "Assess learner's current skills",
                "parameters": {},
            }

    async def _execute_action(self, action: Dict[str, Any]) -> str:
        """Execute the determined action"""
        action_type = action.get("type", "")

        if action_type == "assess_skills":
            return await self._assess_learner_skills()
        elif action_type == "generate_curriculum":
            return await self._generate_curriculum()
        elif action_type == "provide_feedback":
            return await self._provide_feedback()
        elif action_type == "create_exercise":
            return await self._create_exercise()
        elif action_type == "explain_concept":
            return await self._explain_concept()
        elif action_type == "track_progress":
            return await self._track_progress()
        elif action_type == "adjust_path":
            return await self._adjust_learning_path()
        else:
            return f"Unknown action type: {action_type}"

    async def _assess_learner_skills(self) -> str:
        """Assess the learner's current skills and knowledge"""
        assessment_prompt = """
        Create a comprehensive skill assessment for the learner.
        Consider their background, goals, and current level.

        Generate:
        1. A skill assessment questionnaire
        2. Practical exercises to evaluate their knowledge
        3. Recommendations for skill development
        """

        response = await self.llm.ask([{"role": "user", "content": assessment_prompt}])

        # Update learner profile with assessment results
        self.learner_profile["last_assessment"] = {
            "timestamp": asyncio.get_event_loop().time(),
            "assessment": response,
        }

        return f"Skill assessment completed. Results: {response[:200]}..."

    async def _generate_curriculum(self) -> str:
        """Generate a personalized learning curriculum"""
        curriculum_prompt = f"""
        Generate a personalized learning curriculum based on:
        - Learner profile: {json.dumps(self.learner_profile, indent=2)}
        - Learning goals: {self.learner_profile.get('goals', 'Not specified')}
        - Current skills: {json.dumps(self.learner_profile.get('skills', {}), indent=2)}

        Create a structured curriculum with:
        1. Learning objectives
        2. Module breakdown
        3. Timeline and milestones
        4. Assessment criteria
        5. Resources and materials
        """

        response = await self.llm.ask([{"role": "user", "content": curriculum_prompt}])

        # Parse and store the curriculum
        try:
            curriculum = json.loads(response)
            self.current_learning_path = curriculum
        except json.JSONDecodeError:
            self.current_learning_path = {"curriculum": response}

        return f"Personalized curriculum generated. Modules: {len(self.current_learning_path.get('modules', []))}"

    async def _provide_feedback(self) -> str:
        """Provide personalized feedback on learner progress"""
        feedback_prompt = f"""
        Provide personalized feedback based on:
        - Current progress: {json.dumps(self.learning_progress, indent=2)}
        - Learning path: {json.dumps(self.current_learning_path, indent=2)}
        - Recent performance: {self.learner_profile.get('recent_performance', 'Not available')}

        Give constructive, actionable feedback that:
        1. Acknowledges achievements
        2. Identifies areas for improvement
        3. Provides specific next steps
        4. Maintains motivation and engagement
        """

        response = await self.llm.ask([{"role": "user", "content": feedback_prompt}])
        return f"Feedback provided: {response[:200]}..."

    async def _create_exercise(self) -> str:
        """Create a learning exercise or project"""
        exercise_prompt = f"""
        Create an engaging learning exercise based on:
        - Current learning objectives: {self.current_learning_path.get('current_objective', 'Not specified')}
        - Learner's skill level: {self.learner_profile.get('skill_level', 'Intermediate')}
        - Preferred learning style: {self.learner_profile.get('learning_style', 'Mixed')}

        Design an exercise that:
        1. Reinforces current concepts
        2. Provides hands-on practice
        3. Is appropriately challenging
        4. Includes clear instructions
        5. Has measurable outcomes
        """

        response = await self.llm.ask([{"role": "user", "content": exercise_prompt}])
        return f"Exercise created: {response[:200]}..."

    async def _explain_concept(self) -> str:
        """Explain a concept or topic"""
        concept_prompt = f"""
        Explain the current learning concept in a clear, engaging way.
        Consider the learner's:
        - Background knowledge: {self.learner_profile.get('background', 'Not specified')}
        - Learning preferences: {self.learner_profile.get('learning_preferences', 'Not specified')}
        - Current understanding level: {self.learning_progress.get('understanding_level', 'Beginner')}

        Provide:
        1. Clear, simple explanations
        2. Relevant examples
        3. Visual aids or analogies
        4. Common misconceptions to avoid
        5. Practice opportunities
        """

        response = await self.llm.ask([{"role": "user", "content": concept_prompt}])
        return f"Concept explained: {response[:200]}..."

    async def _track_progress(self) -> str:
        """Track and analyze learning progress"""
        progress_prompt = f"""
        Analyze the learner's current progress:
        - Learning path: {json.dumps(self.current_learning_path, indent=2)}
        - Progress data: {json.dumps(self.learning_progress, indent=2)}
        - Recent activities: {self.learner_profile.get('recent_activities', [])}

        Provide:
        1. Progress summary
        2. Achievement highlights
        3. Areas needing attention
        4. Recommendations for next steps
        5. Timeline adjustments if needed
        """

        response = await self.llm.ask([{"role": "user", "content": progress_prompt}])

        # Update progress tracking
        self.learning_progress["last_analysis"] = {
            "timestamp": asyncio.get_event_loop().time(),
            "analysis": response,
        }

        return f"Progress tracked: {response[:200]}..."

    async def _adjust_learning_path(self) -> str:
        """Adjust the learning path based on performance and feedback"""
        adjustment_prompt = f"""
        Analyze and adjust the learning path based on:
        - Current performance: {json.dumps(self.learning_progress, indent=2)}
        - Learner feedback: {self.learner_profile.get('feedback', 'Not available')}
        - Progress rate: {self.learning_progress.get('progress_rate', 'Normal')}

        Consider adjustments for:
        1. Difficulty level
        2. Learning pace
        3. Content focus
        4. Assessment frequency
        5. Resource recommendations
        """

        response = await self.llm.ask([{"role": "user", "content": adjustment_prompt}])

        # Update the learning path
        try:
            adjustments = json.loads(response)
            self.current_learning_path.update(adjustments)
        except json.JSONDecodeError:
            self.current_learning_path["adjustments"] = response

        return f"Learning path adjusted: {response[:200]}..."

    async def _update_learner_state(self, action: Dict[str, Any], result: str):
        """Update learner state based on action and result"""
        # Update learning progress
        self.learning_progress["last_action"] = {
            "timestamp": asyncio.get_event_loop().time(),
            "action": action,
            "result": result,
        }

        # Update step counter
        self.learning_progress["total_steps"] = (
            self.learning_progress.get("total_steps", 0) + 1
        )

    def get_learner_summary(self) -> Dict[str, Any]:
        """Get a summary of the learner's current state"""
        return {
            "profile": self.learner_profile,
            "learning_path": self.current_learning_path,
            "progress": self.learning_progress,
            "total_steps": self.learning_progress.get("total_steps", 0),
            "current_step": self.current_step,
        }
