# 🎯 Monty Hall Problem — Probability Explanation

##  Overview

The **Monty Hall Problem** is a classic probability puzzle that demonstrates how human intuition can fail in conditional probability scenarios.

It is based on a game show setup where a contestant must choose between multiple doors to win a prize.

---

##  Problem Statement

* There are **3 doors**:

  * Behind one door is a **car** 🚗 (the prize)
  * Behind the other two are **goats** 🐐🐐

### Steps:

1. The contestant selects one door (e.g., Door 1)
2. The host (Monty Hall), who knows the contents behind each door:

   * Opens another door (not chosen by the contestant)
   * Always reveals a **goat**
3. The contestant is then given a choice:

   * **Stay** with the original door
   * **Switch** to the remaining unopened door

---

## Key Question

> Should the contestant **stay**, **switch**, or does it not matter?

---

##  Answer

* Probability of winning by **staying** = **1/3**
* Probability of winning by **switching** = **2/3**

 Therefore, **switching is the optimal strategy**.

---

##  Explanation

When the contestant initially selects a door:

* There is a **1/3 probability** that the chosen door contains the car
* There is a **2/3 probability** that the car is behind one of the other two doors

After the host reveals a goat from the unchosen doors:

* The **1/3 probability remains with the original choice**
* The **2/3 probability transfers to the remaining unopened door**

This occurs because the host's action is **not random**:

* The host always avoids revealing the car
* The host always reveals a goat

Thus, the remaining unopened door effectively represents the combined probability of the unchosen doors.

---

##  Extended Intuition (100 Doors Scenario)

Consider a variation with **100 doors**:

* 1 car and 99 goats
* You pick 1 door → probability = **1/100**
* The remaining 99 doors → probability = **99/100**

The host then:

* Opens **98 doors**, all showing goats
* Leaves **one door unopened**

Now:

* Your door still has a **1/100 probability**
* The remaining door has a **99/100 probability**

 This makes it clear that **switching dramatically increases the chance of winning**.

---

## 📊 Key Insight

> The host’s action does not redistribute probability — it reveals information.

The probability mass of the unchosen doors is effectively concentrated into the single remaining unopened door.

---

##  Conclusion

The Monty Hall Problem illustrates that:

* Initial choices carry fixed probabilities
* Additional information can shift decision-making
* Switching choices can significantly improve outcomes

 **Always switch to maximize your probability of winning.**

---

##  Tags

`Probability` `Statistics` `Game Theory` `Mathematics` `Logic`
