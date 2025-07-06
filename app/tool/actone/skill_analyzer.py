from typing import Any, Dict, List, Optional

from pydantic import Field

from app.tool.base import BaseTool, ToolResult


class SkillAnalyzer(BaseTool):
    """
    Skill analysis tool for evaluating skills and identifying gaps.

    Provides comprehensive skill analysis including:
    - Skill level assessment
    - Gap identification and severity calculation
    - Development timeline estimation
    - Training recommendations
    """

    name: str = "skill_analyzer"
    description: str = (
        "Analyze skills, identify gaps, and provide development recommendations"
    )

    parameters: dict = {
        "type": "object",
        "properties": {
            "current_skills": {
                "type": "array",
                "items": {"type": "object"},
                "description": "Current skills with levels and experience",
            },
            "required_skills": {
                "type": "array",
                "items": {"type": "object"},
                "description": "Required skills for target role/position",
            },
            "analysis_type": {
                "type": "string",
                "enum": ["individual", "team", "role"],
                "default": "individual",
                "description": "Type of skill analysis to perform",
            },
            "include_recommendations": {
                "type": "boolean",
                "default": True,
                "description": "Whether to include training recommendations",
            },
        },
        "required": ["current_skills", "required_skills"],
    }

    async def execute(self, **kwargs) -> str:
        """Analyze skills and identify gaps."""
        try:
            current_skills = kwargs.get("current_skills", [])
            required_skills = kwargs.get("required_skills", [])
            analysis_type = kwargs.get("analysis_type", "individual")
            include_recommendations = kwargs.get("include_recommendations", True)

            # Perform skill analysis
            analysis_result = self._analyze_skills(
                current_skills, required_skills, analysis_type, include_recommendations
            )

            return str(analysis_result)

        except Exception as e:
            return f"Skill analysis failed: {str(e)}"

    def _analyze_skills(
        self,
        current_skills: List[Dict],
        required_skills: List[Dict],
        analysis_type: str,
        include_recommendations: bool,
    ) -> Dict[str, Any]:
        """Analyze skills and identify gaps."""

        # Create skill mappings
        current_skill_map = {skill["skill"].lower(): skill for skill in current_skills}
        required_skill_map = {
            skill["skill"].lower(): skill for skill in required_skills
        }

        # Analyze gaps
        skill_gaps = []
        skill_matches = []
        missing_skills = []

        for req_skill_name, req_skill in required_skill_map.items():
            if req_skill_name in current_skill_map:
                current_skill = current_skill_map[req_skill_name]
                gap_analysis = self._calculate_skill_gap(current_skill, req_skill)

                if gap_analysis["has_gap"]:
                    skill_gaps.append(gap_analysis)
                else:
                    skill_matches.append(
                        {
                            "skill": req_skill_name,
                            "current_level": current_skill.get("level"),
                            "required_level": req_skill.get("level"),
                            "match_score": 1.0,
                        }
                    )
            else:
                missing_skills.append(
                    {
                        "skill": req_skill_name,
                        "required_level": req_skill.get("level"),
                        "importance": req_skill.get("importance", "medium"),
                        "gap_severity": "High",
                    }
                )

        # Calculate overall metrics
        total_required = len(required_skills)
        total_matched = len(skill_matches)
        total_gaps = len(skill_gaps) + len(missing_skills)

        overall_score = total_matched / total_required if total_required > 0 else 0

        # Generate recommendations
        recommendations = []
        if include_recommendations:
            recommendations = self._generate_skill_recommendations(
                skill_gaps, missing_skills, analysis_type
            )

        return {
            "analysis_type": analysis_type,
            "overall_score": round(overall_score, 3),
            "skill_matches": skill_matches,
            "skill_gaps": skill_gaps,
            "missing_skills": missing_skills,
            "summary": {
                "total_required_skills": total_required,
                "matched_skills": total_matched,
                "gap_skills": total_gaps,
                "completion_percentage": round(overall_score * 100, 1),
            },
            "recommendations": recommendations,
            "development_timeline": self._estimate_development_timeline(
                skill_gaps, missing_skills
            ),
            "analyzed_at": self._get_timestamp(),
        }

    def _calculate_skill_gap(
        self, current_skill: Dict, required_skill: Dict
    ) -> Dict[str, Any]:
        """Calculate gap between current and required skill levels."""
        level_hierarchy = {"beginner": 1, "intermediate": 2, "advanced": 3, "expert": 4}

        current_level = current_skill.get("level", "beginner").lower()
        required_level = required_skill.get("level", "intermediate").lower()

        current_score = level_hierarchy.get(current_level, 1)
        required_score = level_hierarchy.get(required_level, 2)

        gap_size = required_score - current_score

        if gap_size <= 0:
            return {
                "skill": current_skill.get("skill"),
                "current_level": current_level,
                "required_level": required_level,
                "gap_size": 0,
                "has_gap": False,
                "gap_severity": "None",
            }

        # Determine gap severity
        if gap_size >= 2:
            severity = "High"
        elif gap_size == 1:
            severity = "Medium"
        else:
            severity = "Low"

        # Estimate development time
        development_time = self._estimate_skill_development_time(
            gap_size, current_level
        )

        return {
            "skill": current_skill.get("skill"),
            "current_level": current_level,
            "required_level": required_level,
            "gap_size": gap_size,
            "has_gap": True,
            "gap_severity": severity,
            "development_time": development_time,
            "importance": required_skill.get("importance", "medium"),
        }

    def _estimate_skill_development_time(
        self, gap_size: int, current_level: str
    ) -> str:
        """Estimate time needed to develop skill to required level."""
        base_times = {
            "beginner": {"1": "3-6 months", "2": "6-12 months", "3": "12-18 months"},
            "intermediate": {"1": "2-4 months", "2": "4-8 months", "3": "8-12 months"},
            "advanced": {"1": "1-3 months", "2": "3-6 months", "3": "6-9 months"},
        }

        return base_times.get(current_level, {}).get(str(gap_size), "3-6 months")

    def _generate_skill_recommendations(
        self, skill_gaps: List[Dict], missing_skills: List[Dict], analysis_type: str
    ) -> List[str]:
        """Generate training and development recommendations."""
        recommendations = []

        # High priority gaps
        high_priority_gaps = [
            gap for gap in skill_gaps if gap.get("importance") == "high"
        ]
        high_priority_missing = [
            skill for skill in missing_skills if skill.get("importance") == "high"
        ]

        if high_priority_gaps or high_priority_missing:
            recommendations.append("Focus on high-priority skills first")

        # Specific recommendations
        for gap in skill_gaps[:3]:  # Top 3 gaps
            skill_name = gap.get("skill", "Unknown Skill")
            recommendations.append(
                f"Develop {skill_name} from {gap.get('current_level')} to {gap.get('required_level')}"
            )

        for missing in missing_skills[:3]:  # Top 3 missing
            skill_name = missing.get("skill", "Unknown Skill")
            recommendations.append(
                f"Acquire {skill_name} at {missing.get('required_level')} level"
            )

        # General recommendations
        if analysis_type == "individual":
            recommendations.extend(
                [
                    "Seek mentorship from senior team members",
                    "Participate in relevant training programs",
                    "Practice skills through hands-on projects",
                ]
            )
        elif analysis_type == "team":
            recommendations.extend(
                [
                    "Implement cross-training programs",
                    "Consider hiring for critical skill gaps",
                    "Establish knowledge sharing sessions",
                ]
            )

        return recommendations

    def _estimate_development_timeline(
        self, skill_gaps: List[Dict], missing_skills: List[Dict]
    ) -> Dict[str, Any]:
        """Estimate overall development timeline."""
        if not skill_gaps and not missing_skills:
            return {"timeline": "No development needed", "estimated_months": 0}

        # Calculate total development time
        total_months = 0
        critical_skills = 0

        for gap in skill_gaps:
            if gap.get("importance") == "high":
                critical_skills += 1
                # Add time for high-priority skills
                total_months += 3

        for missing in missing_skills:
            if missing.get("importance") == "high":
                critical_skills += 1
                total_months += 6

        # Add time for other skills
        other_skills = len(skill_gaps) + len(missing_skills) - critical_skills
        total_months += other_skills * 2

        # Estimate timeline
        if total_months <= 3:
            timeline = "Short-term (1-3 months)"
        elif total_months <= 6:
            timeline = "Medium-term (3-6 months)"
        elif total_months <= 12:
            timeline = "Long-term (6-12 months)"
        else:
            timeline = "Extended (12+ months)"

        return {
            "timeline": timeline,
            "estimated_months": total_months,
            "critical_skills_count": critical_skills,
        }

    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime

        return datetime.now().isoformat()
