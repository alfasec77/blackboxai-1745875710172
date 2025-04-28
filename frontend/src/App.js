import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import PainelPrincipal from './componentes/PainelPrincipal';
import InteracaoGPTNeo from './componentes/InteracaoGPTNeo';
import GerenciadorTreinamento from './componentes/GerenciadorTreinamento';
import ExecucaoScripts from './componentes/ExecucaoScripts';
import GerenciadorDocling from './componentes/GerenciadorDocling';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<PainelPrincipal />} />
        <Route path="/gpt-neo" element={<InteracaoGPTNeo />} />
        <Route path="/treinamento" element={<GerenciadorTreinamento />} />
        <Route path="/scripts" element={<ExecucaoScripts />} />
        <Route path="/docling" element={<GerenciadorDocling />} />
      </Routes>
    </Router>
  );
}

export default App;
