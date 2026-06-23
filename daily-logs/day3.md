# Day 2 — Loss Functions, Gradient Descent, Backpropagation, Overfitting, Underfitting & Train/Val/Test Split

> **#45DaysOfGenAI** • [LinkedIn](https://www.linkedin.com/in/shani-kumar-041177329/) • [GitHub](https://github.com/shanikumar4)

## Loss Functions

A loss function tells us — how wrong is the prediction?

It is very important because every model must minimize the loss, and with the help of a loss function we know at each step how much error happened.

Some common loss functions:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Binary Cross-Entropy
- Categorical Cross-Entropy

## Gradient Descent

Gradient Descent is an optimizer that updates the weights and minimizes the loss.

## Gradient

The gradient tells us in which direction we need to move to update the weight.
If the gradient is positive → move left. If the gradient is negative → move right.

## Learning Rate

Learning rate tells us how fast or how big each step should be while updating the weights.

## Backpropagation

Backpropagation is a technique for minimizing loss. It works step by step — it moves one step backward, updates the weight, calculates the loss, then moves one step back again. This keeps repeating until the loss is minimized.

## Overfitting

The model learns the data too well — including the noise — and gives very high accuracy on training data. But it may fail on new, unseen data.

## Underfitting

The model is too simple and learns very few features, so it gives low accuracy even on training data.

## Train / Val / Test Split

We split the data into three parts — train, val, and test.
- **Train data** — used for training the model
- **Val data** — used for validating the output during training
- **Test data** — used for testing the final model

---

## The One Sentence That Connects Everything

```
Loss tells us HOW WRONG we are,
Backpropagation tells us WHY we are wrong,
Gradients tell us HOW TO FIX it,
Gradient Descent actually FIXES it.
```