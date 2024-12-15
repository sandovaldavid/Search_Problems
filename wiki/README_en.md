# Problem 01

## The Missionaries and Cannibals Problem

The **Missionaries and Cannibals problem** is another classic logic puzzle involving moving a group of people across a river while respecting certain restrictions. It is very similar to the problem of the farmer, the wolf, the goat, and the cabbage, but with a different narrative and a unique set of constraints.

---

### **Problem Description**

Three missionaries and three cannibals need to cross a river using a boat that can hold up to two people. There is an important restriction: at no point can the number of cannibals on one side of the river exceed the number of missionaries (if missionaries are present), as the cannibals would eat the missionaries.

#### **Rules:**

1. The boat can carry one or two people per trip.
2. There must be at least one person in the boat for it to move.
3. The number of cannibals cannot exceed the number of missionaries on either side of the river.
4. The goal is to get everyone (missionaries and cannibals) to the other side of the river without the missionaries being eaten.

---

### **Initial and Goal States**

- **Initial state:**  
  All missionaries and cannibals are on the left side of the river:  
  `(Mission_L, Cannib_L, Boat)` = `(3, 3, L)`

- **Goal state:**  
  All missionaries and cannibals are on the right side of the river:  
  `(Mission_L, Cannib_L, Boat)` = `(0, 0, R)`

---

### **Step-by-Step Solution**

The solution involves moving people back and forth across the river while adhering to the rules. For example:

1. **First trip:** 2 cannibals cross the river.  
   State: `(3, 1, L)` on the left side; `(0, 2, R)` on the right side.

2. **Return trip:** 1 cannibal returns.  
   State: `(3, 2, L)` and `(0, 1, R)`.

3. **Second trip:** 2 cannibals cross again.  
   State: `(3, 0, L)` and `(0, 3, R)`.

4. **Return trip:** 1 cannibal returns.  
   State: `(3, 1, L)` and `(0, 2, R)`.

5. **Third trip:** 2 missionaries cross the river.  
   State: `(1, 1, L)` and `(2, 2, R)`.

6. **Return trip:** 1 missionary and 1 cannibal return.  
   State: `(2, 2, L)` and `(1, 1, R)`.

... and so on, until everyone has crossed.

---

### **Formal Representation**

Each state is represented as a tuple `(Mission_L, Cannib_L, Boat)`, where:

- `Mission_L` is the number of missionaries on the left side.
- `Cannib_L` is the number of cannibals on the left side.
- `Boat` indicates the position of the boat (`L` or `R`).

The goal state is `(0, 0, R)`.

---

### **Solving with BFS or DFS**

The problem can be solved using breadth-first search (BFS) or depth-first search (DFS) to explore all possible states and find a valid solution that satisfies the constraints.
