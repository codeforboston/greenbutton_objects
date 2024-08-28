"""Nox sessions."""

import nox

package = "greenbutton_objects"
python_versions = ["3.12", "3.11", "3.10", "3.9"]
nox.needs_version = ">= 2024.4.15"
nox.options.sessions = (
    "safety",
    "mypy",
    "tests",
)


@nox.session(python=python_versions[0])
def safety(session) -> None:
    """Scan dependencies for insecure packages."""
    session.install(".[dev]")
    session.install("safety")
    session.run("safety", "check", "--full-report")


@nox.session(python=python_versions)
def mypy(session) -> None:
    """Type-check using mypy."""
    args = session.posargs or ["src"]
    session.install(".[dev]")
    session.run("mypy", *args)


@nox.session(python=python_versions)
def tests(session) -> None:
    """Run the test suite."""
    session.install(".[dev]")
    session.run("coverage", "run", "--source=src", "--parallel", "-m", "pytest", *session.posargs)
