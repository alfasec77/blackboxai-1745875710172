import React, { useState } from 'react';
import axios from 'axios';

function GerenciadorDocling() {
  const [modelo, setModelo] = useState('gpt-neo');
  const [caminhoDados, setCaminhoDados] = useState('');
  const [resposta, setResposta] = useState(null);
  const [carregando, setCarregando] = useState(false);

  const iniciarTreinamento = async () => {
    if (!caminhoDados.trim()) {
      alert('Por favor, informe o caminho dos dados.');
      return;
    }
    setCarregando(true);
    setResposta(null);
    try {
      const res = await axios.post('http://localhost:8000/api/docling/iniciar', {
        modelo,
        caminho_dados: caminhoDados,
      });
      setResposta(res.data);
    } catch (error) {
      setResposta({ status: 'erro', mensagem: error.message });
    }
    setCarregando(false);
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h2 className="text-xl font-bold mb-4">Gerenciador de Treinamento Docling</h2>
      <div className="mb-4">
        <label className="block mb-2">Modelo</label>
        <select
          value={modelo}
          onChange={(e) => setModelo(e.target.value)}
          className="border p-2 rounded w-full"
        >
          <option value="gpt-neo">GPT-Neo</option>
          <option value="openmanus">OpenManus</option>
        </select>
      </div>
      <div className="mb-4">
        <label className="block mb-2">Caminho dos Dados</label>
        <input
          type="text"
          value={caminhoDados}
          onChange={(e) => setCaminhoDados(e.target.value)}
          className="border p-2 rounded w-full"
          placeholder="Ex: /caminho/para/dados"
        />
      </div>
      <button
        onClick={iniciarTreinamento}
        disabled={carregando}
        className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700"
      >
        {carregando ? 'Iniciando...' : 'Iniciar Treinamento'}
      </button>
      {resposta && (
        <div className="mt-4 p-2 border rounded bg-gray-50 whitespace-pre-wrap">
          {JSON.stringify(resposta, null, 2)}
        </div>
      )}
    </div>
  );
}

export default GerenciadorDocling;
