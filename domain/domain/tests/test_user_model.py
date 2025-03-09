import pytest
from datetime import datetime, timezone
from domain.feature1.model import UserModel
from pydantic import ValidationError


def test_valid_user():
    """Test creating a valid user instance."""
    user = UserModel(id=1, name="John Doe", email="john@example.com")

    assert user.id == 1
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    assert user.is_active is True
    assert isinstance(user.created_at, datetime)
    assert user.created_at.tzinfo == timezone.utc  # Ensure timezone-awareness


def test_invalid_user_id():
    """Test validation failure when using an invalid user ID."""
    with pytest.raises(ValidationError):
        UserModel(id=0, name="John Doe", email="john@example.com")  # ID must be >= 1


def test_invalid_email():
    """Test validation failure when using an invalid email."""
    with pytest.raises(ValidationError):
        UserModel(id=1, name="John Doe", email="not-an-email")


def test_invalid_name():
    """Test validation failure when using a short name."""
    with pytest.raises(ValidationError):
        UserModel(id=1, name="J", email="john@example.com")  # Name too short


def test_custom_created_at():
    """Test overriding the default timestamp."""
    custom_time = datetime(2023, 1, 1, tzinfo=timezone.utc)
    user = UserModel(id=2, name="Jane Doe", email="jane@example.com", created_at=custom_time)

    assert user.created_at == custom_time
