import app
import pytest

def test_hello():
    response = app.hello()

    assert response