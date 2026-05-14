import React, { useState } from "react";
import axios from "axios";

import {
Chart as ChartJS,
CategoryScale,
LinearScale,
PointElement,
LineElement,
ArcElement,
BarElement,
Tooltip,
Legend,
} from "chart.js";

import { Line, Pie, Bar } from "react-chartjs-2";

import "./App.css";

ChartJS.register(
CategoryScale,
LinearScale,
PointElement,
LineElement,
ArcElement,
BarElement,
Tooltip,
Legend
);

function App() {
const [file, setFile] = useState(null);
const [result, setResult] = useState(null);

const handleUpload = async () => {
if (!file) return;

```
const formData = new FormData();
formData.append("file", file);

try {
  const response = await axios.post(
    "http://localhost:5000/analyze",
    formData
  );

  setResult(response.data);
} catch (error) {
  console.log(error);
  alert("Backend not connected");
}
```

};

const qualityData = {
labels: ["1", "2", "3", "4", "5", "6"],
datasets: [
{
label: "Quality Score",
data: [90, 88, 95, 92, 97, 94],
},
],
};

const mutationData = {
labels: ["SNP", "Insertion", "Deletion"],
datasets: [
{
label: "Mutation Count",
data: [12, 4, 2],
},
],
};

const gcData = {
labels: ["GC Content", "Other"],
datasets: [
{
data: [52, 48],
},
],
};

return ( <div className="app"> <h1>🧬 GeneScope Pipeline</h1>

```
  <p className="subtitle">
    NGS Data Processing & Genomic Visualization Platform
  </p>

  <div className="upload-box">
    <input
      type="file"
      onChange={(e) => setFile(e.target.files[0])}
    />

    <button onClick={handleUpload}>
      Analyze FASTQ
    </button>
  </div>

  {result && (
    <>
      <div className="cards">
        <div className="card">
          <h2>Total Reads</h2>
          <p>{result.reads}</p>
        </div>

        <div className="card">
          <h2>GC Content</h2>
          <p>{result.gc_content}%</p>
        </div>

        <div className="card">
          <h2>Mutations</h2>
          <p>{result.mutations}</p>
        </div>

        <div className="card">
          <h2>Quality Score</h2>
          <p>{result.quality_score}%</p>
        </div>
      </div>

      <div className="charts">
        <div className="chart-box">
          <h2>Quality Analysis</h2>
          <Line data={qualityData} />
        </div>

        <div className="chart-box">
          <h2>GC Distribution</h2>
          <Pie data={gcData} />
        </div>

        <div className="chart-box">
          <h2>Mutation Analysis</h2>
          <Bar data={mutationData} />
        </div>
      </div>

      <div className="mutation-viewer">
        <h2>Mutation Viewer</h2>

        <div className="chromosome">
          <div className="mutation-dot dot1"></div>
          <div className="mutation-dot dot2"></div>
          <div className="mutation-dot dot3"></div>
        </div>
      </div>

      <a
        href="http://localhost:5000/report"
        target="_blank"
        rel="noreferrer"
      >
        <button className="download-btn">
          Download Genomic Report
        </button>
      </a>
    </>
  )}
</div>
```

);
}

export default App;
