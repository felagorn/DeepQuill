from . import Optimizer
from ..core import Tensor

_State = Tensor | dict[str, "_State"]

class SGD(Optimizer):

    def __init__(self, params: dict[str, _State], lr: float = 0.001, momentum: float = 0.):
        super().__init__(params)
        self.lr: float = lr
        self.momentum: float = momentum
    
    def step(self) -> None:
        def _sgd_step(x: Tensor) -> None:
            if self.momentum != 0:
                if x.velocity is None:
                    x.velocity = self.lr * x.grad
                else:
                    x.velocity = (self.momentum * x.velocity) + (self.lr * x.grad)
                x.grad = x.velocity
            x.nd -= x.grad
        self._modify_params(_sgd_step)