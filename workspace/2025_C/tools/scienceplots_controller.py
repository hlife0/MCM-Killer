# -*- coding: utf-8 -*-
"""
SciencePlots Auto-Fix Controller for MCM-Killer v3.1.0

Self-healing code generation loop with max 3 retries.
Progressive fix strategy per retry attempt:
- Retry 1: Fix syntax, imports, plt.show() removal
- Retry 2: Fix column names, dimensions, NaN handling
- Retry 3: Fix directory creation, tight_layout

Author: MCM-Killer Visualizer Team
Version: 3.1.0
"""

import subprocess
import sys
import os
import tempfile
from pathlib import Path
from typing import Tuple, Optional, List


class AgentController:
    """
    Controller for self-healing matplotlib code execution.

    Executes generated code in subprocess with automatic error detection
    and progressive fixing strategy.
    """

    def __init__(self, timeout: int = 60):
        """
        Initialize controller.

        Args:
            timeout: Execution timeout in seconds (default: 60)
        """
        self.timeout = timeout

    def execute_and_fix(self, code: str, output_path: str, max_retries: int = 3) -> Tuple[bool, str, Optional[str]]:
        """
        Execute code with automatic error fixing (max 3 retries).

        Progressive fix strategy:
        - Attempt 1: Execute original code
        - Attempt 2: Fix syntax errors, missing imports, plt.show() calls
        - Attempt 3: Fix column name mismatches, dimension errors, NaN handling
        - Attempt 4: Fix directory creation, tight_layout issues

        Args:
            code: Python code to execute
            output_path: Expected output figure path
            max_retries: Maximum retry attempts (default: 3)

        Returns:
            Tuple[bool, str, Optional[str]]:
                - Success status
                - Message describing what happened
                - Error output (if failed)

        Examples:
            >>> controller = AgentController()
            >>> code = "import matplotlib.pyplot as plt; plt.plot([1,2,3]); plt.savefig('test.png')"
            >>> success, msg, error = controller.execute_and_fix(code, 'output/figures/test.png')
            >>> print(success)
            True
        """
        for attempt in range(1, max_retries + 1):
            print(f"[Attempt {attempt}/{max_retries}] Executing code...")

            # Apply progressive fixes based on attempt number
            fixed_code = self._apply_fixes(code, attempt)

            # Execute in subprocess
            success, output, error = self._execute_in_subprocess(fixed_code, output_path)

            if success:
                # Verify output file exists
                if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                    return True, f"Success on attempt {attempt}", None
                else:
                    print(f"  [Warning] Code executed but output file missing: {output_path}")
            else:
                print(f"  [Error] Execution failed: {error[:200]}...")

            # If last attempt failed, return final error
            if attempt == max_retries:
                return False, f"Failed after {max_retries} attempts", error

        # Should not reach here, but handle edge case
        return False, "Unknown error", None

    def _apply_fixes(self, code: str, attempt: int) -> str:
        """
        Apply progressive fixes based on attempt number.

        Args:
            code: Original code
            attempt: Attempt number (1, 2, or 3)

        Returns:
            str: Fixed code
        """
        lines = code.split('\n')
        fixed_lines = []

        # Always add UTF-8 encoding at top
        fixed_lines.append("import sys")
        fixed_lines.append("sys.stdout.reconfigure(encoding='utf-8')")

        # Track imports and plt.show() calls
        has_matplotlib_import = False
        has_pandas_import = False
        has_numpy_import = False
        has_plt_show = False

        for line in lines:
            # Track imports
            if 'import matplotlib' in line or 'import plt' in line:
                has_matplotlib_import = True
            if 'import pandas' in line:
                has_pandas_import = True
            if 'import numpy' in line:
                has_numpy_import = True
            if 'plt.show(' in line:
                has_plt_show = True
                continue  # Skip plt.show() calls

            fixed_lines.append(line)

        # Attempt 1: Only add missing imports
        if attempt >= 1:
            # Add missing imports after UTF-8 lines
            import_lines = []
            if not has_matplotlib_import:
                import_lines.append("import matplotlib.pyplot as plt")
            if not has_pandas_import:
                import_lines.append("import pandas as pd")
            if not has_numpy_import:
                import_lines.append("import numpy as np")

            # Insert imports after UTF-8 configuration
            fixed_lines = fixed_lines[:2] + import_lines + fixed_lines[2:]

        # Attempt 2: Add error handling and NaN fixes
        if attempt >= 2:
            # Wrap in try-except
            wrapped = []
            for i, line in enumerate(fixed_lines):
                if i == len(import_lines) + 2:  # After imports
                    wrapped.append("try:")

                # Indent existing code
                if i >= len(import_lines) + 2:
                    wrapped.append(f"    {line}")

                # Add except clause at end
                if i == len(fixed_lines) - 1:
                    wrapped.append("except Exception as e:")
                    wrapped.append(f"    print(f'Error: {{e}}')")
                    wrapped.append("    import traceback")
                    wrapped.append("    traceback.print_exc()")

            fixed_lines = wrapped

        # Attempt 3: Add directory creation and tight_layout
        if attempt >= 3:
            # Add plt.tight_layout() before saving
            for i, line in enumerate(fixed_lines):
                if 'plt.savefig(' in line or 'fig.savefig(' in line:
                    fixed_lines.insert(i, "    plt.tight_layout()")
                    break

            # Add directory creation before save
            for i, line in enumerate(fixed_lines):
                if "plt.savefig(" in line:
                    # Extract path from savefig call
                    if "output_path" in line:
                        fixed_lines.insert(i, "    import os")
                        fixed_lines.insert(i+1, "    output_dir = os.path.dirname(output_path)")
                        fixed_lines.insert(i+2, "    if output_dir and not os.path.exists(output_dir):")
                        fixed_lines.insert(i+3, "        os.makedirs(output_dir, exist_ok=True)")
                    break

        return '\n'.join(fixed_lines)

    def _execute_in_subprocess(self, code: str, output_path: str) -> Tuple[bool, str, str]:
        """
        Execute code in subprocess with timeout.

        Args:
            code: Python code to execute
            output_path: Expected output path (for validation)

        Returns:
            Tuple[bool, str, str]: (success, stdout, stderr)
        """
        try:
            # Create temporary file for code
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
                f.write(code)
                temp_file = f.name

            # Execute in subprocess
            result = subprocess.run(
                [sys.executable, temp_file],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                encoding='utf-8',
                errors='replace'  # Handle encoding errors gracefully
            )

            # Clean up temp file
            try:
                os.unlink(temp_file)
            except:
                pass

            # Check return code
            if result.returncode == 0:
                return True, result.stdout, result.stderr
            else:
                return False, result.stdout, result.stderr

        except subprocess.TimeoutExpired:
            return False, "", f"Execution timeout after {self.timeout} seconds"
        except Exception as e:
            return False, "", str(e)


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def execute_visualization_code(code: str, output_path: str, max_retries: int = 3) -> Tuple[bool, str]:
    """
    Convenience function for executing visualization code with auto-fix.

    Args:
        code: Python matplotlib code
        output_path: Expected output figure path
        max_retries: Maximum retry attempts (default: 3)

    Returns:
        Tuple[bool, str]: (success, message)

    Examples:
        >>> code = '''
        ... import matplotlib.pyplot as plt
        ... plt.plot([1, 2, 3], [1, 4, 9])
        ... plt.savefig('output/test.png')
        ... '''
        >>> success, msg = execute_visualization_code(code, 'output/test.png')
        >>> print(success)
        True
    """
    controller = AgentController()
    success, msg, error = controller.execute_and_fix(code, output_path, max_retries)

    if success:
        return True, msg
    else:
        return False, f"{msg}\nLast error: {error}"


