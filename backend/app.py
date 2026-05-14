from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(**name**)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
file = request.files['file']

```
result = {
    "reads": 120000,
    "gc_content": 52,
    "mutations": 18,
    "quality_score": 94
}

return jsonify(result)
```

@app.route('/report')
def report():
filename = "Genomic_Report.pdf"

```
doc = SimpleDocTemplate(filename)
styles = getSampleStyleSheet()

content = []

content.append(Paragraph("GeneScope Genomic Analysis Report", styles['Title']))
content.append(Spacer(1, 20))

content.append(Paragraph("Total Reads: 120000", styles['BodyText']))
content.append(Paragraph("GC Content: 52%", styles['BodyText']))
content.append(Paragraph("Mutation Count: 18", styles['BodyText']))
content.append(Paragraph("Quality Score: 94%", styles['BodyText']))

doc.build(content)

return send_file(filename, as_attachment=True)
```

if **name** == '**main**':
app.run(debug=True)
