import io
import contextlib
import traceback
import matplotlib.pyplot as plt


class CodeExecutorAgent:

    def execute(self, code, df):

        output_buffer = io.StringIO()

        local_scope = {
            "df": df,
            "plt": plt
        }

        try:

            with contextlib.redirect_stdout(output_buffer):
                exec(code, {}, local_scope)

            return {
                "success": True,
                "output": output_buffer.getvalue(),
                "error": None,
                "figure": plt.gcf()
            }

        except Exception:

            return {
                "success": False,
                "output": output_buffer.getvalue(),
                "error": traceback.format_exc(),
                "figure": None
            }