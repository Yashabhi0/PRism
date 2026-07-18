"""
FastAPI dependency injection — reusable service instances.

Usage in route handlers:
    from dependencies import get_analysis_service
    async def my_route(service: AnalysisService = Depends(get_analysis_service)):
        ...
"""

from __future__ import annotations

from functools import lru_cache

from services.analysis_service import AnalysisService
from services.github_service import GitHubService
from services.rag_service import RAGService


@lru_cache(maxsize=1)
def get_analysis_service() -> AnalysisService:
    return AnalysisService()


@lru_cache(maxsize=1)
def get_github_service() -> GitHubService:
    return GitHubService()


@lru_cache(maxsize=1)
def get_rag_service() -> RAGService:
    return RAGService()
