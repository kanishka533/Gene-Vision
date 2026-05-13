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

    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post(
      "http://localhost:5000/analyze",
      formData
    );

    setResult(response.data);
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

  return (
    <div className="app">
export default App;