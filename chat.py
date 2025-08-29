import tkinter as tk
from tkinter import scrolledtext

# Simple knowledge base
knowledge = {
    "ai": "AI stands for Artificial Intelligence. It is the simulation of human intelligence in machines.",
    "machine learning": "Machine Learning is a subset of AI that allows systems to learn from data.",
    "deep learning": "Deep Learning uses neural networks with many layers to learn complex patterns.",
    "python": "Python is a powerful high-level programming language used in AI, data science, and web development.",
    "blockchain": "Blockchain is a decentralized ledger technology used in cryptocurrencies and secure data sharing."
}

def answer_question():
    user_q = question_entry.get("1.0", tk.END).strip().lower()
    response = "🤔 Sorry, I don’t know the answer to that yet."
    
    for key in knowledge:
        if key in user_q:
            response = knowledge[key]
            break
    
    answer_box.config(state="normal")
    answer_box.delete("1.0", tk.END)
    answer_box.insert(tk.END, response)
    answer_box.config(state="disabled")

# GUI setup
root = tk.Tk()
root.title("Q&A Smart App")
root.geometry("500x400")
root.configure(bg="black")

# Question input
tk.Label(root, text="Ask me anything:", font=("Helvetica", 14, "bold"), fg="cyan", bg="black").pack(pady=5)
question_entry = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=4, font=("Helvetica", 12))
question_entry.pack(pady=10)

# Submit button
tk.Button(root, text="Get Answer", font=("Helvetica", 12, "bold"), command=answer_question, bg="lime", fg="black").pack(pady=5)

# Answer output
tk.Label(root, text="Answer:", font=("Helvetica", 14, "bold"), fg="yellow", bg="black").pack(pady=5)
answer_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=8, font=("Helvetica", 12), state="disabled")
answer_box.pack(pady=10)

# Run App
root.mainloop()
