from typing import Any, Dict, List, Optional

from pydantic import Field

from app.tool.base import BaseTool, ToolResult


class JobMatcher(BaseTool):
    """
    Job matching tool for comparing candidate skills to job requirements.

    Calculates fit scores, identifies skill gaps, and provides recommendations
    for candidate-job matching.
    """

    name: str = "job_matcher"
    description: str = (
        "Match candidate skills to job requirements and calculate fit scores"
    )

    parameters: dict = {
        "type": "object",
        "properties": {
            "candidate_skills": {
                "type": "array",
                "items": {"type": "object"},
                "description": "List of candidate skills with levels and experience",
            },
            "job_requirements": {
                "type": "array",
                "items": {"type": "object"},
                "description": "List of job requirements with importance levels",
            },
            "candidate_experience": {
                "type": "array",
                "items": {"type": "object"},
                "description": "Candidate work experience history",
            },
            "job_level": {
                "type": "string",
                "enum": ["entry", "mid", "senior", "lead", "executive"],
                "description": "Target job level",
            },
        },
        "required": ["candidate_skills", "job_requirements"],
    }

    async def execute(self, **kwargs) -> str:
        """Match candidate to job requirements and calculate fit score."""
        try:
            candidate_skills = kwargs.get("candidate_skills", [])
            job_requirements = kwargs.get("job_requirements", [])
            candidate_experience = kwargs.get("candidate_experience", [])
            job_level = kwargs.get("job_level", "mid")

            # Calculate match results
            match_result = self._calculate_job_match(
                candidate_skills, job_requirements, candidate_experience, job_level
            )

            # Return formatted string
            fit_score = match_result["fit_score"]
            skill_matches = (
                ", ".join([skill["skill"] for skill in match_result["skill_matches"]])
                if match_result["skill_matches"]
                else "None"
            )
            missing_skills = (
                ", ".join([skill["skill"] for skill in match_result["missing_skills"]])
                if match_result["missing_skills"]
                else "None"
            )

            return f"Job matching completed. Fit Score: {fit_score}, Matched Skills: {skill_matches}, Missing Skills: {missing_skills}"

        except Exception as e:
            return f"Failed to match job requirements: {str(e)}"

    def _calculate_job_match(
        self,
        candidate_skills: List[Dict],
        job_requirements: List[Dict],
        candidate_experience: List[Dict],
        job_level: str,
    ) -> Dict[str, Any]:
        """Calculate job match score and analysis."""

        # Placeholder implementation - would use ML models for skill matching
        skill_matches = []
        missing_skills = []
        fit_score = 0.0

        # Create skill mapping for comparison
        candidate_skill_map = {
            skill["skill"].lower(): skill for skill in candidate_skills
        }

        for requirement in job_requirements:
            req_skill = requirement["skill"].lower()
            req_level = requirement.get("level", "intermediate")
            req_importance = requirement.get("importance", "medium")

            if req_skill in candidate_skill_map:
                candidate_skill = candidate_skill_map[req_skill]
                skill_level = candidate_skill.get("level", "intermediate")

                # Calculate skill match score
                level_score = self._calculate_level_match(skill_level, req_level)
                experience_bonus = min(candidate_skill.get("years", 0) / 5, 0.2)

                match_score = level_score + experience_bonus
                skill_matches.append(
                    {
                        "skill": req_skill,
                        "required_level": req_level,
                        "candidate_level": skill_level,
                        "match_score": match_score,
                        "importance": req_importance,
                    }
                )

                # Weight by importance
                if req_importance == "high":
                    fit_score += match_score * 0.4
                elif req_importance == "medium":
                    fit_score += match_score * 0.3
                else:
                    fit_score += match_score * 0.2
            else:
                missing_skills.append(
                    {
                        "skill": req_skill,
                        "required_level": req_level,
                        "importance": req_importance,
                    }
                )

        # Normalize fit score
        total_requirements = len(job_requirements)
        if total_requirements > 0:
            fit_score = fit_score / total_requirements

        # Generate recommendations
        recommendations = self._generate_recommendations(
            skill_matches, missing_skills, fit_score, job_level
        )

        return {
            "fit_score": round(fit_score, 3),
            "skill_matches": skill_matches,
            "missing_skills": missing_skills,
            "recommendations": recommendations,
            "experience_analysis": self._analyze_experience(
                candidate_experience, job_level
            ),
            "overall_assessment": self._get_overall_assessment(fit_score),
            "matched_at": self._get_timestamp(),
        }

    def _calculate_level_match(
        self, candidate_level: str, required_level: str
    ) -> float:
        """Calculate skill level match score."""
        level_hierarchy = {"beginner": 1, "intermediate": 2, "advanced": 3, "expert": 4}

        candidate_score = level_hierarchy.get(candidate_level.lower(), 1)
        required_score = level_hierarchy.get(required_level.lower(), 2)

        if candidate_score >= required_score:
            return 1.0
        elif candidate_score >= required_score - 1:
            return 0.7
        else:
            return 0.3

    def _generate_recommendations(
        self,
        skill_matches: List[Dict],
        missing_skills: List[Dict],
        fit_score: float,
        job_level: str,
    ) -> List[str]:
        """Generate recommendations based on match analysis."""
        recommendations = []

        if fit_score >= 0.8:
            recommendations.append("Strong candidate match - recommend for interview")
        elif fit_score >= 0.6:
            recommendations.append("Good potential - consider with training plan")
        else:
            recommendations.append("Significant skill gaps - may not be suitable")

        # High importance missing skills
        critical_missing = [
            skill for skill in missing_skills if skill["importance"] == "high"
        ]
        if critical_missing:
            recommendations.append(
                f"Critical missing skills: {', '.join([s['skill'] for s in critical_missing])}"
            )

        # Training recommendations
        if missing_skills:
            recommendations.append("Consider targeted training for missing skills")

        # Level-specific recommendations
        if job_level == "senior" and fit_score < 0.7:
            recommendations.append("May need more senior-level experience")
        elif job_level == "entry" and fit_score > 0.9:
            recommendations.append("Overqualified - consider more senior role")

        return recommendations

    def _analyze_experience(
        self, experience: List[Dict], job_level: str
    ) -> Dict[str, Any]:
        """Analyze candidate experience relative to job level."""
        if not experience:
            return {
                "years_total": 0,
                "relevant_experience": 0,
                "assessment": "No experience listed",
            }

        total_years = sum(exp.get("years", 0) for exp in experience)

        level_requirements = {
            "entry": {"min_years": 0, "max_years": 2},
            "mid": {"min_years": 2, "max_years": 5},
            "senior": {"min_years": 5, "max_years": 8},
            "lead": {"min_years": 8, "max_years": 12},
            "executive": {"min_years": 12, "max_years": 20},
        }

        req = level_requirements.get(job_level, {"min_years": 0, "max_years": 5})

        if total_years < req["min_years"]:
            assessment = "Underqualified for experience level"
        elif total_years > req["max_years"]:
            assessment = "Overqualified for experience level"
        else:
            assessment = "Appropriate experience level"

        return {
            "years_total": total_years,
            "relevant_experience": total_years,
            "assessment": assessment,
            "level_appropriate": req["min_years"] <= total_years <= req["max_years"],
        }

    def _get_overall_assessment(self, fit_score: float) -> str:
        """Get overall assessment based on fit score."""
        if fit_score >= 0.9:
            return "Excellent Match"
        elif fit_score >= 0.8:
            return "Strong Match"
        elif fit_score >= 0.7:
            return "Good Match"
        elif fit_score >= 0.6:
            return "Moderate Match"
        elif fit_score >= 0.5:
            return "Weak Match"
        else:
            return "Poor Match"

    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime

        return datetime.now().isoformat()
