from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- LOGIC TRANSLATOR CLASS ---
class LogicTranslator:
    def __init__(self):
        self.symbol_table = {}
        self.symbol_counter = 0

    def normalize(self, text):
        text = text.lower().strip()
        while "  " in text:
            text = text.replace("  ", " ")
        return text

    def assign_symbol(self, proposition):
        if proposition not in self.symbol_table:
            self.symbol_table[proposition] = chr(ord('p') + self.symbol_counter)
            self.symbol_counter += 1
        return self.symbol_table[proposition]

    def contains_embedded_not(self, sentence):
        return " not " in sentence

    def translate(self, sentence):
        sentence = self.normalize(sentence)
        
        # IF ... THEN
        if "if" in sentence and ("then" in sentence or "," in sentence):
            if "then" in sentence:
                parts = sentence.split("then", 1)
                antecedent = parts[0].split("if", 1)[1].strip()
                consequent = parts[1].strip()
            else: 
                parts = sentence.split(",", 1)
                antecedent = parts[0].split("if", 1)[1].strip()
                consequent = parts[1].strip()
            return f"({self.translate(antecedent)} → {self.translate(consequent)})"

        # AND
        if " and " in sentence:
            parts = [p.strip() for p in sentence.split(" and ")]
            translated = [self.translate(p) for p in parts]
            return "(" + " ∧ ".join(translated) + ")"

        # OR
        if " or " in sentence:
            parts = [p.strip() for p in sentence.split(" or ")]
            translated = [self.translate(p) for p in parts]
            return "(" + " ∨ ".join(translated) + ")"

        # NOT
        if self.contains_embedded_not(sentence):
            positive_form = sentence.replace(" not ", " ", 1)
            symbol = self.assign_symbol(positive_form.strip())
            return f"¬{symbol}"

        return self.assign_symbol(sentence)

# --- ROUTES ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def get_translation():
    data = request.get_json()
    user_input = data.get('text', '')

    if not user_input:
        return jsonify({'symbolic': '', 'legend': {}})

    translator = LogicTranslator()
    try:
        result = translator.translate(user_input)
        # Swap keys/values for the legend so it reads P: "proposition"
        legend_data = {v: k for k, v in translator.symbol_table.items()}
        return jsonify({'symbolic': result, 'legend': legend_data})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)