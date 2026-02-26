from pydantic import BaseModel, field_validator, Field
from typing import List, Optional


class User3(BaseModel):
    name: str
    age: int


class Feedback3(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Имя от 2 до 50 символов")
    message: str = Field(..., min_length=10, max_length=500, description="Сообщение от 10 до 500 символов")

    @field_validator('message')
    @classmethod
    def validate_no_forbidden_words(cls, v: str) -> str:
        forbidden_words = ['кринж', 'рофл', 'вайб']

        message_lower = v.lower()

        for word in forbidden_words:
            if word in message_lower:
                raise ValueError('Использование недопустимых слов')

        return v