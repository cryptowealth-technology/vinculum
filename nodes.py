from dataclasses import dataclass

@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return f"{self.value}"

@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} + {self.node_b})"


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} - {self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} * {self.node_b})"

@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} / {self.node_b})"

@dataclass
class ModuloNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} % {self.node_b})"

@dataclass
class PosNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"

@dataclass
class NegateNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"