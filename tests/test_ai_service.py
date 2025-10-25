import pytest

import ai_service


class DummyChoice:
    def __init__(self, content):
        class Msg:
            def __init__(self, c):
                self.content = c
        self.message = Msg(content)


class DummyResponse:
    def __init__(self, text):
        self.choices = [DummyChoice(text)]


class DummyChat:
    def __init__(self, response_text):
        self._response_text = response_text

    class completions:
        pass


def test_create_simple_tasks_no_key(monkeypatch):
    # Simulate no API key set on client
    monkeypatch.setattr(ai_service.client, 'api_key', None)
    res = ai_service.create_simple_tasks("Do something complex")
    assert isinstance(res, list)
    assert res[0].startswith("Error: OpenAI")


def test_create_simple_tasks_success(monkeypatch):
    # Mock client.chat.completions.create to return a predictable response
    def fake_create(**kwargs):
        # Return a string with dash-prefixed subtasks
        return DummyResponse("- Step one\n- Step two\n- Step three")

    class FakeChat:
        def __init__(self):
            self.completions = type('C', (), {'create': staticmethod(fake_create)})()

    monkeypatch.setattr(ai_service, 'client', type('C', (), {'api_key': 'ok', 'chat': FakeChat()})())

    subtasks = ai_service.create_simple_tasks("Some complex task")
    assert subtasks == ["Step one", "Step two", "Step three"]
