# Detect Cycle in Linked List

Python solution for the LeetCode problem **Linked List Cycle**.

## Problem

Given the head of a linked list, determine whether the linked list contains a cycle.

Return:

- `True` if a cycle exists
- `False` otherwise

## Approach

This solution uses **Floyd's Cycle Detection Algorithm** (also known as the **Tortoise and Hare Algorithm**).

Two pointers traverse the list:

- the slow pointer moves one node at a time
- the fast pointer moves two nodes at a time

If a cycle exists, the two pointers will eventually meet.

If the fast pointer reaches the end of the list, no cycle exists.

## Complexity

- Time: **O(n)**
- Space: **O(1)**

## Technologies

- Python 3

## Repository Structure

```
main.py
```

The file contains:

- implementation of the `Node` class
- creation of a sample linked list
- creation of a cyclic list for testing
- Floyd's cycle detection algorithm
- simple demonstration in the console

## Learning Goal

This project was created while practicing linked list algorithms and preparing for technical interviews.
