from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, timezone

class UserModel(BaseModel):
    id: int = Field(..., ge=1, description="Unique identifier for the user")
    name: str = Field(..., min_length=2, max_length=50, description="Full name of the user")
    email: EmailStr = Field(..., description="Valid email address")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Timestamp of user creation")
    is_active: bool = Field(default=True, description="Status of the user account")

    class Config:
        orm_mode = True
