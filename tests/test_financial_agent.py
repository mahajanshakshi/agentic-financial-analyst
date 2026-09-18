import pytest
from app.agents.financial_Agent import Ask_Financial_Agent


@pytest.mark.asyncio
async def test_financial_agent_without_tool():
    answer, tool, status = await Ask_Financial_Agent(
        "What is 10% of 100?"
    )

    assert answer is not None
    assert tool is None
    assert status == "no tool required"
