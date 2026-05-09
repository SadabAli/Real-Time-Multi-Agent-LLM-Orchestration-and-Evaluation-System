import subprocess
import tempfile
import time

# This satisfies:

# real code execution
# stdout
# stderr
# exit code
# timeout handling

def python_tool(code: str):

    start = time.time()

    if not code.strip():

        return {
            "status": "malformed_input",
            "tool_name": "python_tool",
            "result": None,
            "latency": 0,
            "error": "empty code"
        }

    try:

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False
        ) as f:

            f.write(code)

            temp_path = f.name

        result = subprocess.run(
            ["python", temp_path],
            capture_output=True,
            text=True,
            timeout=5
        )

        latency = round(time.time() - start, 2)

        return {
            "status": "success",
            "tool_name": "python_tool",
            "result": {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode
            },
            "latency": latency,
            "error": None
        }

    except subprocess.TimeoutExpired:

        return {
            "status": "timeout",
            "tool_name": "python_tool",
            "result": None,
            "latency": 5,
            "error": "execution timeout"
        }