import React, { useState } from 'react';
import axios from 'axios';

function ExecucaoScripts() {
  const [nomeScript, setNomeScript] = useState('');
  const [saida, setSaida] = useState('');
  const [carregando, setCarregando] = useState(false);

  const executarScript = async () => {
    if (!nomeScript.trim()) {
      alert('Por favor, informe o nome do script.');
      return;
    }
    setCarregando(true);
    setSaida('');
    try {
      const res = await axios.post('http://localhost:8000/api/openmanus/executar', {
        nome_script: nomeScript,
      });
      setSaida(res.data.saida);
    } catch (error) {
      setSaida('Erro ao executar script: ' + error.message);
    }
    setCarregando(false);
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h2 className="text-xl font-bold mb-4">Execução de Scripts OpenManus</h2>
      <input
        type="text"
        className="border p-2 rounded w-full mb-4"
        placeholder="Nome do script (sem extensão)"
        value={nomeScript}
        onChange={(e) => setNomeScript(e.target.value)}
      />
      <button
        onClick={executarScript}
        disabled={carregando}
        className="bg-purple-600 text-white px-4 py-2 rounded hover:bg-purple-700"
      >
        {carregando ? 'Executando...' : 'Executar Script'}
      </button>
      <pre className="mt-4 p-2 border rounded bg-gray-50 whitespace-pre-wrap">{saida}</pre>
    </div>
  );
}

export default ExecucaoScripts;
