# 🟢 Search Insert Position - LeetCode (Easy)  

## 📌 Problem Statement  

Given a **sorted** array of distinct integers `nums` and a target value `target`, return the **index** where `target` should be inserted **to maintain order**.  

If `target` is found in `nums`, return its index. Otherwise, return the **index where it would be if it were inserted in order**.  

You **must** write an algorithm with `O(log n)` runtime complexity.  

---

## 🔹 Example  

### **Example 1:**  
```python
Input: nums = [1,3,5,6], target = 5  
Output: 2  
Explanation: Target `5` is found at index `2`.

### **Example 2:**  
```python
Input: nums = [1,3,5,6], target = 2  
Output: 1  
Explanation: `2` should be inserted at index `1` to maintain order.

### **Example 3:**  
```python
Input: nums = [1,3,5,6], target = 7  
Output: 4  
Explanation: `7` should be inserted at index `4` (end of array).

### **Example 4:**  
```python
Input: nums = [1,3,5,6], target = 0  
Output: 0  
Explanation: `0` should be inserted at index `0` (beginning of array).
