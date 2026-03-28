#  Monty Hall Problem — Probability Explanation & Simulation

##  Overview

The **Monty Hall Problem** is a classic probability puzzle that demonstrates how human intuition can fail in **conditional probability** scenarios.

It is based on a game show setup where a contestant must choose between multiple doors to win a prize. Despite appearing simple, the problem reveals a surprising result that contradicts common intuition.

---

##  Problem Statement

* There are **3 doors**:

  * Behind one door is a **car**  (the prize)
  * Behind the other two are **goats** 

###  Steps:

1. The contestant selects one door (e.g., Door 1)
2. The host (Monty Hall), who knows what is behind each door:

   * Opens another door (not chosen by the contestant)
   * Always reveals a **goat**
3. The contestant is given a choice:

   * **Stay** with the original door
   * **Switch** to the remaining unopened door

---

##  Key Question

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

After the host reveals a goat:

* The **1/3 probability remains** with the original choice
* The **2/3 probability shifts** to the remaining unopened door

###  Why does this happen?

Because the host’s behavior is **not random**:

* The host always knows where the car is
* The host never opens the door with the car
* The host always reveals a goat

 This means the host is **providing information**, not redistributing probability.

---

##  Extended Intuition (100 Doors Scenario)

Consider a variation with **100 doors**:

* 1 car and 99 goats
* You pick 1 door → probability = **1/100**
* Remaining doors → probability = **99/100**

The host then:

* Opens **98 doors**, all showing goats
* Leaves **one door unopened**

Now:

* Your door still has **1/100 probability**
* The remaining door has **99/100 probability**

 This clearly shows why **switching is far better**.

---

##  Simulation Approach

To verify the theoretical result, we can simulate the Monty Hall game using Python.

###  Simulation Logic

Each simulation follows these steps:

1. Randomly place the **car** behind one of the doors
2. The player randomly selects a door
3. The host:

   * Opens a door with a **goat**
   * Never opens the player's chosen door
   * Never reveals the car
4. The player then:

   * Either **stays** with the original choice
   * Or **switches** to the remaining door
5. Record whether the player **wins or loses**

---

### Repeated Trials

* The simulation is repeated **thousands of times** (e.g., 10,000+ trials)
* This helps approximate the true probabilities using **experimental frequency**

---

###  Sample Results

| Strategy | Probability (Approx) |
| -------- | -------------------- |
| Stay     | ~0.33                |
| Switch   | ~0.66                |

 As the number of trials increases, results converge to the theoretical values:

* Stay → **1/3**
* Switch → **2/3**

---

## Key Insight

> The host’s action does not redistribute probability — it reveals information.

The probability of the unchosen doors is effectively **concentrated into the remaining unopened door**.

---

##  Conclusion

The Monty Hall Problem teaches us that:

* Initial choices have fixed probabilities
* Additional information changes decision-making
* Human intuition can fail in probabilistic reasoning

 **Switching doors doubles your chance of winning.**

---

##  Tags

`Probability` `Statistics` `Simulation` `Game Theory` `Mathematics` `Logic`
