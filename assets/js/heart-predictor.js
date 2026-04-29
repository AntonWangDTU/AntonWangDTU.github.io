"use strict";
const API_URL = "https://resplendent-growth-production-e0d9.up.railway.app/predict";
async function predict() {
    const resultDiv = document.getElementById("heart-result");
    const button = document.getElementById("heart-submit");
    const getValue = (id) => parseInt(document.getElementById(id).value, 10);
    const body = new URLSearchParams({
        age: getValue("age").toString(),
        sex: getValue("sex").toString(),
        cp: getValue("cp").toString(),
        trestbps: getValue("trestbps").toString(),
        chol: getValue("chol").toString(),
        thalach: getValue("thalach").toString(),
        exang: getValue("exang").toString(),
    });
    button.disabled = true;
    resultDiv.innerHTML = "<em>Predicting...</em>";
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: body.toString(),
        });
        if (!response.ok)
            throw new Error(`HTTP ${response.status}`);
        const data = await response.json();
        const pct = (data.probability * 100).toFixed(1);
        const risk = data.prediction === 1 ? "High Risk" : "Low Risk";
        const color = data.prediction === 1 ? "#e74c3c" : "#27ae60";
        resultDiv.innerHTML = `
      <div style="margin-top:1rem; padding:1rem; border-radius:8px; border: 2px solid ${color}; text-align:center;">
        <div style="font-size:1.4rem; font-weight:bold; color:${color};">${risk}</div>
        <div style="font-size:1rem; margin-top:0.3rem;">Probability: <strong>${pct}%</strong></div>
      </div>`;
    }
    catch (err) {
        resultDiv.innerHTML = `<div style="color:#e74c3c; margin-top:1rem;">Error: could not reach the prediction API.</div>`;
    }
    finally {
        button.disabled = false;
    }
}
document.getElementById("heart-submit").addEventListener("click", predict);
