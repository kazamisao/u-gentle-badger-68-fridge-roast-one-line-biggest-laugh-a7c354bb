"""Local gate test for the Fridge Roast entry.

Mirrors the competition's sealed gate: /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only white space, on a single line.
Run: python3 -m pytest test_entry.py -v  (or: python3 test_entry.py)
"""

import os
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent


def run_entry(out_dir: pathlib.Path) -> pathlib.Path:
    env = dict(os.environ, MAKEFUN_OUTPUT_DIR=str(out_dir))
    proc = subprocess.run(
        [sys.executable, str(HERE / "main.py")],
        cwd=HERE,
        env=env,
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert proc.returncode == 0, f"main.py exited {proc.returncode}: {proc.stderr}"
    return out_dir / "entry.txt"


def test_entry_is_valid_one_line():
    with tempfile.TemporaryDirectory() as tmp:
        entry = run_entry(pathlib.Path(tmp))
        assert entry.exists(), "entry.txt was not written"
        raw = entry.read_bytes()
        text = raw.decode("utf-8")  # raises if not valid UTF-8
        assert 1 <= len(text) <= 200, f"length {len(text)} outside 1-200"
        assert text.strip(), "entry is only white space"
        assert "\n" not in text and "\r" not in text, "entry is not a single line"
        assert text == text.strip(), "entry has leading/trailing whitespace"


def test_entry_is_deterministic():
    with tempfile.TemporaryDirectory() as tmp:
        first = run_entry(pathlib.Path(tmp)).read_bytes()
        second = run_entry(pathlib.Path(tmp)).read_bytes()
        assert first == second, "two runs wrote different bytes"


if __name__ == "__main__":
    test_entry_is_valid_one_line()
    test_entry_is_deterministic()
    print("all tests passed")
