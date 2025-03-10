# 🔵 Partition Array According to Given Pivot - LeetCode (Medium)  

## 📌 Problem Statement  

You are given a **0-indexed** integer array `nums` and an integer `pivot`.  

**Rearrange** `nums` such that:  
1. All elements **less than** `pivot` appear **before** elements **equal to** `pivot`.  
2. All elements **equal to** `pivot` appear **before** elements **greater than** `pivot`.  
3. The **relative order** of elements in each of the three groups is **maintained**.  

Return the **rearranged array**.  

---

## 🔹 Example  

### **Example 1:**  
```python
Input: nums = [9,12,5,10,14,3,10], pivot = 10  
Output: [9,5,3,10,10,12,14]  
