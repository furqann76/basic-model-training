```markdown
# 📈 Basic Linear Regression Model in Python with FastAPI

This project demonstrates how to **train a basic linear regression model from scratch using plain Python** (no ML frameworks) and expose it via a **FastAPI** server for real-time predictions.

---

## 🧠 What It Does

- Loads training data from a CSV file (`data.csv`)
- Trains a linear regression model manually using gradient descent
- Saves the trained model weights
- Runs a FastAPI server to predict outputs based on new input

---

## 📁 Project Structure

```

.
├── data.csv        # Training data (CSV)
├── model.py        # Training script (manual gradient descent)
├── model.npy       # Saved model weights
├── main.py         # FastAPI app for serving predictions
├── README.md       # Project description

````

---

## 📊 Sample Data (`data.csv`)

```csv
x,y
1,2
2,4
3,6
4,8
5,10
````

---

## 🚀 How to Run

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Train the Model

```bash
python model.py
```

Expected output:

```
Model trained: y = 2.00x + 0.02
```

### 3. Start FastAPI Server

```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
Use the `/predict/` endpoint to test.

## 📚 Technologies Used

* Python 3
* NumPy (for calculations)
* FastAPI (for serving the model)

---

## ✅ Ideal For

* Beginners learning ML fundamentals
* Understanding how ML works under the hood
* Integrating a trained model with APIs

---

## 👤 Author

Furqan Hafeez
