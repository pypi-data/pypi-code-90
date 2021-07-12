# This code is part of Qiskit.
#
# (C) Copyright IBM 2019, 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""Exact reciprocal rotation."""

from math import isclose
import numpy as np
from qiskit.circuit import QuantumCircuit, QuantumRegister
from qiskit.extensions.quantum_initializer import UCRYGate


class ExactReciprocal(QuantumCircuit):
    r"""Exact reciprocal

    .. math::

        |x\rangle |0\rangle \mapsto \cos(1/x)|x\rangle|0\rangle + \sin(1/x)|x\rangle |1\rangle
    """

    def __init__(self, num_state_qubits: int, scaling: float, name: str = "1/x") -> None:
        r"""
        Args:
            num_state_qubits: The number of qubits representing the value to invert.
            scaling: Scaling factor of the reciprocal function, i.e. to compute
             ::math:: `scaling / x`.
            name: The name of the object.
        Note:
            It is assumed that the binary string x represents a number < 1.
        """
        qr_state = QuantumRegister(num_state_qubits, "state")
        qr_flag = QuantumRegister(1, "flag")
        circuit = QuantumCircuit(qr_state, qr_flag, name=name)

        angles = [0.0]
        nl = 2 ** num_state_qubits

        for i in range(1, nl):
            if isclose(scaling * nl / i, 1, abs_tol=1e-5):
                angles.append(np.pi)
            elif scaling * nl / i < 1:
                angles.append(2 * np.arcsin(scaling * nl / i))
            else:
                angles.append(0.0)

        circuit.compose(UCRYGate(angles), [qr_flag[0]] + qr_state[:], inplace=True)

        super().__init__(*circuit.qregs, name=name)
        self.compose(circuit.to_gate(), qubits=self.qubits, inplace=True)
