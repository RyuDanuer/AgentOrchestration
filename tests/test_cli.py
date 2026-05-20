import pytest

from src.cli.main import cli


class TestCli:
    def test_deploy_missing_manifest_fails_before_progress_message(
        self, monkeypatch, capsys, tmp_path
    ):
        missing_manifest = tmp_path / "missing-agent.yaml"
        monkeypatch.setattr(
            "sys.argv", ["ao", "deploy", str(missing_manifest)]
        )

        with pytest.raises(SystemExit) as exc_info:
            cli()

        captured = capsys.readouterr()
        assert exc_info.value.code == 1
        assert f"manifest file not found: {missing_manifest}" in captured.err
        assert "Deploying agent from manifest" not in captured.out

    def test_deploy_existing_manifest_prints_progress_message(
        self, monkeypatch, capsys, tmp_path
    ):
        manifest = tmp_path / "agent.yaml"
        manifest.write_text("name: test-agent\n")
        monkeypatch.setattr("sys.argv", ["ao", "deploy", str(manifest)])

        cli()

        captured = capsys.readouterr()
        assert f"Deploying agent from manifest: {manifest}" in captured.out
        assert captured.err == ""
