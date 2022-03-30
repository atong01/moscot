import numpy as np
import numpy.typing as npt

from moscot.solvers._output import MatrixSolverOutput


class TestSolverOutput(MatrixSolverOutput):
    @property
    def cost(self) -> float:
        return 0.5

    @property
    def converged(self) -> bool:
        return True

    def _ones(self, n: int) -> npt.ArrayLike:
        return np.ones(n)
