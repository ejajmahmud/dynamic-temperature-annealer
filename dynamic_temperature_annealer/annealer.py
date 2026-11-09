"""Core Dynamic Temperature Annealer implementation."""
import re
from typing import Dict, Optional, Any


class SamplingParams:
    def __init__(self, temperature: float, top_p: float, task_mode: str):
        self.temperature = temperature
        self.top_p = top_p
        self.task_mode = task_mode

    def to_dict(self) -> Dict[str, Any]:
        return {
            "temperature": round(self.temperature, 2),
            "top_p": round(self.top_p, 2),
            "task_mode": self.task_mode
        }


class TemperatureAnnealer:
    def __init__(self):
        self.code_keywords = re.compile(r"(\bdef\b|\bclass\b|\bjson\b|\bSELECT\b|\bINSERT\b|\bfunction\b|\bimport\b|```)", re.IGNORECASE)
        self.creative_keywords = re.compile(r"(\bbrainstorm\b|\bcreative\b|\bideate\b|\bstory\b|\bexplore\b)", re.IGNORECASE)

    def recommend_params(self, prompt: str) -> SamplingParams:
        # Check for code or structured data cues
        if self.code_keywords.search(prompt):
            # Strict deterministic mode
            return SamplingParams(temperature=0.1, top_p=0.95, task_mode="code_structured")
        elif self.creative_keywords.search(prompt):
            # Creative exploratory mode
            return SamplingParams(temperature=0.85, top_p=0.98, task_mode="creative_ideation")
        else:
            # Balanced general reasoning
            return SamplingParams(temperature=0.5, top_p=0.90, task_mode="balanced_reasoning")

    def anneal_step(self, initial_temp: float, step: int, max_steps: int = 50) -> float:
        # Linear cooldown as steps progress
        progress = min(1.0, step / max(1, max_steps))
        return max(0.05, initial_temp * (1.0 - (0.5 * progress)))
