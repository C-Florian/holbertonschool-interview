# Lockboxes

## Project Description

The Lockboxes project consists of determining whether all boxes can be opened given a set of keys distributed across those boxes.

Each box may contain keys to other boxes. A key with the same number as a box opens that box. The first box (box 0) is unlocked by default.

The goal is to simulate the process of collecting keys and opening boxes to check if it is possible to open all boxes starting from box 0.

---

## Problem Explanation

- You are given n locked boxes, numbered from 0 to n - 1
- Each box may contain keys to other boxes
- A key opens the box with the same number
- Some keys may not correspond to any box and must be ignored
- Box 0 is already unlocked
- Each box can be opened only once

The task is to determine whether it is possible to open all the boxes by collecting and using the keys found along the way.

---

## Solution Strategy

The solution follows a progressive exploration approach:

1. Start with box 0, which is already open
2. Collect the keys inside the opened box
3. Use the keys to open new boxes
4. Collect new keys from those boxes
5. Repeat the process until no new boxes can be opened
6. Check if all boxes have been opened

This approach ensures that all reachable boxes are explored exactly once.

---

## Example

```python
boxes = [[1, 2], [3], [], [4], []]
