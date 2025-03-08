# 🟡 Divide Two Integers - LeetCode (Medium)  

## 📌 Problem Statement  

Given two integers `dividend` and `divisor`, divide them **without using multiplication (`*`), division (`/`), or modulus (`%`)** operators.  

Return the **quotient** after dividing `dividend` by `divisor`.  

🔹 **Note:**  
- The **result must be truncated** (i.e., rounded toward zero).  
- If the quotient is **beyond the range** of a **32-bit signed integer** (`[-2³¹, 2³¹ - 1]`), return `2³¹ - 1` (`2147483647`) if it overflows.  

---

## 🔹 Example  

### **Example 1:**  
```python
Input: dividend = 10, divisor = 3  
Output: 3  
Explanation: 10 / 3 = 3.333.., which is truncated to 3.

### **Example 2:**
Input: dividend = 7, divisor = -3  
Output: -2  
Explanation: 7 / -3 = -2.333.., which is truncated to -2.

### **Example 3:**
Input: dividend = -2147483648, divisor = -1  
Output: 2147483647  
Explanation: The actual quotient is 2147483648, which exceeds 32-bit integer limits.