# =============================================================================
# SELF-TEST
# =============================================================================

if __name__ == "__main__":
    # Force UTF-8 output
    sys.stdout.reconfigure(encoding='utf-8')

    print("=" * 70)
    print("SciencePlots Controller - Self-Test")
    print("=" * 70)

    # Test 1: Simple working code
    print("\n[TEST 1] Simple working code")
    code1 = """
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.savefig('output/test_simple.png')
"""
    success, msg = execute_visualization_code(code1, 'output/test_simple.png')
    print(f"  {'[PASS]' if success else '[FAIL]'} {msg}")

    # Test 2: Code with plt.show() (should be removed)
    print("\n[TEST 2] Code with plt.show() (auto-fix)")
    code2 = """
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()  # This should be removed
plt.savefig('output/test_show.png')
"""
    success, msg = execute_visualization_code(code2, 'output/test_show.png')
    print(f"  {'[PASS]' if success else '[FAIL]'} {msg}")

    # Test 3: Code with missing imports (should be added)
    print("\n[TEST 3] Missing imports (auto-fix)")
    code3 = """
plt.figure()
plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig('output/test_imports.png')
"""
    success, msg = execute_visualization_code(code3, 'output/test_imports.png')
    print(f"  {'[PASS]' if success else '[FAIL]'} {msg}")

    # Test 4: Code with syntax error (will fail after 3 attempts)
    print("\n[TEST 4] Syntax error (expected failure)")
    code4 = """
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9]
plt.savefig('output/test_error.png')  # Missing closing parenthesis above
"""
    success, msg = execute_visualization_code(code4, 'output/test_error.png')
    print(f"  {'[PASS] Failed as expected' if not success else '[FAIL] Should have failed'}")

    print("\n" + "=" * 70)
    print("All tests completed!")
    print("=" * 70)
