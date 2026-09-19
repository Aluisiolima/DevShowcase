from http import HTTPStatus

from fastapi import APIRouter
from devshowcase.feedback.schema import FeedbackCreateSchema, FeedbackResponseSchema

from devshowcase.feedback.service import FeedbackService

feedback_router = APIRouter(prefix="/feedback", tags=["Feedback"])


@feedback_router.get("/", response_model=list[FeedbackResponseSchema])
async def get_feedbacks():
    return await FeedbackService.get_feedbacks()
