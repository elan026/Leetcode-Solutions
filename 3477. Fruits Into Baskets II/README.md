# 🟢 Fruits Into Baskets II - LeetCode (Easy)  

## 📌 Problem Statement  

You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where:  

- `fruits[i]` represents the **quantity** of the `i-th` type of fruit.  
- `baskets[j]` represents the **capacity** of the `j-th` basket.  

### **Rules for Placing Fruits:**  

1. Each fruit type **must be placed** in the **leftmost available** basket with a capacity **greater than or equal** to the quantity of that fruit type.  
2. Each basket can **hold only one type** of fruit.  
3. If a fruit type **cannot be placed** in any basket, it remains **unplaced**.  

The goal is to return the **number of fruit types** that remain **unplaced** after all possible allocations are made.  

---

## 🔹 Example  

### **Example 1:**  
```python
Input: fruits = [4,2,5], baskets = [3,5,4]  
Output: 1  
