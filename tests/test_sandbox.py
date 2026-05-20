from src.agent import AgentSandbox, AgentStatus
from src.agent.sandbox import ResourceLimits
import src.agent.sandbox as sandbox_module


class TestAgentSandbox:
    def test_agent_status_is_exported_from_agent_package(self):
        assert AgentStatus.RUNNING.value == "running"

    def test_apply_limits_is_noop_without_resource_module(self, monkeypatch, tmp_path):
        monkeypatch.setattr(sandbox_module, "resource", None)
        sandbox = AgentSandbox(base_path=str(tmp_path))

        sandbox.apply_limits("agent-1", ResourceLimits())
