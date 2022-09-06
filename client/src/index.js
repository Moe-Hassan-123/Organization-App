import ReactDOM from "react-dom";
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Layout from "./pages/Layout"
import Main from "./pages/Main"

export default function App() {
  return (
    <div>
      <Main />
    </div>
    );
}

const container = document.getElementById('root');
const root = createRoot(container); // createRoot(container!) if you use TypeScript
root.render(<App />);