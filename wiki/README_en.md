# Problem 02

## Water Jugs Puzzle

The **Water Jugs Puzzle** is a classic logic problem that involves measuring an exact amount of water using jugs of different capacities. Despite the fact that the jugs have no intermediate markings, you can fill, empty, or transfer water between them to reach the target amount.

### Problem Statement

Suppose you have two jugs:

- **Jug A** with a capacity of `m` liters.
- **Jug B** with a capacity of `n` liters.

Your goal is to measure exactly `d` liters of water, where:

- `0 < d ≤ max(m, n)`.
- It is possible to achieve this using the allowed operations.

### Allowed Operations

1. **Fill**: You can fill either of the jugs to its maximum capacity.
2. **Empty**: You can completely empty either of the jugs.
3. **Transfer**: You can pour water from one jug into the other until:
   - The first jug is empty, or
   - The second jug is full.

### Classic Example

You have a **3-liter** jug and a **5-liter** jug, and you need to measure exactly **4 liters**.

#### Solution

1. Fill the 5-liter jug (5, 0).
2. Transfer water from the 5-liter jug to the 3-liter jug (2, 3).
3. Empty the 3-liter jug (2, 0).
4. Transfer the remaining water from the 5-liter jug to the 3-liter jug (0, 2).
5. Fill the 5-liter jug again (5, 2).
6. Transfer water from the 5-liter jug to the 3-liter jug (4, 3).

### Mathematical Relation

The problem has a solution if and only if:

1. `d` is a multiple of the greatest common divisor (**GCD**) of `m` and `n`.
2. `d` does not exceed the maximum capacity of the jugs.
