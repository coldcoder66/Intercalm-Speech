import pytest
from unittest.mock import MagicMock, patch
from fastapi import Request
from routers.google_auth import get_current_user

@pytest.fixture
def mock_request_with_user_id():
    mock_request = MagicMock(spec=Request)
    mock_request.session = {'user_id': 123}
    return mock_request

@pytest.fixture
def mock_request_without_user_id():
    mock_request = MagicMock(spec=Request)
    mock_request.session = {}
    return mock_request

@patch("routers.google_auth.Session")
@patch("routers.google_auth.User")
def test_get_current_user_returns_user(mock_user, mock_session, mock_request_with_user_id):
    # Arrange
    user_instance = MagicMock()
    mock_session.begin.return_value.__enter__.return_value = mock_session
    mock_session.query.return_value.filter.return_value.first.return_value = user_instance

    # Act
    result = get_current_user(mock_request_with_user_id)

    # Assert
    assert result == user_instance
    mock_session.query.assert_called_once_with(mock_user)
    mock_session.query.return_value.filter.assert_called_once()
    mock_session.query.return_value.filter.return_value.first.assert_called_once()

def test_get_current_user_returns_none_if_no_user_id(mock_request_without_user_id):
    result = get_current_user(mock_request_without_user_id)
    assert result is None